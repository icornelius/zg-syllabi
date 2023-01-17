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
link-citations: true
toc: true
csl: ../config/chicago-numerical.csl
bibliography: ../bibliographies/engl-300.yaml
suppress-bibliography: # true
---
PANDOC_FRONTMATTER

echo "\newpage"
echo

# Basic information
heading

## Course details
heading
zfind $COMMON --query-string 'filename:20220929164952' $PUBLISH  | pandoc_shift_headings
echo

## How to contact me
heading
zfind $COMMON --query-string 'filename:20230107090154' $PUBLISH  | pandoc_shift_headings
echo

# Course description and objectives
heading
zfind $COMMON --query-string 'filename:20220306084855' $PUBLISH  | pandoc_shift_headings
echo

# Schedule
heading
zfind $COMMON --query-string 'filename:20221201113335' $PUBLISH  | pandoc_shift_headings
echo

# Assessment
heading

## Summary of grade components
heading
zfind $COMMON --query-string 'filename:20230116175142' $PUBLISH  | pandoc_shift_headings
echo

## Description of components
heading

### Participation
heading
echo "See [attendance](#attendance). Informal assignments also count towards this component."
echo

### Writing
heading
zfind $COMMON --query-string 'filename:20230116204430' $PUBLISH  | pandoc_shift_headings
echo

### Class presentation
heading
zfind $COMMON --query-string 'filename:20230116223912' $PUBLISH  | pandoc_shift_headings
echo

### Exams
heading
echo "There are no exams in this course."
echo

## Grade schema
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"quintile system"' $PUBLISH  | pandoc_shift_headings
echo

# Policies
heading

## Attendance
heading
zfind $COMMON --query-string 'tags:syllabus & tags:attendance' $PUBLISH  | pandoc_shift_headings
echo

## Texts
heading
zfind $COMMON --query-string 'filename:20230111135113' $PUBLISH  | pandoc_shift_headings
echo

## Communication
heading
zfind $COMMON --query-string 'tags:syllabus & tags:communication' $PUBLISH  | pandoc_shift_headings
echo

## Diversity, inclusion, and equity
heading
zfind $COMMON --query-string 'tags:syllabus & tags:DEI' $PUBLISH  | pandoc_shift_headings
echo

## Academic integrity
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"integrity"' $PUBLISH  | pandoc_shift_headings
echo

## Late work
heading
zfind $COMMON --query-string 'filename:20230107104207' $PUBLISH  | pandoc_shift_headings
echo

## Extra credit
heading
zfind $COMMON --query-string 'filename:20221105180224' $PUBLISH  | pandoc_shift_headings
echo

## Accommodations and assistance
heading
zfind $COMMON --query-string 'tags:syllabus & tags:SAC' $PUBLISH  | pandoc_shift_headings
echo

## Privacy
heading
zfind $COMMON --query-string 'tags:syllabus & tags:privacy & tags:"no recordings"' $PUBLISH  | pandoc_shift_headings
echo

## Public health
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"public health" & tags:"masks optional"' $PUBLISH  | pandoc_shift_headings
echo

## Statement of intent
heading

cat << TEXT
By remaining in this course, students agree to accept this syllabus and abide by its policies.
Students will be informed of any changes to the syllabus.
TEXT
echo

# Version information
heading
zfind $COMMON --query-string 'filename:20220818164402' $PUBLISH  | pandoc_shift_headings
echo

# Questionnaire
heading
zfind $COMMON --query-string 'filename:20220818142112' $PUBLISH  | pandoc_shift_headings
echo

# Bibliography
heading
