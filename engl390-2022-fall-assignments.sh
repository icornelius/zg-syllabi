#!/bin/bash

[ -f config/book-functions.sh ] && source config/book-functions.sh

PUBLISH="--publish config/publishing-template.md --publish-conf config/publishing-options.json"

cat << PANDOC_FRONTMATTER
---
title: Assignment instructions for ENGL 390
subtitle: English poetry from manuscript to print
author: Ian Cornelius
date: Fall 2022
geometry: margin=1in
fontsize: 12pt
colorlinks: true
toc: true
csl: ../../styles/chicago-fullnote-bibliography.csl
bibliography: ../bibliographies/engl390-2022-fall.yaml
suppress-bibliography: true
---
PANDOC_FRONTMATTER

echo "\newpage"
echo

# Writing systems and speech sounds
heading
echo "**Prompts for 09-06.**"
zfind $COMMON --query-string 'tags:"ENGL 390" & tags:"fall 2022" & tags:prompt & tags:week1' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Exploring Middle English words
heading
echo "**Prompt for 09-13.**"
zfind $COMMON --query-string 'tags:"test"' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Translation and commentary
heading
zfind $COMMON --query-string 'tags:"ENGL 390" & tags:"fall 2022" & tags:prompt & tags:translation' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Rubric for poetry recitation
heading
zfind $COMMON --query-string 'tags:rubric & tags:"poetry recitation" & tags:Chaucer' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo
