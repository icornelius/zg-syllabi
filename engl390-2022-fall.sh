#!/bin/bash

[ -f config/book-functions.sh ] && source config/book-functions.sh

PUBLISH="--publish config/publishing-template.md --publish-conf config/publishing-options.json"

cat << PANDOC_FRONTMATTER
---
title: Advanced seminar
subtitle: English poetry from manuscript to print
author:
- Ian Cornelius
- Loyola University Chicago
date: Fall 2022
version: 0
geometry: margin=1in
fontsize: 12pt
colorlinks: true
toc: true
csl: ../config/chicago-cv.csl
bibliography: ../bibliographies/engl390-2022-fall.yaml
suppress-bibliography: true
---
PANDOC_FRONTMATTER

echo "\newpage"
echo

# Registrar information
heading

## Course information
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"meeting time" & tags:390 & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
echo

## Contact information
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"contact info" & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
echo

# Course description and objectives
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"course description" & tags:390 & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
echo

# Texts
heading
zfind $COMMON --query-string 'tags:syllabus & tags:textbooks & tags:390 & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
echo

# Schedule
heading
zfind $COMMON --query-string 'tags:syllabus & tags:schedule & tags:390 & tags:"fall 2022"' $PUBLISH  | pandoc_shift_headings
echo

# Assignments
heading

## Exams
heading
echo "There are no exams in this course."
echo

## Formal writing
heading

### General instructions
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"writing intensive" & tags:"document specifications"' $PUBLISH  | pandoc_shift_headings
echo

### Essays
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"midterm essay" & tags:390 & tags:fall' $PUBLISH  | pandoc_shift_headings
echo

### Other formal writing
heading

#### Translation and critical commentary
heading
zfind $COMMON --query-string 'tags:syllabus & tags:translation & tags:Chaucer' $PUBLISH  | pandoc_shift_headings
echo

#### Response papers
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"response papers" & tags:390' $PUBLISH  | pandoc_shift_headings
echo

#### Annotated bibliography
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"annotated bibliography" & tags:390 & tags:"book history"' $PUBLISH  | pandoc_shift_headings
echo

## Oral presentations
heading

### Poetry recitation
heading
zfind $COMMON --query-string 'tags:syllabus & tags:recitation & tags:Chaucer' $PUBLISH  | pandoc_shift_headings
echo

### Peer interview
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"peer interview"' $PUBLISH  | pandoc_shift_headings
echo

### Research presentation
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"research presentation" & tags:fall' $PUBLISH  | pandoc_shift_headings
echo

## Sakai blog
heading
zfind $COMMON --query-string 'tags:syllabus & tags:390 & tags:Sakai' $PUBLISH  | pandoc_shift_headings
echo

# Assessment
heading
#zfind $COMMON --query-string 'tags:syllabus & tags:MD & tags:MLB & tags:"NL East"' $PUBLISH  | pandoc_shift_headings
echo

## Course components and points
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"ENGL 390" & tags:"fall 2022" & tags:weights' $PUBLISH  | pandoc_shift_headings
echo

## Standards for formal writing
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"marking rubric"' $PUBLISH  | pandoc_shift_headings
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

## Communication
heading
zfind $COMMON --query-string 'tags:syllabus & tags:communication' $PUBLISH  | pandoc_shift_headings
echo

## Diversity, inclusion, and equity
heading
zfind $COMMON --query-string 'tags:syllabus & tags:DEI' $PUBLISH  | pandoc_shift_headings
echo

## Alternative editions
heading
zfind $COMMON --query-string 'tags:syllabus & tags:390 & tags:"alternative editions"' $PUBLISH  | pandoc_shift_headings
echo

## Academic integrity
heading
zfind $COMMON --query-string 'tags:syllabus & tags:"academic integrity"' $PUBLISH  | pandoc_shift_headings
echo

## Revisions
heading
zfind $COMMON --query-string 'tags:syllabus & tags:390 & tags:revisions' $PUBLISH  | pandoc_shift_headings
echo

## Late work
heading
zfind $COMMON --query-string 'tags:syllabus & tags:390 & tags:"late work"' $PUBLISH  | pandoc_shift_headings
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
zfind $COMMON --query-string 'tags:syllabus & tags:"ENGL 390" & tags:"fall 2022" & tags:"version information"' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Questionnaire
heading

zfind $COMMON --query-string 'tags:syllabus & tags:390 & tags:questionnaire' $PUBLISH  | pandoc_shift_headings
