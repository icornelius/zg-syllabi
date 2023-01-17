This repository builds course materials using the [ZettelGeist](https://zettelgeist.org/) publication workflow.
Scripts are adapted from George K. Thiruvathukal's [working example](https://github.com/ZettelGeist/zg-tutorial/tree/master/a-working-example).

The repository contains component parts and assembly scripts to build syllabi and assignments for courses taught at Loyola University Chicago in fall 2022 and spring 2023.
It also hosts the following generated pdf files:

- "English Poetry from Manuscript to Print" (ENGL 390)
  [syllabus](https://icornelius.github.io/zg-syllabi/files/engl390-2022-fall.pdf)
  and [assignment package](https://icornelius.github.io/zg-syllabi/files/engl390-2022-fall-assignments.pdf)
- "History of the English Language" (ENGL 300)
  [syllabus](https://icornelius.github.io/zg-syllabi/files/engl300-2023-spring.pdf)
- "Interpreting Literature" (UCLR 100)
  [syllabus](https://icornelius.github.io/zg-syllabi/files/uclr100-2023-spring.pdf)

To view and browse the plain-text components of these documents, clone this repository.
Then, assuming you have [installed ZettelGeist](https://github.com/ZettelGeist/zettelgeist/wiki/Installing-the-Tools), and activated the Python virtual environment, do the following:

```shell
$ cd path/to/zg-syllabi/zetteln
$ zimport --database index.db --create --fullpath --dir .
$ zfind --database index.db --get-all-tags | less
```

To view metadata for documents with a given tag, run (e.g.)

```shell
$ zfind --database index.db --query-string 'tags:"translation"' --show-all
```

To view the document payloads, add the option `--show-document` to the above command, or open or view the files themselves (filenames are included among the metadata printed by `--show-all`).

For more on queries, see the ZettelGeist [manual](https://github.com/ZettelGeist/zettelgeist/wiki/Manual#zfind).
