#!/bin/bash

[ -f config/book-functions.sh ] && source config/book-functions.sh

PUBLISH="--publish config/publishing-template.md --publish-conf config/publishing-options.json"

cat << PANDOC_FRONTMATTER
---
title: History of the English Language
author: Ian Cornelius
date: Spring 2023
geometry: margin=1in
fontsize: 12pt
colorlinks: true
toc: # true
csl: ../config/chicago-cv.csl
bibliography: ../bibliographies/engl390-2022-fall.yaml
suppress-bibliography: true
---
PANDOC_FRONTMATTER

#echo "\newpage"
#echo

# Registrar information
heading

### Course information
#heading
zfind $COMMON --query-string 'filename:20220929164952' $PUBLISH  | pandoc_shift_headings
echo

### Contact information
#heading
#zfind $COMMON --query-string 'tags:syllabus & tags:"contact info" & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
#echo

# Course description and objectives
heading
zfind $COMMON --query-string 'filename:20220306084855' $PUBLISH  | pandoc_shift_headings
echo
