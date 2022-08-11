#!/usr/bin/env python3

def generate_mm_lines():
    output = ""

    mm_scaler = (1000.0 / 25.4)

    fmt = """
                <g>
                    <line
                        style="stroke: rgb(0,0,0); stroke-width: 2;"
                        vector-effect="non-scaling-stroke"
                        x1="100"
                        y1="-{0:.02f}"
                        x2="0"
                        y2="-{0:.02f}" />
                    <text
                        x="110"
                        y="-{0:.02f}"
                        font-size="2em"
                        font-family="sans-serif"
                        font-weight="bold"
                        text-anchor="start"
                        alignment-baseline="middle">{1} mm</text>
                </g>"""

    for i in range(24,1,-1):
        y_val = round(mm_scaler * i, 2)
        output += fmt.format(y_val, i)

    return output

if __name__ == "__main__":
    print(generate_mm_lines())