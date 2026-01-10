#!/bin/bash

COURSES=("engl413")
NAME="cornelius"
SEMESTER="2026-01"

for COURSE in ${COURSES[@]} ; do
        echo "Creating /build/$NAME-$COURSE-$SEMESTER.pdf..."
	pandoc --metadata-file config/pandoc-metadata.yaml \
		--lua-filter include-files.lua \
		--citeproc --toc --number-sections \
                frames/$COURSE.md \
		-o build/$NAME-$COURSE-$SEMESTER.pdf &&
		echo -e "\tSuccess"
done
