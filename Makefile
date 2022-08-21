SHELL = /bin/sh
FILE_NAME = metric-to-sae
OUTPUT_DIR = output

TEMPLATE = chart-template.svg
SVG = ${OUTPUT_DIR}/${FILE_NAME}.svg
PNG = ${OUTPUT_DIR}/${FILE_NAME}.png
PDF = ${OUTPUT_DIR}/${FILE_NAME}.pdf

all: svg previews
svg: ${SVG}
previews: ${PDF} ${PNG}

${PDF}: ${SVG}
	inkscape -z ${SVG} -d 300 -A ${PDF} 2>/dev/null

${PNG}: ${SVG}
	inkscape -z ${SVG} -d 150 -e ${PNG} 2>/dev/null

${SVG}: ${TEMPLATE}
	mkdir -p ${OUTPUT_DIR}
	./generator.py ${SVG}

clean:
	rm -rf ${OUTPUT_DIR}