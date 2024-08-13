This repository hosts the published syllabi (as PDF) for some recent courses:

- "Exploring Poetry" (ENGL 271)
  [spring 2024](https://icornelius.github.io/zg-syllabi/files/engl271-2024-spring.pdf)
- "History of the English Language" (ENGL 300)
  [spring 2023](https://icornelius.github.io/zg-syllabi/files/engl300-2023-spring.pdf)
- "Introduction to Old English" (ENGL 321/441)
  spring 2024 [undergraduate](https://icornelius.github.io/zg-syllabi/files/engl321-2024-spring.pdf)
  and [graduate](https://icornelius.github.io/zg-syllabi/files/engl441-2024-spring.pdf)
- "English Poetry from Manuscript to Print" (ENGL 390)
  [fall 2022](https://icornelius.github.io/zg-syllabi/files/engl390-2022-fall.pdf)
- "Interpreting Literature" (UCLR 100)
  [spring 2023](https://icornelius.github.io/zg-syllabi/files/uclr100-2023-spring.pdf)

# Plain text components
Plain text components are maintained in the directories `frames/` and `partials/`.

Files in `frames/` provide document outlines, metadata, and code blocks for loading content.
(See [Build], below.)

Content is loaded from files in `partials/`.
These are queryable with [ZettelGeist](https://zettelgeist.org/).
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

# Misc
- `scripts/date-calculator.py` generates skeleton schedules. See the comment at the head of the file.
- `bibliographies/` contains bibliographical details for use by Pandoc's `citeproc`
- `config/` contains some files that control formatting.
  The Citation Style Language files control the formatting of bibliographical details.
