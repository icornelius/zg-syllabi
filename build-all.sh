#!/bin/bash

COURSES=("engl320-2025-fall" "engl299-2025-fall")

# Convert CSV schedules to Markdown
pushd schedules

echo "Converting CSV-formatted schedules to Markdown..."

for COURSE in ${COURSES[@]} ; do
	python3 ../scripts/date-formatter.py $COURSE.csv
done

popd

# Unlock Markdown files in the build directory
for f in build/*md ; do chmod 666 $f ; done

# Build a single Markdown file from atomized components
pushd partials

echo "Building composite Markdown from components..."
for COURSE in ${COURSES[@]} ; do
	pandoc --metadata-file ../config/pandoc-metadata.yaml --lua-filter include-files.lua --wrap=preserve ../frames/$COURSE.md -so ../build/$COURSE.md
	echo -e "\tCreated /build/$COURSE.md"
done

popd

# Make Markdown files in build/ read-only
for f in build/*md ; do chmod 444 $f ; done

# Call build-pdf.sh to build the PDF(s)
bash build-pdf.sh

echo "Done"
