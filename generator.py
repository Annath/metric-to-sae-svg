#!/usr/bin/env python3

from inch_generator import generate_inch_lines
from mm_generator import generate_mm_lines
from os import mkdir

output_dir = "output"
output_file = f"{output_dir}/metric-to-sae.svg"

def main():
    inch_lines = generate_inch_lines()
    mm_lines = generate_mm_lines()

    svg = None
    with open("chart-template.svg", "r") as f:
        svg = f.read()

    if svg != None:
        svg = svg.replace("{{INCHES_CONTENT}}", inch_lines)
        svg = svg.replace("{{MILLIMETERS_CONTENT}}", mm_lines)

    # print(svg)

    try:
        mkdir(output_dir)
    except FileExistsError:
        pass

    with open(output_file, "w") as f:
        f.write(svg)

if __name__ == "__main__":
    main()