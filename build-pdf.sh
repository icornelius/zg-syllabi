#!/bin/bash

COURSE_1=engl300-2025-spring
#COURSE_2=engl323-2024-fall

echo 'Creating pdf for' $COURSE_1 '...'
pandoc --citeproc --toc --number-sections --metadata-file config/latex-header-includes.yaml build/$COURSE_1.md -o build/$COURSE_1.pdf
#echo 'Creating pdf for' $COURSE_2 '...'
#pandoc --citeproc --toc --number-sections --metadata-file config/latex-header-includes.yaml build/$COURSE_2.md -o build/$COURSE_2.pdf
