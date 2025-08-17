#!/bin/bash

COURSES=("engl320-2025-fall" "engl299-2025-fall")

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
