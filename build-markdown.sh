COURSE_1=uclr100-2024-fall
COURSE_2=engl323-2024-fall

# Unlock Markdown files for overwriting
for f in build/*md ; do chmod 666 $f ; done

pushd partials

# Build a single Markdown file from atomized components
pandoc --metadata-file ../config/pandoc-metadata.yaml --lua-filter include-files.lua --wrap=preserve ../frames/$COURSE_1.md -so ../build/$COURSE_1.md
pandoc --metadata-file ../config/pandoc-metadata.yaml --lua-filter include-files.lua --wrap=preserve ../frames/$COURSE_2.md -so ../build/$COURSE_2.md

popd

# Make Markdown files in build/ read-only
for f in build/*md ; do chmod 444 $f ; done
