# This Python script generates meeting dates for standard academic course
# schedules. The user is prompted for the meeting pattern (supported options
# are MWF, TuTh, WM, and once-per-week), date of the first meeting, and length
# of the semester. The script is not aware of academic or religious holidays,
# but it handles irregular starts (e.g., a MWF class that meets WF in the first
# week). To simplify input, the script will try to guess the year and month in
# which to begin the sequence. (This guess is based on the current date.)
#
# Output is formatted with Markdown headers and previewed in the terminal.
# There is an option to write the output to a file, by default
# `meeting-dates.md` in the current working directory. (To change that path,
# update the value of the `output` variable.)
#
# There are no builtin options for changing the output format. The aim is just
# to generate a structured sequence of dates, for modification and reformatting
# in a text editor.

from datetime import datetime, timedelta
import os

output = 'meeting-dates.md'

def get_valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        prompt = "Invalid selection. Try again. "

def get_valid_start_date(prompt, options):
    if semester_id == 'n':
        while True:
            choice = input(prompt)
            if bool(datetime.strptime(choice, "%Y-%m-%d")):
                choice = datetime.strptime(choice, "%Y-%m-%d")
                if int(datetime.strftime(choice, "%w")) in options:
                    return choice
            prompt = "Invalid format or date. Format should be YYYY-MM-DD.\nDate must be consistent with the selected meeting-pattern. Try again: "
    else:
        while True:
            choice = start_year + "-" + start_month + "-" + input(prompt)
            if bool(datetime.strptime(choice, "%Y-%m-%d")):
                choice = datetime.strptime(choice, "%Y-%m-%d")
                if int(datetime.strftime(choice, "%w")) in options:
                    return choice
            prompt = "Invalid start day. Start day must be consistent with the selected meeting-pattern. Try again: "

def get_mtg_dates(week, date):
    lines = []
    if mtg_pattern == 'TuTh' or mtg_pattern == 'MW':
        while week <= int(semester_length):
            lines.append("# Week " + str(week))
            lines.append("## " + date.strftime("%a %b %d"))
            diff = timedelta(days=2)
            date += diff
            lines.append("## " + date.strftime("%a %b %d"))
            lines.append('')
            diff = timedelta(days=5)
            date += diff
            week += 1
    elif mtg_pattern == 'MWF':
        while week <= int(semester_length):
            lines.append("# Week " + str(week))
            lines.append("## " + date.strftime("%a %b %d"))
            diff = timedelta(days=2)
            for i in range(2):
                date += diff
                lines.append("## " + date.strftime("%a %b %d"))
            lines.append('')
            diff = timedelta(days=3)
            date += diff
            week += 1
    else:
        while week <= int(semester_length):
            lines.append("# Week " + str(week))
            lines.append("## " + date.strftime("%a %b %d"))
            lines.append('')
            diff = timedelta(days=7)
            date += diff
            week += 1
    return lines

print("Welcome!")

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

# Get the start date
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

if semester_id == "y" or len(semester_id) == 0:
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

start_date = get_valid_start_date(prompt, options)

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
if mtg_pattern == 'TuTh' and start_idx != '2':
    regular_start = False
elif mtg_pattern == 'MWF' or mtg_pattern == 'MW':
    if start_idx != '1':
        regular_start = False
else:
    regular_start = True

# Generate meeting dates
if regular_start:
    week = 1
    date = start_date
    schedule = get_mtg_dates(week, date)
else: # create a custom first-week schedule
    schedule = []
    week = 1
    date = start_date
    schedule.append("# Week " + str(week))
    schedule.append("## " + date.strftime("%a %b %d"))
    if mtg_pattern == 'TuTh' or mtg_pattern == 'MW':
        diff = timedelta(days=5)
    else: # WMF beginning W or F
        if start_idx == '3': # MWF beginning W
            diff = timedelta(days=2)
            date += diff
            schedule.append("## " + date.strftime("%a %b %d"))
        diff = timedelta(days=3)
    date += diff
    week += 1
    schedule.append('')
    schedule += get_mtg_dates(week, date)

# Print a preview
pretty_date = start_date.strftime("%A, %d %B, %Y")
print(f"\nPreviewing dates for a class that meets {mtg_pattern} for {semester_length} weeks, beginning {pretty_date}.\n")

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

# Write to a file, if desired
prompt = f'Write this schedule to filename `{output}` in the current directory? (Y/n): '
options = ['y', 'n', '']
decision = get_valid_input(prompt, options)

if decision == 'y' or len(decision) == 0:
    with open(output, 'w') as file:
        for line in range(len(schedule)):
            file.write(schedule[line] + '\n')

print('\nGoodbye')
