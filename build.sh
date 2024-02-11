if [ ! -e build/ ] ; then
	mkdir build/
fi

pandoc --metadata-file config/pandoc-metadata.yaml --lua-filter include-files.lua --citeproc --number-sections \
       zetteln/frame-0000-20240101165940.md \
       -o build/engl321-2024-spring.pdf

pandoc --metadata-file config/pandoc-metadata.yaml --lua-filter include-files.lua --citeproc --number-sections \
       zetteln/frame-0002-20240110165851.md \
       -o build/engl441-2024-spring.pdf
