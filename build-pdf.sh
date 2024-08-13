COURSE_1=uclr100-2024-fall

pandoc --citeproc --toc --number-sections build/$COURSE_1.md -o build/$COURSE_1.pdf
