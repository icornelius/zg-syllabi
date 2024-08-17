# This Python script reads a specified `csv` file and transforms its content
# into a Markdown-formatted document. The `csv` file should be created with the
# Python script `date-calculator.py` or match the structure of files produced
# by that script.
#
# For a list of required column labels, see the variable `required_keys`.
# Additional columns are permitted; their values will be rendered only if the
# column label begins with 'assignment' (e.g., 'assignment_1', 'assignment_2',
# 'assignment_n').
#
# To change the default directories for reading or writing, edit the values of
# `data_dir` or `output_dir`, respectively.

import os
import csv
import re

data_dir = '../temp/'
output_dir = data_dir
required_keys = ['week', 'date', 'breaks', 'unit', 'assignment_0']

def get_valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        prompt = "Invalid selection. Try again. "

def get_filename(data_dir):
    if not os.path.exists(data_dir):
        print(f'Default source directory {data_dir} not found. If your `csv`-formatted schedules are in another location, update the `data_dir` variable.')
        exit()
    else:
        csvfiles = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and re.search('.csv$', f)]
        if len(csvfiles) == 0:
            print('No `csv` file found. Aborting.')
            exit()
        elif len(csvfiles) == 1:
            prompt = f'Found 1 `csv` file, {csvfiles[0]}. Use this one? (Y/n): '
            options = ['y', 'n', '']
            choice = get_valid_input(prompt, options)
            if choice == 'n':
                print('No file selected. Aborting.')
                exit()
            else:
                choice = csvfiles[0]
                print(f'Selected `{choice}`')
                return choice
        else:
            print(f'Found {str(len(csvfiles))} `csv` files:')
            for idx in range(len(csvfiles)):
                print(f'\t({str(idx +1)}) {csvfiles[idx]}')
            print(f'\t({len(csvfiles) + 1}) Select none (exit)')
            prompt = 'Enter a number from the options above: '
            options = []
            for idx in range(len(csvfiles)):
                options.append(str(idx + 1))
            options.append(str(len(csvfiles) + 1))
            choice = get_valid_input(prompt, options)
            if choice == str(len(csvfiles) + 1):
                print('No file selected. Aborting.')
                exit()
            else:
                for idx in range(len(csvfiles)):
                    if int(choice) == idx + 1:
                        choice = csvfiles[idx]
                        print(f'Selected `{choice}`')
                        return choice

def load_csv_to_list_of_dicts(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(dict(row))
    return data

def validate_csv_labels(data):
    data_keys = list(data[0].keys())
    valid = True
    for key in data_keys:
        if key not in required_keys:
            if not re.search('^assignment', key):
                print(f'Warning: values in column {key} will be ignored. Continuing.')
    for key in required_keys:
        if key not in data_keys:
            valid = False
            break
    if not valid:
        print('\nColumn labels do not match requirements. Aborting.')
        print(f'Required column labels: {", ".join(required_keys)}.')
        exit()

def get_assignment_labels(data):
    assignment_labels = []
    keys = list(data[0].keys())
    for key in keys:
        if 'assignment' in key and key != 'assignment_0':
            assignment_labels.append(key)
    return assignment_labels

def format_schedule(data, assignments):
    md_partials = []
    previous_unit = ''
    for item in data:
        if item['unit'] != previous_unit and item['unit'] != '':
            string = '\n# ' + item['unit'] + ' {.unnumbered}'
            md_partials.append(string)
            previous_unit = item['unit']
        string = '\n## ' + item['date'] + ' {.unlisted .unnumbered}\n'
        md_partials.append(string)
        if item['breaks'] != '':
            string = '- **' + item['breaks'] + '**. Class does not meet.'
            md_partials.append(string)
        if item['assignment_0'] != '':
            string = '- **' + item['assignment_0'] + '**'
            md_partials.append(string)
        for assignment in assignments:
            if item[assignment] != '':
                string = '- ' + item[assignment]
                md_partials.append(string)
    return md_partials

def preview_formatted_schedule(partials):
    print('Here is a preview of the `markdown`-formatted schedule:')
    if len(partials) > 10:
        for n in range(5):
            print(partials[n])
        for n in range(3):
            print('...')
        for n in range(-5, 0):
            print(partials[n])
    else:
        for n in range(len(partials)):
            print(partials[n])

def write_to_file(partials, source_file):
    basename = re.sub('.csv', '', source_file)
    output_filename = basename + '.md'
    output_path = os.path.join(output_dir, output_filename)
    prompt = f'\nWrite this schedule to `{output_path}`? (y/N): '
    options = ['y', 'n', '']
    decision = get_valid_input(prompt, options)

    if decision == 'y':
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
            print(f'Created a new directory `{output_dir}`.')
        with open(output_path, 'w') as file:
            for line in range(len(partials)):
                file.write(partials[line] + '\n')
        print(f'Wrote {str(len(partials))} lines to {output_path}.')

def main():
    source_file = get_filename(data_dir)
    source_path = os.path.join(data_dir, source_file)
    data = load_csv_to_list_of_dicts(source_path)
    validate_csv_labels(data)
    assignments = get_assignment_labels(data)
    formatted_schedule_parts = format_schedule(data, assignments)
    preview_formatted_schedule(formatted_schedule_parts)
    write_to_file(formatted_schedule_parts, source_file)
    print('Goodbye.')

main()
