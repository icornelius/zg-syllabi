This repository hosts the published syllabi (as PDF) for some recent courses:

- "Exploring Poetry" (ENGL 271)
  [spring 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.engl321.0.3/engl271-2024-spring.pdf)
- "History of the English Language" (ENGL 300)
  [spring 2023](https://github.com/icornelius/zg-syllabi/releases/download/uclr100-v.2023.0.3/engl300-2023-spring.pdf)
- "Introduction to Old English" (ENGL 321/441)
  [spring 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.engl321.0.3/engl441-2024-spring.pdf)
- "Studies in Medieval Literature" (ENGL 323)
  [fall 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.2024f.3/engl323-2024-fall.pdf)
- "English Poetry from Manuscript to Print" (ENGL 390)
  [fall 2022](https://github.com/icornelius/zg-syllabi/releases/download/uclr100-v.2023.0.3/engl390-2022-fall.pdf)
- "Interpreting Literature" (UCLR 100)
  [fall 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.2024f.3/uclr100-2024-fall.pdf)

# Plain text components
Plain text components are maintained in the directories `frames`, `schedules`, and `partials`.

## `frames`
Markdown files (one per course).
These supply document outlines and code blocks for loading content.
(See [Build], below.)

## `schedules`
Course schedules as `csv` and `markdown`.
The `markdown` files are created from the corresponding `csv` by script.
(See [scripts].)

## `partials`
This directory houses all syllabus content except course schedules.
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
(ZettelGeist queries have some known bugs, described in [this issue](https://github.com/ZettelGeist/zettelgeist/issues/38)).

# Builds
Syllabi are built with [Pandoc](https://pandoc.org/) and LaTeX.
This is done in two steps.

First, atomized components are gathered into a single Markdown file, using the lua filter [`include-files`](https://github.com/pandoc/lua-filters/tree/master/include-files).
This operation is done with `build-markdown.sh`, which should be run locally.
The resulting Markdown file is read-only: editing should be done in the atomized source components.

Second, the read-only Markdown file is converted to PDF.
This is done with `build-pdf.sh`, which may be run locally for testing purposes.
Deployment is done with GitHub Actions (see `.github/workflows/action.yaml`).

The reason for the two-step build is transparency:
the intermediate Markdown file provides a single plain-text document with clear version history.

# Other repository contents
## `scripts`
Python scripts to generate skeleton schedules as `csv` and transform the `csv` into well-structured `markdown`.
See comments at the head of the files.

## `bibliographies`
Bibliographical details for use by Pandoc's `citeproc`.

## `config`
Configuration files for document conversion and formatting, including formatting of bibliographical references.
