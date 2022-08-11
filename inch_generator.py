#!/usr/bin/env python3

from fractions import Fraction

def generate_inch_lines():
    output = ""
    inch_scaler = (1000.0 / 16)

    fmt = """
                <g>
                    <line
                        style="stroke: rgb(0,0,0); stroke-width: 2;"
                        vector-effect="non-scaling-stroke"
                        x1="-100"
                        y1="-{0:.01f}"
                        x2="0"
                        y2="-{0:.01f}" />
                    <text
                        x="-110"
                        y="-{0:.01f}"
                        font-size="2em"
                        font-family="sans-serif"
                        font-weight="bold"
                        text-anchor="end"
                        alignment-baseline="middle">{1}/{2}"</text>
                </g>"""

    for i in range(15,0,-1):
        fractional_inch = Fraction(i, 16)
        y_val = round(inch_scaler * i, 2)
        output += fmt.format(y_val, fractional_inch.numerator, fractional_inch.denominator)

    return output

if __name__ == "__main__":
    print(generate_inch_lines())