"""Generate meeting dates for a standard academic course schedule.

The user is prompted for the meeting pattern (supported options are MWF, TuTh,
MW, and once-per-week), the date of the first meeting, and the length of the
semester. The script is not aware of academic or religious holidays, but it
handles irregular starts (e.g., a MWF class that meets WF in the first week).
To simplify input, the script guesses the year and month in which to begin the
sequence, based on the current date.

Usage:

python3 date-calculator.py

Output is formatted as `csv` and previewed in the terminal. There is an option
to write the output to a file, by default `meeting-dates.csv` in the directory
`schedules`, which is created if it does not exist. To change that path, update
the value of the `OUTPUT_DIR` and/or `OUTPUT_FILENAME` constants. Paths are
resolved relative to this script, not to the working directory.

Edit the `csv` to supply content (units, assignments) and record breaks when
class does not meet. Then run `date-formatter.py` to format the finished
schedule as Markdown. Column labels in the `csv` should not be changed, as
those are read by `date-formatter.py`. See that script for details.
"""

import calendar
import sys
from datetime import date, timedelta
from functools import partial
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / 'schedules'
OUTPUT_FILENAME = 'meeting-dates.csv'

# Column labels of the generated `csv`. `date-formatter.py` reads these, so
# the first four are fixed; the assignment columns may be added to or removed.
COLUMNS = (
    'week',
    'date',
    'breaks',
    'unit',
    'assignment_0',
    'assignment_1',
    'assignment_2',
    'assignment_n',
)

# Meeting patterns, in the order they are offered in the menu. Each value is
# the set of weekdays on which the semester may begin, as `date.weekday()`
# values (Monday is 0). For every pattern but `WEEKLY` these are also the days
# on which the class meets; a once-per-week class meets on whichever day the
# semester starts, so any weekday but Sunday is permitted there.
WEEKLY = 'once per week'
MEETING_PATTERNS = {
    'TuTh': (calendar.TUESDAY, calendar.THURSDAY),
    'MWF': (calendar.MONDAY, calendar.WEDNESDAY, calendar.FRIDAY),
    'MW': (calendar.MONDAY, calendar.WEDNESDAY),
    WEEKLY: (
        calendar.MONDAY,
        calendar.TUESDAY,
        calendar.WEDNESDAY,
        calendar.THURSDAY,
        calendar.FRIDAY,
        calendar.SATURDAY,
    ),
}

DEFAULT_SEMESTER_WEEKS = 15
MAX_SEMESTER_WEEKS = 52  # An arbitrary maximum

# Number of rows shown at the head and tail of a long preview.
PREVIEW_ROWS = 10


# Prompting


def ask(prompt, parse):
    """Prompt until `parse` accepts the answer, then return the parsed value.

    `parse` takes the raw answer and returns the value to use, or raises
    `ValueError` carrying a message to show the user.
    """
    while True:
        try:
            return parse(input(prompt))
        except ValueError as error:
            print(error)
        except (EOFError, KeyboardInterrupt):
            sys.exit('\nAborted.')


def parse_yes_no(answer, default=True):
    """Interpret a yes/no answer; an empty answer takes `default`."""
    answer = answer.strip().lower()
    if answer == '':
        return default
    if answer in ('y', 'yes'):
        return True
    if answer in ('n', 'no'):
        return False
    raise ValueError('Invalid selection. Answer `y` or `n`.')


def parse_menu_choice(answer, count):
    """Interpret an answer to a numbered menu of `count` options."""
    answer = answer.strip()
    if answer.isdigit() and 1 <= int(answer) <= count:
        return int(answer)
    raise ValueError(f'Invalid selection. Enter a number from 1 to {count}.')


def parse_week_count(answer):
    """Interpret the length of the semester in weeks."""
    answer = answer.strip()
    if answer == '':
        return DEFAULT_SEMESTER_WEEKS
    if answer.isdigit() and 1 <= int(answer) <= MAX_SEMESTER_WEEKS:
        return int(answer)
    raise ValueError(f'Invalid length. Enter a number from 1 to {MAX_SEMESTER_WEEKS}.')


def check_start_weekday(candidate, weekdays):
    """Return `candidate` if the meeting pattern permits it as a start date."""
    if candidate.weekday() in weekdays:
        return candidate
    permitted = ', '.join(calendar.day_name[weekday] for weekday in weekdays)
    raise ValueError(
        f'{candidate:%A}s are inconsistent with the selected meeting pattern. '
        f'The first meeting must fall on one of: {permitted}. Try again.'
    )


def parse_day_number(answer, year, month, weekdays):
    """Interpret a day-number within the guessed month as a start date."""
    try:
        candidate = date(year, month, int(answer.strip()))
    except ValueError:
        last_day = calendar.monthrange(year, month)[1]
        raise ValueError(f'Invalid day. Enter a number from 1 to {last_day}.') from None
    return check_start_weekday(candidate, weekdays)


