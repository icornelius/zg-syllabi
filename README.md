# Published syllabi

For current syllabi see the [latest tagged release](https://github.com/icornelius/zg-syllabi/releases/latest).

Final versions of some past syllabi may be downloaded at the following links:

- "Exploring Poetry" (ENGL 271)
  [spring 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.engl321.0.3/engl271-2024-spring.pdf)
- "History of the English Language" (ENGL 300)
  [spring 2023](https://github.com/icornelius/zg-syllabi/releases/download/uclr100-v.2023.0.3/engl300-2023-spring.pdf),
  [spring 2025](https://github.com/icornelius/zg-syllabi/releases/download/v2025.01.4/engl300-2025-spring.pdf)
- "Introduction to Old English" (ENGL 321/441)
  [spring 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.engl321.0.3/engl441-2024-spring.pdf)
- "Studies in Medieval Literature" (ENGL 323)
  [fall 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.2024f.3/engl323-2024-fall.pdf)
- "English Poetry from Manuscript to Print" (ENGL 390)
  [fall 2022](https://github.com/icornelius/zg-syllabi/releases/download/uclr100-v.2023.0.3/engl390-2022-fall.pdf)
- "Interpreting Literature" (UCLR 100)
  [fall 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.2024f.3/uclr100-2024-fall.pdf)

# Versioning

Beginning with `v2025.01.0`, tagged releases have the following semantics: YEAR.MONTH.VERSION.
The MONTH is the two-digit month in which a given semester begins (usually 01 or 08).

# Plain text components

Plain text components are maintained in the directories `frames`, `schedules`, `bibliographies`, and `partials`.

## `frames`

Markdown files (one per course).
These supply document outlines and code blocks for loading content.

## `schedules`

Course schedules as CSV and Markdown.
The Markdown files are created by script from the corresponding CSV and should not be edited manually.
See [scripts](#scripts).

## `bibliographies`

Bibliographical details for use by Pandoc's `citeproc`.

## `partials`

This directory houses all syllabus content except course schedules and bibliographic details.
Files are queryable with [ZettelGeist](https://zettelgeist.org/).
To do that, clone the repository.
Then, assuming you have [installed ZettelGeist](https://github.com/ZettelGeist/zettelgeist/wiki/Installing-the-Tools), and activated the Python virtual environment, do the following:

```shell
$ cd path/to/zg-syllabi/partials
$ zimport --database index.db --create --fullpath --dir .
$ zfind --database index.db --get-all-tags | less
```

To view metadata for documents with a given tag, run (e.g.)

```shell
$ zfind --database index.db --query-string 'tags:presentation' --show-all
```

To view the document payloads, add the option `--show-document` to the above command, or open or view the files themselves.
Filenames are included among the metadata printed by `--show-all`.

For more on queries, see the ZettelGeist [manual](https://github.com/ZettelGeist/zettelgeist/wiki/Manual#zfind).
(ZettelGeist queries have some [known issues](https://github.com/ZettelGeist/zettelgeist/issues/38)).

# Production tools

Production tools are maintained in the directories `scripts` and `config`.

## `scripts`

The directory `scripts` contains Python scripts to generate skeleton course schedules as CSV and transform the CSV into well-structured Markdown.
See comments at the head of the files.

## `config`

The directory `config` contains files used by `pandoc` to control the conversion and formatting of documents, including the formatting of bibliographical references.

# Builds and deployment

For local builds, and prior to each release, run the shell script `build-all.sh`.
This script calls a Python script (`scripts/date-formatter.py`) to create Markdown files in `schedules` and calls another shell script (`build-pdf.sh`) to create PDFs in `build`.
The Markdown files created in `schedules` must be committed to the repository and pushed to origin prior to deployment.
(This may be obviated in a future release.)
The PDF files created in `build` are for local testing.
(They are ignored by `git`.)
Deployment is done with GitHub Actions: see `.github/workflows/action.yaml`.
