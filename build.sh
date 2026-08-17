#!/bin/bash

# Build the syllabi named in COURSES: regenerate each Markdown schedule from
# its CSV, then write one PDF per course to `build`.
#
# The GitHub Action runs this same script, so a local build and a released PDF
# come from the same source. Update COURSES and SEMESTER at the start of each
# semester. A course is built from `frames/$COURSE.md` and, where one exists,
# `schedules/$COURSE-$SEMESTER.csv`.

set -euo pipefail

COURSES=("engl406" "engl322")
NAME="cornelius"
SEMESTER="2026-08"

mkdir -p build

for COURSE in "${COURSES[@]}" ; do
	SCHEDULE="schedules/$COURSE-$SEMESTER.csv"

	if [ -f "$SCHEDULE" ] ; then
		echo "Converting $SCHEDULE to Markdown..."
		python3 scripts/date-formatter.py "$SCHEDULE"
	else
		# Courses predating the CSV workflow keep a Markdown schedule
		# under version control. See README.md.
		echo "No CSV schedule for $COURSE; using the Markdown as committed"
	fi

	echo "Creating build/$NAME-$COURSE-$SEMESTER.pdf..."
	pandoc --metadata-file config/pandoc-metadata.yaml \
		--lua-filter include-files.lua \
		--citeproc --toc --number-sections \
		-V pdfstandard=ua-2 \
		--pdf-engine lualatex \
		"frames/$COURSE.md" \
		-o "build/$NAME-$COURSE-$SEMESTER.pdf"
	echo -e "\tSuccess"
done

echo "Done"
