#!/bin/bash

COURSES=("comp250-engl296")

for COURSE in ${COURSES[@]} ; do
        echo "Creating /build/$COURSE.pdf..."
	pandoc \
	        --metadata-file config/pandoc-metadata.yaml \
		--lua-filter include-files.lua \
		--citeproc --toc --number-sections \
                frames/$COURSE.md \
		-o build/$COURSE.pdf &&
		echo -e "\tSuccess"
done
