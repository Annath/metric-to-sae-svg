SHELL = /bin/sh
FILE_NAME = metric-to-sae
OUTPUT_DIR = output
PREVIEWS_DIR = ${OUTPUT_DIR}/previews
SVG_PATH = ${OUTPUT_DIR}/${FILE_NAME}.svg

all: previews

previews: png pdf

pdf: svg
	mkdir -p ${PREVIEWS_DIR}
	inkscape -z ${SVG_PATH} -d 300 -A ${PREVIEWS_DIR}/${FILE_NAME}.pdf 2>/dev/null

png: svg
	mkdir -p ${PREVIEWS_DIR}
	inkscape -z ${SVG_PATH} -w 927 -h 1200 -e ${PREVIEWS_DIR}/${FILE_NAME}.png 2>/dev/null

svg:
	mkdir -p ${OUTPUT_DIR}
	./generator.py ${SVG_PATH}

clean:
	rm -rf ${OUTPUT_DIR}