def parse_iso_date(answer, weekdays):
    """Interpret a full YYYY-MM-DD date as a start date."""
    try:
        candidate = date.fromisoformat(answer.strip())
    except ValueError:
        raise ValueError('Invalid format or date. Format should be YYYY-MM-DD.') from None
    return check_start_weekday(candidate, weekdays)


def ask_meeting_pattern():
    """Prompt for the meeting pattern; return one of the `MEETING_PATTERNS` keys."""
    patterns = list(MEETING_PATTERNS)
    print('\nWhat is the meeting pattern?\n')
    for number, pattern in enumerate(patterns, start=1):
        print(f'       {number}. {pattern.capitalize() if pattern == WEEKLY else pattern}')
    print()
    prompt = f'Select from the options above (1-{len(patterns)}): '
    choice = ask(prompt, partial(parse_menu_choice, count=len(patterns)))
    return patterns[choice - 1]


def guess_term_start(today):
    """Guess the year and month of the next semester to be scheduled."""
    if today.month >= 10:  # Autumn: the next semester starts in the new year
        return today.year + 1, 1
    if today.month == 1:
        return today.year, 1
    return today.year, 8


def ask_start_date(pattern):
    """Prompt for the date of the first meeting."""
    weekdays = MEETING_PATTERNS[pattern]
    year, month = guess_term_start(date.today())
    if ask(f'Begin in {calendar.month_name[month]} {year}? (Y/n) ', parse_yes_no):
        return ask(
            'Enter the date of the first meeting (day-number only): ',
            partial(parse_day_number, year=year, month=month, weekdays=weekdays),
        )
    return ask(
        'Enter the date of the first meeting in the format YYYY-MM-DD: ',
        partial(parse_iso_date, weekdays=weekdays),
    )


# Schedule generation


def meeting_weekdays(pattern, start_date):
    """Return the weekdays on which the class meets in a full week."""
    if pattern == WEEKLY:
        return (start_date.weekday(),)
    return MEETING_PATTERNS[pattern]


def generate_meeting_dates(start_date, pattern, weeks):
    """Yield a (week number, date) pair for every meeting of the semester.

    Week 1 is the calendar week containing `start_date`. Meeting days that
    fall earlier in that week than `start_date` are skipped, so an irregular
    first week (e.g., a MWF class beginning on a Wednesday) needs no special
    handling.
    """
    weekdays = meeting_weekdays(pattern, start_date)
    first_monday = start_date - timedelta(days=start_date.weekday())
    for week in range(weeks):
        monday = first_monday + timedelta(weeks=week)
        for weekday in weekdays:
            meeting = monday + timedelta(days=weekday)
            if meeting >= start_date:
                yield week + 1, meeting


def build_csv_rows(start_date, pattern, weeks):
    """Return the schedule as a list of `csv` rows, header first."""
    empty_columns = ',' * (len(COLUMNS) - 2)  # `week` and `date` are filled in
    rows = [','.join(COLUMNS)]
    rows += [
        f'{week},{meeting:%a %b %d}{empty_columns}'
        for week, meeting in generate_meeting_dates(start_date, pattern, weeks)
    ]
    return rows


def print_preview(rows, start_date, pattern, weeks):
    """Print the schedule, eliding the middle of a long one."""
    print(
        f'\nPreviewing `csv`-formatted dates for a class that meets {pattern} '
        f'for {weeks} weeks, beginning {start_date:%A, %d %B, %Y}.\n'
    )
    if len(rows) <= 2 * PREVIEW_ROWS:
        print('\n'.join(rows))
        return
    elided = len(rows) - 2 * PREVIEW_ROWS
    print('\n'.join(rows[:PREVIEW_ROWS]))
    print(f'... ({elided} more rows) ...')
    print('\n'.join(rows[-PREVIEW_ROWS:]))


def write_to_file(rows):
    """Offer to write the schedule to `OUTPUT_DIR`, confirming any overwrite."""
    output_path = OUTPUT_DIR / OUTPUT_FILENAME
    if not ask(f'Write this schedule to `{output_path}`? (Y/n): ', parse_yes_no):
        return
    if output_path.exists():
        prompt = f'`{output_path}` already exists. Overwrite it? (y/N): '
        if not ask(prompt, partial(parse_yes_no, default=False)):
            print('Left the existing file in place.')
            return
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)
        print(f'Created a new directory `{OUTPUT_DIR}`.')
    output_path.write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print(f'Wrote {len(rows)} lines to {output_path}.')


def main():
    print('Welcome!')
    pattern = ask_meeting_pattern()
    start_date = ask_start_date(pattern)
    weeks = ask(
        f'Enter the length of the semester in weeks (default {DEFAULT_SEMESTER_WEEKS}): ',
        parse_week_count,
    )
    rows = build_csv_rows(start_date, pattern, weeks)
    print_preview(rows, start_date, pattern, weeks)
    write_to_file(rows)
    print('Goodbye.')


if __name__ == '__main__':
    main()
