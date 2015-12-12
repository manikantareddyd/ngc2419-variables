echo "sort" && python src/sort.py && \
echo "sort2" && python src/sort2.py && \
echo "listing" && python src/mklist.py && \
echo "combine" && python src/combine.py && \
echo "clean" && python src/cleaner.py && \
echo "trim" && python src/trim.py && \
echo "align" && python src/dft.py && \
echo "trim" && python src/align_trim.py && \
echo "phot" && python src/photmetry.py
