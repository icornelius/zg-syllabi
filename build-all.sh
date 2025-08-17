#!/bin/bash

COURSES=("engl320-2025-fall" "engl299-2025-fall")

# Convert CSV schedules to Markdown
pushd schedules

for f in *md ; do chmod 666 $f ; done # unlock Markdown files

echo "Converting CSV-formatted schedules to Markdown..."

for COURSE in ${COURSES[@]} ; do
	python3 ../scripts/date-formatter.py $COURSE.csv
done

for f in *md ; do chmod 444 $f ; done # lock Markdown files

popd

# Call build-pdf.sh to build the PDF(s)
bash build-pdf.sh

echo "Done"
