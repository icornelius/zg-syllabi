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

# Course introduction: writing systems and speech sounds (week 2)
heading
zfind $COMMON --query-string 'filename:20220830084038' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Exploring Middle English words (week 3)
heading
zfind $COMMON --query-string 'filename:20210822133004' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Translation and commentary (week 4)
heading
zfind $COMMON --query-string 'filename:20200120155517' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Rubric for poetry recitation (week 4)
heading
zfind $COMMON --query-string 'filename:20200116101507' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Introduction to medieval handwritten books (week 5)
heading
zfind $COMMON --query-string 'filename:20221104173823' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Manuscripts and/of Chaucer's poetry (week 6)
heading
zfind $COMMON --query-string 'filename:20221104174814' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Alisoun of Bath: sources, texts, glosses (week 7)
heading
zfind $COMMON --query-string 'filename:20221003204226' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Midterm essay (week 8)
heading
zfind $COMMON --query-string 'filename:20221007183937' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Introduction to early printed books (week 9)
heading
zfind $COMMON --query-string 'filename:20210922000000' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Encountering *Hamlet* (week 10)
heading
zfind $COMMON --query-string 'filename:20221101101723' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# The second quarto *Hamlet* (week 11)
heading
zfind $COMMON --query-string 'filename:20221105181640' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Three texts of *Hamlet* (week 12)
heading
zfind $COMMON --query-string 'filename:20221104205657' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Annotated bibliography and presentation (week 13)
heading
zfind $COMMON --query-string 'filename:20211110000000' $PUBLISH  | pandoc_shift_headings
echo "\newpage"
echo

# Final essay (week 15)
heading
echo

## Instructions
heading
zfind $COMMON --query-string 'filename:20180321000000' $PUBLISH  | pandoc_shift_headings
echo

## Prompts
heading
zfind $COMMON --query-string 'filename:20221104214813' $PUBLISH  | pandoc_shift_headings
echo

