#!/usr/bin/env python3

from cgitb import text
from fractions import Fraction

step_size = 32

text_offset = 10
inch_scaler = (1000.0 / step_size)

def generate_inch_lines():
    output = ""

    fmt = """
                <g opacity="{6:.02f}">
                    <line
                        style="stroke: rgb(0,0,0); stroke-width: 2;"
                        vector-effect="non-scaling-stroke"
                        x1="{3}"
                        y1="-{0:.01f}"
                        x2="0"
                        y2="-{0:.01f}" />
                    <text
                        x="{4}"
                        y="-{0:.01f}"
                        font-size="{5:.01f}em"
                        font-family="sans-serif"
                        font-weight="bold"
                        text-anchor="start"
                        alignment-baseline="middle">{1}/{2}"</text>
                </g>"""

    for i in range((step_size-1),0,-1):
        opacity = 1
        line_width = 150
        font_size_em = 2
        fractional_inch = Fraction(i, step_size)

        if fractional_inch.denominator == 32:
            opacity = 0.5
            font_size_em = 1.5
            line_width = 50

        if fractional_inch.denominator == 16:
            font_size_em = 1.7
            line_width = 100

        y_val = round(inch_scaler * i, 2)
        output += fmt.format(y_val,
            fractional_inch.numerator,
            fractional_inch.denominator,
            line_width,
            line_width + text_offset,
            font_size_em,
            opacity)

    return output

if __name__ == "__main__":
    print(generate_inch_lines())