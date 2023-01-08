#!/bin/bash

[ -f config/book-functions.sh ] && source config/book-functions.sh

PUBLISH="--publish config/publishing-template.md --publish-conf config/publishing-options.json"

cat << PANDOC_FRONTMATTER
---
title: Interpreting Literature
subtitle: Speaking Out
author: Ian Cornelius
date: Loyola University Chicago, Spring 2023
geometry: margin=1in
fontsize: 12pt
colorlinks: true
link-citations: true
toc: true
csl: ../config/chicago-cv.csl
bibliography: ../bibliographies/engl390-2022-fall.yaml
suppress-bibliography: true
---
PANDOC_FRONTMATTER

echo "\newpage"
echo

# Basic information
heading

## Course details
heading
zfind $COMMON --query-string 'filename:20220929164752' $PUBLISH  | pandoc_shift_headings
echo

## How to contact me
heading
zfind $COMMON --query-string 'filename:20230107090154' $PUBLISH  | pandoc_shift_headings
echo

# Course description and objectives
heading
zfind $COMMON --query-string 'filename:20221001073436' $PUBLISH  | pandoc_shift_headings
echo

# Schedule
heading
#zfind $COMMON --query-string 'tags:syllabus & tags:schedule & tags:390 & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
echo "To be supplied"
echo

# Assessment
heading

## Summary of grade components
heading
zfind $COMMON --query-string 'filename:20230108100027' $PUBLISH  | pandoc_shift_headings
echo

## Description of components
heading

### Participation
heading
echo "See [attendance](#attendance)."
echo

### Class presentation
heading
zfind $COMMON --query-string 'filename:20230108135227' $PUBLISH  | pandoc_shift_headings
echo

### Quizzes
heading
zfind $COMMON --query-string 'filename:20230108134902' $PUBLISH  | pandoc_shift_headings
echo

### Exams
heading
zfind $COMMON --query-string 'filename:20230108134803' $PUBLISH  | pandoc_shift_headings
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
zfind $COMMON --query-string 'filename:20230107092615' $PUBLISH  | pandoc_shift_headings
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
zfind $COMMON --query-string 'tags:syllabus & tags:"academic integrity"' $PUBLISH  | pandoc_shift_headings
echo

### Late work
#heading
#zfind $COMMON --query-string 'filename:20230107104207' $PUBLISH  | pandoc_shift_headings
#echo

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
zfind $COMMON --query-string 'tags:syllabus & tags:"ENGL 390" & tags:"fall 2022" & tags:"version information"' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

## Questionnaire
#heading
#
#zfind $COMMON --query-string 'tags:syllabus & tags:UCLR & tags:questionnaire' $PUBLISH  | pandoc_shift_headings

# Bibliography
heading
