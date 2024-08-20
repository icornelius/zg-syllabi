# This Python script generates meeting dates for standard academic course
# schedules. The user is prompted for the meeting pattern (supported options
# are MWF, TuTh, WM, and once-per-week), date of the first meeting, and length
# of the semester. The script is not aware of academic or religious holidays,
# but it handles irregular starts (e.g., a MWF class that meets WF in the first
# week). To simplify input, the script will try to guess the year and month in
# which to begin the sequence. The guess is based on the current date.
#
# Output is formatted as `csv` and previewed in the terminal.  There is an
# option to write the output to a file, by default `meeting-dates.csv` in the
# directory `../schedules/`, which is created if it does not exist. To change
# that path, update the value of the `output_dir` and/or `output_filename`
# variables.
#
# Edit the `csv` to supply content (units, assignments) and record breaks when
# class does not meet. Then run `format-dates.py` to format the finished
# schedule as Markdown. Column labels in the `csv` should not be changed, as
# those are read by `format-dates.py`. See that script for details.

from datetime import datetime, timedelta
import os

output_filename = 'meeting-dates.csv'
output_dir = '../schedules/'

def get_valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        prompt = "Invalid selection. Try again. "

def get_regular_mtg_dates(csv_lines, week, date, mtg_pattern, semester_length):
    if mtg_pattern == 'TuTh' or mtg_pattern == 'MW':
        while week <= int(semester_length):
            string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
            csv_lines.append(string)
            diff = timedelta(days=2)
            date += diff
            string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
            csv_lines.append(string)
            diff = timedelta(days=5)
            date += diff
            week += 1
    elif mtg_pattern == 'MWF':
        while week <= int(semester_length):
            string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
            csv_lines.append(string)
            diff = timedelta(days=2)
            for i in range(2):
                date += diff
                string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
                csv_lines.append(string)
            diff = timedelta(days=3)
            date += diff
            week += 1
    else:
        while week <= int(semester_length):
            string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
            csv_lines.append(string)
            diff = timedelta(days=7)
            date += diff
            week += 1
    return csv_lines

