#!/bin/bash

COURSES=("engl406" "engl322")
NAME="cornelius"
SEMESTER="2026-08"

for COURSE in ${COURSES[@]} ; do
        echo "Creating /build/$NAME-$COURSE-$SEMESTER.pdf..."
	pandoc --metadata-file config/pandoc-metadata.yaml \
		--lua-filter include-files.lua \
		--citeproc --toc --number-sections \
		-V pdfstandard=ua-2 \
		--pdf-engine lualatex \
                frames/$COURSE.md \
		-o build/$NAME-$COURSE-$SEMESTER.pdf &&
		echo -e "\tSuccess"
done
