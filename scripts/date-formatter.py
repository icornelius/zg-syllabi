"""Transform a `csv` course schedule into a Markdown-formatted document.

The `csv` file should be created with the Python script `date-calculator.py`
or match the structure of files produced by that script.

For a list of required column labels, see the constant `REQUIRED_COLUMNS`.
Additional columns are permitted; their values will be rendered only if the
column label begins with 'assignment' (e.g., 'assignment_1', 'assignment_2',
'assignment_n').

Usage:

python3 date-formatter.py [FILEPATH]

FILEPATH may be an absolute path, a path relative to the working directory, or
the name of a file in `DATA_DIR`. If it is not specified on the command line
the script will print a list of `csv` files in `DATA_DIR` and prompt the user
to select one as input.

To change the default directories for reading or writing, edit the values of
`DATA_DIR` or `OUTPUT_DIR`, respectively. Paths are resolved relative to this
script, not to the working directory.
"""

import csv
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / 'schedules'
OUTPUT_DIR = DATA_DIR

REQUIRED_COLUMNS = ('week', 'date', 'breaks', 'unit', 'assignment_0')

# Values in any other column whose label begins with this prefix are rendered
# as list items, in the order the columns appear in the `csv`.
ASSIGNMENT_PREFIX = 'assignment'


# Input


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


def choose_source_path():
    """Prompt the user to choose one of the `csv` files in `DATA_DIR`."""
    if not DATA_DIR.is_dir():
        sys.exit(
            f'Default source directory {DATA_DIR} not found. If your '
            '`csv`-formatted schedules are in another location, update the '
            '`DATA_DIR` variable.'
        )
    csvfiles = sorted(
        path for path in DATA_DIR.iterdir()
        if path.is_file() and path.suffix.lower() == '.csv'
    )
    if not csvfiles:
        sys.exit('No `csv` file found. Aborting.')

    if len(csvfiles) == 1:
        prompt = f'Found 1 `csv` file, {csvfiles[0].name}. Use this one? (Y/n): '
        if not ask(prompt, parse_yes_no):
            sys.exit('No file selected. Aborting.')
        choice = csvfiles[0]
    else:
        print(f'Found {len(csvfiles)} `csv` files:')
        for number, path in enumerate(csvfiles, start=1):
            print(f'\t({number}) {path.name}')
        print(f'\t({len(csvfiles) + 1}) Select none (exit)')
        prompt = 'Enter a number from the options above: '
        number = ask(prompt, lambda answer: parse_menu_choice(answer, len(csvfiles) + 1))
        if number > len(csvfiles):
            sys.exit('No file selected. Aborting.')
        choice = csvfiles[number - 1]

    print(f'Selected `{choice.name}`')
    return choice


def resolve_source_path(argument):
    """Resolve a command-line argument to a `csv` file.

    An absolute path, or a path relative to the working directory, is used as
    given; a bare filename is also looked for in `DATA_DIR`.
    """
    path = Path(argument)
    if path.is_file():
        return path
    candidate = DATA_DIR / path
    if candidate.is_file():
        return candidate
    sys.exit(f'No such file: {argument}')


# Reading and validation


def read_schedule(path):
    """Read `path` as a `csv`; return its column labels and rows.

    Rows are returned as dictionaries in which every column label is present:
    columns missing from a short row are supplied as empty strings, and values
    beyond the labelled columns are discarded.
    """
    with path.open(newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames or []
        rows = [
            {label: value or '' for label, value in row.items() if label is not None}
            for row in reader
        ]
    return columns, rows


def validate_columns(columns):
    """Warn about columns that will be ignored; abort if any are missing."""
    for label in columns:
        if label not in REQUIRED_COLUMNS and not label.startswith(ASSIGNMENT_PREFIX):
            print(f'Warning: values in column {label} will be ignored. Continuing.')
    if any(label not in columns for label in REQUIRED_COLUMNS):
        print('\nColumn labels do not match requirements. Aborting.')
        sys.exit(f'Required column labels: {", ".join(REQUIRED_COLUMNS)}.')


def get_assignment_columns(columns):
    """Return the assignment columns rendered as plain list items.

    `assignment_0` is excluded: it is rendered in bold, ahead of the others.
    """
    return [
        label for label in columns
        if label.startswith(ASSIGNMENT_PREFIX) and label != 'assignment_0'
    ]


# Formatting and output


def format_schedule(rows, assignment_columns):
    """Render the schedule as a list of Markdown lines."""
    lines = []
    previous_unit = ''
    for row in rows:
        if row['unit'] not in ('', previous_unit):
            lines += ['', f'# {row["unit"]} {{.unnumbered}}']
            previous_unit = row['unit']
        lines += ['', f'## {row["date"]} {{.unlisted .unnumbered}}', '']
        if row['breaks']:
            lines.append(f'- **{row["breaks"]}**. Class does not meet.')
        if row['assignment_0']:
            lines.append(f'- **{row["assignment_0"]}**')
        lines += [f'- {row[label]}' for label in assignment_columns if row[label]]
    return lines


def write_to_file(lines, source_path):
    """Write the Markdown lines to `OUTPUT_DIR`, named after the source file."""
    output_path = OUTPUT_DIR / f'{source_path.stem}.md'
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True)
        print(f'Created a new directory `{OUTPUT_DIR}`.')
    output_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'\tWrote {len(lines)} lines to {output_path}')


def main():
    if len(sys.argv) > 1:
        source_path = resolve_source_path(sys.argv[1])
    else:
        source_path = choose_source_path()
    columns, rows = read_schedule(source_path)
    validate_columns(columns)
    assignment_columns = get_assignment_columns(columns)
    write_to_file(format_schedule(rows, assignment_columns), source_path)


if __name__ == '__main__':
    main()
