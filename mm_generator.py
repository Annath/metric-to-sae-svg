#!/usr/bin/env python3

mm_scaler = (1000.0 / 25.4)
values = [ *range(25,0,-1), *[ 5.5 ] ]
important_values = [ 8, 10, 12, 14, 15, 17, 19, 21 ]
quiet_values = [ 1, 2, 3, 5.5, 25 ]
text_offset = 10

def generate_mm_lines():
    output = ""

    fmt = """
                <g opacity="{5:.02f}">
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
                        font-size="{4:.01f}em"
                        font-family="sans-serif"
                        font-weight="bold"
                        text-anchor="end"
                        alignment-baseline="middle">{1} mm</text>
                </g>"""

    for i in values:
        opacity = 1
        font_size_em = 1.7
        line_width = 75

        if i in important_values:
            line_width = 150
            font_size_em = 2

        if i in quiet_values:
            opacity=0.5
            line_width = 25
            font_size_em = 1.3

        y_val = round(mm_scaler * i, 2)
        output += fmt.format(y_val,
            i,
            line_width,
            line_width + text_offset,
            font_size_em,
            opacity)

    return output

if __name__ == "__main__":
    print(generate_mm_lines())