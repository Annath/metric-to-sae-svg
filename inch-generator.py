from fractions import Fraction
import fractions

inch_scaler = (1000.0 / 16)

fmt = """            <g>
                <line
                    style="stroke: rgb(0,0,0); stroke-width: 2;"
                    vector-effect="non-scaling-stroke"
                    x1="-100"
                    y1="{0:.1f}"
                    x2="0"
                    y2="{0:.1f}" />
                <text
                    x="-110"
                    y="{0:.1f}"
                    font-size="2em"
                    font-family="sans-serif"
                    font-weight="bold"
                    text-anchor="end"
                    alignment-baseline="middle">{1}/{2}"</text>
            </g>"""

print('        <g id="inches">')

for i in range(15,0,-1):
    y_val = round(inch_scaler * i, 2)
    fractional_inch = Fraction(i, 16)
    print(fmt.format(y_val * -1, fractional_inch.numerator, fractional_inch.denominator))

print("</g>")