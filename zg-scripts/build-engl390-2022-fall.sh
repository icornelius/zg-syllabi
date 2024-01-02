#!/bin/bash

NAME=engl390-2022-fall
CONFIG=config
ZETTELS=zetteln

[ -f ~/zenv/bin/activate ] && source ~/zenv/bin/activate

[ -f ${CONFIG}/book-functions.sh ] && source ${CONFIG}/book-functions.sh

mkdir -p ${BUILD}

zimport --create --database ${DB_PATH} --dir ${ZETTELS}  --fullpath

bash ${NAME}.sh | tee ${BUILD}/${NAME}-preview.md

pushd ${BUILD}

if [ ! -e build-log-${NAME}.txt ] ; then
	touch build-log-${NAME}.txt
fi

echo "wc on `date`" >> build-log-${NAME}.txt
wc ${NAME}-preview.md >> build-log-${NAME}.txt
tail -4 build-log-${NAME}.txt

pandoc --read markdown --number-sections --citeproc ${NAME}-preview.md -o ${NAME}-preview.pdf
pandoc --read markdown --number-sections --citeproc ${NAME}-preview.md -o ${NAME}-preview.html
# pandoc --read markdown --number-sections --citeproc ${NAME}-preview.md -o ${NAME}-preview.docx
popd

cp ${BUILD}/${NAME}-preview.pdf docs/files/${NAME}.pdf
