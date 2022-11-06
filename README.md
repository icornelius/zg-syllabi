This repository builds course materials using the [ZettelGeist](https://zettelgeist.org/) publication workflow.
Scripts are adapted from George K. Thiruvathukal's [working example](https://github.com/ZettelGeist/zg-tutorial/tree/master/a-working-example).

Currently the repository contains the components parts and assembly scripts to build the syllabus and assignments for ENGL 390 "English Poetry from Manuscript to Print" (fall 2022).
This GitHub repository also hosts the generated pdf files:

- ENGL 390, fall 2022 [syllabus](https://icornelius.github.io/zg-syllabi/files/engl390-2022-fall.pdf)
- ENGL 390, fall 2022 [assignment package](https://icornelius.github.io/zg-syllabi/files/engl390-2022-fall-assignments.pdf)

To view and browse the plain-text components of these documents, clone this repository.
Then, assuming you have [installed ZettelGeist](https://github.com/ZettelGeist/zettelgeist/wiki/Installing-the-Tools), and activated the Python virtual environment, do the following:

```shell
$ cd path/to/zg-syllabi/zetteln
$ zimport --database index.db --create --fullpath --dir .
$ zfind --database index.db --get-all-tags | less
```

Then, to view metadata for documents with a given tag, run (e.g.)

```shell
$ zfind --database index.db --query-string 'tags:"translation"' --show-all
```

To view the document payloads, add the option `--show-document` to the above command, or open or view the files themselves (filenames are includes among the metadata printed by `--show-all`).

For more on queries, see the ZettelGeist [manual](https://github.com/ZettelGeist/zettelgeist/wiki/Manual#zfind).
