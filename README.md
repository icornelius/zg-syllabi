# Overview

This repository holds the source of course syllabi taught by Ian Cornelius in the [Department of English at Loyola University Chicago](https://www.luc.edu/english/), which are released as PDFs.

A syllabus is not written as a single document.
It is assembled at build time from a *frame*, which supplies the outline, and files of reusable text held in `partials/`, `schedules/`, and `bibliographies/`.
Policies, assignment instructions, and rubrics are therefore written once and shared by any number of courses.

## Published syllabi

For current syllabi see the [latest tagged release](https://github.com/icornelius/zg-syllabi/releases/latest).

Some past syllabi may be downloaded at the following links:

- "Introduction to Literature"
  [fall 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.2024f.3/uclr100-2024-fall.pdf)
- "Introduction to Poetry"
  [spring 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.engl321.0.3/engl271-2024-spring.pdf)
- "Research Writing: Open Source Tools and Techniques"
  [fall 2025](https://github.com/icornelius/zg-syllabi/releases/download/v2025.08.1/engl299-2025-fall.pdf)
- "History of the English Language"
  [spring 2023](https://github.com/icornelius/zg-syllabi/releases/download/uclr100-v.2023.0.3/engl300-2023-spring.pdf),
  [spring 2025](https://github.com/icornelius/zg-syllabi/releases/download/v2025.01.4/engl300-2025-spring.pdf)
- "Medieval British Literature" (Survey)
  [fall 2025](https://github.com/icornelius/zg-syllabi/releases/download/v2025.08.1/engl320-2025-fall.pdf)
- "Introduction to Old English"
  [spring 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.engl321.0.3/engl441-2024-spring.pdf)
- "Introduction to Middle English"
  [fall 2024](https://github.com/icornelius/zg-syllabi/releases/download/v.2024f.3/engl323-2024-fall.pdf)
- "English Poetry from Manuscript to Print" (Senior Seminar)
  [fall 2022](https://github.com/icornelius/zg-syllabi/releases/download/uclr100-v.2023.0.3/engl390-2022-fall.pdf)
- "Textual Criticism" (Graduate)
  [spring 2026](https://github.com/icornelius/zg-syllabi/releases/download/v2026.01.2-1/cornelius-engl413-2026-01.pdf)

# Where the text lives

## `frames`

Markdown files, one per syllabus.
A frame is an outline, not a text.
It carries the title block, the section headings, and any passage written for that course alone, and it pulls in shared text from `partials/` and `schedules/` at build time, using the Lua filter `include-files.lua`:

````
## Attendance
``` {.include}
partials/policies-0000-20220818144137.md
```
````

Several files may be listed in one block; they are included in the order given.

The frame's YAML block carries the title, subtitle, and the path to the course bibliography.
Together with `config/pandoc-metadata.yaml`, it is the only metadata that reaches the PDF; the YAML of an included file is discarded.

Two consequences follow, and both matter when editing an included file:

Headings in an included file start at `#` and are demoted to fit beneath the frame's own headings, because `config/pandoc-metadata.yaml` sets `include-auto`.
Under a frame's `##`, a partial's `#` becomes `###`.
Write each partial as though it began at the top level, and let the build place it.

An included file may itself include others, and the filter resolves those paths against the directory of the file doing the including, not the working directory.
Partials in the `frame` category use this: they supply the outline of a multi-part assignment and pull in its sections by bare filename, since those sit in `partials/` alongside them.

## `partials`

This directory houses all syllabus content except course schedules and bibliographic details.

Filenames follow the pattern `category-NNNN-YYYYMMDDHHMMSS.md`: a category (`assignments`, `assessment`, `policies`, `course_desc`, `course_id`, `outcome`, `schedule`, `texts`, `misc`, `frame`), a serial number within that category, and the timestamp at which the file was created.
A filename is a permanent address, not a description.
Revise a partial freely, but do not rename it or turn it into a different document: frames refer to partials by name, and a partial included by an archived frame must keep saying what that syllabus said.
Where the text of an old syllabus should stand and a new course needs something different, create a new partial with the next serial number and leave the old one alone.

Each partial carries a YAML block, which the build discards.
`title` and `tags` are expected in every file; `summary`, `comment`, `dates`, `url`, and `bibkey` are used where they apply.
This metadata identifies the document to whoever maintains it and makes it findable; it is not addressed to a student.
Anything a student needs to know belongs in the body of the partial.

Tag generously and reuse tags that are already in use, since tags are the means of finding a partial again.
`zfind --get-all-tags` prints the tags in use; see below.

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

The index (`index.db`) is a local artifact and is not tracked; rebuild it after editing partials.

## `schedules`

Course schedules, one per course and semester.

The CSV is the source.
`build.sh` regenerates the corresponding Markdown from it on every build, by calling `scripts/date-formatter.py`, so the Markdown is not tracked and must not be edited by hand: the next build overwrites whatever is there.
Edits belong in the CSV.

The exception is `engl413-2026-01.md`, which predates this workflow and has no CSV.
That file is source, is maintained by hand, and is tracked; `.gitignore` exempts it by name.
A course with no CSV is built from its Markdown as committed.

## `bibliographies`

Bibliographical details for use by Pandoc's `citeproc`, as CSL YAML exported from Zotero, one file per course.
A frame names its bibliography in the frame's YAML block, and the text cites entries by their `id`, e.g. `@BarberEnglishLanguageHistorical2025`.
Several frames close with a `nocite: @*` block, so that the printed bibliography lists every entry in the file, not only those cited.

# Editing the text

Write one sentence per line, so that a reworded sentence shows as a one-line change.

Keep the source ASCII, so far as the language allows.
Write `--` for an en dash and `---` for an em dash, and use straight quotation marks; Pandoc renders all of these.
The rule governs punctuation Pandoc can generate from ASCII, not spelling: an accented loanword, or an Old English word written with `æ`, keeps its character.
Set terminal commas and periods inside the closing quotation mark, per the American convention; colons and semicolons stay outside.

The schedule CSVs are the exception, since they are edited in a spreadsheet: they carry typographic quotation marks directly, and `--` for the en dashes in line and page ranges.

Prefer linking a university page to restating it, so that the syllabus does not go stale when the policy changes.

Text written for a single course belongs in that course's frame.
Text that another course could use belongs in a partial.

# Production tools

## `scripts`

Python scripts (3.12) to generate skeleton course schedules as CSV and transform the CSV into well-structured Markdown.
Neither script has dependencies beyond the standard library.
See the docstring at the head of each file for usage and for the constants that control input and output paths.

`date-calculator.py` is run once at the start of a semester.
It prompts for the meeting pattern, the first meeting, and the length of the semester, and writes a CSV of meeting dates with empty columns for units and assignments.
It does not know about holidays; record those in the `breaks` column afterwards.

`date-formatter.py` is run by `build.sh` on every build.
It reads the filled-in CSV and writes the corresponding Markdown.
Columns whose label begins with `assignment` are rendered as list items, in the order the columns appear, so a schedule may carry as many assignment columns as it needs.

## `config`

Files used by `pandoc` to control conversion and formatting.
`pandoc-metadata.yaml` holds the settings passed on every build with `--metadata-file`, and `chicago-in-text-shortened-author-title.csl` is the citation style it names.
`latex-header-includes.yaml` is not referenced by the current build.

Not to be confused with `.config/tl_packages`, which is the list of TeX Live packages the GitHub Action installs.
A package the document comes to require must be added there, or the build will pass locally and fail in CI.

# Building

`build.sh` is the build.
Run it from the root of the repository.
For each course it regenerates the Markdown schedule from the CSV and then writes a PDF to `build/`, named `cornelius-COURSE-SEMESTER.pdf`.
The contents of `build/` are for local testing and are not tracked.

The GitHub Action runs this same script, so a local build and a released PDF come from the same source.

The script opens with a `COURSES` array and a `SEMESTER` string, which name the syllabi to be built and are updated at the start of each semester.
The names locate `frames/COURSE.md` and `schedules/COURSE-SEMESTER.csv`, so a course added to the array must have a frame, and a schedule named to match.
Where there is no CSV, the build reports as much and uses the Markdown schedule as committed.

The build needs:

- Pandoc, pinned in the workflow to the version the build is tested against locally (currently 3.10.1)
- LuaLaTeX from TeX Live 2025 or later, required by the PDF/UA-2 tagging the build requests with `-V pdfstandard=ua-2`
- Python 3, for `date-formatter.py`, which uses nothing beyond the standard library
- the Lua filter `include-files.lua`, resolved from either the working directory or Pandoc's user data directory (`~/.local/share/pandoc/filters/`)

The filter is part of the [pandoc/lua-filters](https://github.com/pandoc/lua-filters) collection and is not tracked in this repository; the workflow downloads it at build time.

# Releasing

Work for a semester is done on a dev branch named for the release, e.g. `dev-2026.8`, and merged into `main`.

Deployment is done with GitHub Actions: see `.github/workflows/action.yaml`.
Pushing to `main` builds the PDFs.
Pushing a tag matching `v*` also attaches them to a GitHub release.

Before tagging, run `build.sh` locally and read the PDFs.
Nothing the build generates needs to be committed: the Action regenerates the schedules from the CSV as part of the same script.

Record the release in CHANGELOG.md.
The changelog covers the syllabi only, so commits typed `build`, `ci`, `chore`, and `docs` do not appear in it, and a semester's initial release is entered as such, without an account of how it differs from the semester before.

## Versioning

Beginning with `v2026-08.1`, tagged releases have the following semantics: YEAR-MONTH.VERSION.
The MONTH is the two-digit month in which a given semester begins (usually 01 or 08).
The VERSION counter restarts at 1 each semester.

Earlier tags use a dot in place of the hyphen, and their counter begins at 0.
For the releases themselves see CHANGELOG.md.

# Commit conventions

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), in the form `type(scope): description`.

The product of this repository is a set of syllabi, and their readers are students.
The prose in `frames/`, `partials/`, and `schedules/` is therefore source, not documentation.
A commit type describes what a change does for a reader of a syllabus; only `docs` refers to documentation of the repository itself.

| Type | Use for |
| --- | --- |
| `feat` | a new partial, section, policy, or assignment |
| `fix` | correcting what is wrong, stale, or broken |
| `refactor` | rewording or reorganizing, meaning unchanged |
| `style` | whitespace, Markdown formatting, typography |
| `build` | `build.sh`, `config/`, Pandoc settings |
| `ci` | the GitHub Action and `.config/tl_packages` |
| `chore` | version bumps, changelog upkeep, repository housekeeping |
| `docs` | `README.md`, `LICENSE`: the repository, not the syllabi |

The specification defines only `feat` and `fix`; the remaining types are local convention and may be revised.
There is no type for removal.
Use `fix` where something is removed as wrong or outdated, and `refactor` where it is removed because it has moved or been superseded.

A scope names the part of the source affected: a course, by its number (`322`, `406`, `413`); a category of partial (`assignments`, `assessment`, `policies`); or a component (`scripts`, `bib`, `csl`, `readme`, `changelog`).

Make one logical change per commit.
Entries in CHANGELOG.md cite the commit that made the change, so a commit mixing several student-facing changes cannot be cited precisely.
Where a change reaches several courses because it edits a shared partial, the scope is the category of partial, not the courses.
