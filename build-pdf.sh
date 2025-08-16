#!/bin/bash

COURSES=("engl320-2025-fall" "engl299-2025-fall")

for COURSE in ${COURSES[@]} ; do
        echo "Creating /build/$COURSE.pdf..."
	pandoc --citeproc --toc --number-sections --metadata-file config/latex-header-includes.yaml build/$COURSE.md -o build/$COURSE.pdf
	echo -e "\tSuccess"
done