def create_schedule():
    now = datetime.now()
    diff = timedelta(days=365)
    current_year = now.strftime("%Y")
    current_month = now.strftime("%m")
    next_year = (now + diff).strftime("%Y")

    # Get meeting pattern
    print("""\nWhat is the meeting pattern?

       1. TuTh
       2. MWF
       3. MW
       4. Once per week
       """)
    options = []
    for i in range(4):
       options.append(str(i+1))
    prompt = 'Select from the option above (1-4): '

    mtg_pattern = get_valid_input(prompt, options)

    if mtg_pattern == '1':
        mtg_pattern = 'TuTh'
    elif mtg_pattern == '2':
        mtg_pattern = 'MWF'
    elif mtg_pattern == '3':
        mtg_pattern = 'MW'
    else:
        mtg_pattern = 'once per week'

    # Get the year and semester
    if int(current_month) > 9:
        prompt = f"Begin in January {next_year}? (Y/n) "
        default = "spring_next_yr"
    elif int(current_month) < 2:
        prompt = f"Begin in January {current_year}? (Y/n) "
        default = "spring_current_yr"
    else:
        prompt = f"Begin in August {current_year}? (Y/n) "
        default = "fall"
    options = ['y', 'n', '']

    semester_id = get_valid_input(prompt, options)

    if semester_id == 'y' or semester_id == '':
        prompt = "Enter the date of the first meeting (day-number only): "
        semester_id = default
        if semester_id == "spring_next_yr":
            start_month = "01"
            start_year = next_year
        elif semester_id == "spring_current_yr":
            start_month = "01"
            start_year = current_year
        else:
            start_month = "08"
            start_year = current_year
    else:
        prompt = "Enter the date of the first meeting in the format YYYY-MM-DD: "

    # Redefine options to validate the start-date
    if mtg_pattern == 'TuTh':
        options = [2, 4]
    elif mtg_pattern == 'MWF':
        options = [1, 3, 5]
    elif mtg_pattern == 'MW':
        options = [1, 3]
    else:
        options = []
        for i in range(6):
            options.append(i+1)

    # Get a valid start date
    if semester_id == 'n':
        while True:
            choice = input(prompt)
            if bool(datetime.strptime(choice, "%Y-%m-%d")):
                choice = datetime.strptime(choice, "%Y-%m-%d")
                if int(datetime.strftime(choice, "%w")) in options:
                    start_date = choice
                    break
            prompt = "Invalid format or date. Format should be YYYY-MM-DD.\nDate must be consistent with the selected meeting-pattern. Try again: "
    else:
        while True:
            choice = start_year + "-" + start_month + "-" + input(prompt)
            if bool(datetime.strptime(choice, "%Y-%m-%d")):
                choice = datetime.strptime(choice, "%Y-%m-%d")
                if int(datetime.strftime(choice, "%w")) in options:
                    start_date = choice
                    break
            prompt = "Invalid start day. Start day must be consistent with the selected meeting-pattern. Try again: "

    # Get semester length
    options = [] # Set an arbitrary maximum
    for i in range(52):
       options.append(str(i+1))
    options.append('')
    prompt = "Enter the length of the semester in weeks (default 15): "

    semester_length = get_valid_input(prompt, options)
    if len(semester_length) == 0:
        semester_length = '15'

    # Check whether the first week has the full set of meetings
    start_idx = start_date.strftime('%w')
    regular_start = True
    if mtg_pattern == 'TuTh' and start_idx != '2':
        regular_start = False
    elif mtg_pattern == 'MWF' or mtg_pattern == 'MW':
        if start_idx != '1':
            regular_start = False

    # Generate meeting dates as csv
    csv_lines = ['week,date,breaks,unit,assignment_0,assignment_1,assignment_2,assignment_n']
    week = 1
    date = start_date
    if regular_start:
        schedule = get_regular_mtg_dates(csv_lines, week, date, mtg_pattern, semester_length)
    else: # create a custom first-week schedule
        string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
        csv_lines.append(string)
        if mtg_pattern == 'TuTh' or mtg_pattern == 'MW':
            diff = timedelta(days=5)
        else: # WMF beginning W or F
            if start_idx == '3': # MWF beginning W
                diff = timedelta(days=2)
                date += diff
                string = str(week) + ',' + date.strftime("%a %b %d") + 6 * ','
                csv_lines.append(string)
            diff = timedelta(days=3)
        date += diff
        week += 1
        schedule = get_regular_mtg_dates(csv_lines, week, date, mtg_pattern, semester_length)

    # Print a preview
    pretty_date = start_date.strftime("%A, %d %B, %Y")
    print(f"\nPreviewing `csv`-formatted dates for a class that meets {mtg_pattern} for {semester_length} weeks, beginning {pretty_date}.\n")

    if len(schedule) > 20:
        for n in range(10):
            print(schedule[n])
        for n in range(3):
            print('...')
        for n in range(-10, 0):
            print(schedule[n])
    else:
        for n in range(len(schedule)):
            print(schedule[n])

    return schedule

def write_to_file(schedule):
    output_path = os.path.join(output_dir, output_filename)
    prompt = f'Write this schedule to `{output_path}`? (Y/n): '
    options = ['y', 'n', '']
    decision = get_valid_input(prompt, options)

    if decision == 'y' or len(decision) == 0:
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
            print(f'Created a new directory `{output_dir}`.')
        with open(output_path, 'w') as file:
            for line in range(len(schedule)):
                file.write(schedule[line] + '\n')
        print(f'Wrote {str(len(schedule))} lines to {output_path}.')

def main():
    print('Welcome!')
    schedule = create_schedule()
    write_to_file(schedule)
    print('Goodbye.')

main()
