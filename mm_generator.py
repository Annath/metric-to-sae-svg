#!/usr/bin/env python3

mm_scaler = (1000.0 / 25.4)
important_values = [ 8, 10, 12, 14, 15, 17, 19, 21 ]
text_offset = 10

def generate_mm_lines():
    output = ""

    fmt = """
                <g>
                    <line
                        style="stroke: rgb(0,0,0); stroke-width: 2;"
                        vector-effect="non-scaling-stroke"
                        x1="-{2}"
                        y1="-{0:.02f}"
                        x2="0"
                        y2="-{0:.02f}" />
                    <text
                        x="-{3}"
                        y="-{0:.02f}"
                        font-size="2em"
                        font-family="sans-serif"
                        font-weight="bold"
                        text-anchor="end"
                        alignment-baseline="middle">{1} mm</text>
                </g>"""

    for i in range(24,0,-1):
        line_width = 100
        if i in important_values:
            line_width = 200
        y_val = round(mm_scaler * i, 2)
        output += fmt.format(y_val, i, line_width, line_width + text_offset)

    return output

if __name__ == "__main__":
    print(generate_mm_lines())