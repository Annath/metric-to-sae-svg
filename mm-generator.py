mm_scaler = (1000.0 / 25.4)

fmt = """
            <g>
                <line
                    style="stroke: rgb(0,0,0); stroke-width: 2;"
                    vector-effect="non-scaling-stroke"
                    x1="100"
                    y1="{0:.02f}"
                    x2="0"
                    y2="{0:.02f}" />
                <text
                    x="110"
                    y="{0:.02f}"
                    font-size="2em"
                    font-family="sans-serif"
                    font-weight="bold"
                    text-anchor="start"
                    alignment-baseline="middle">{1} mm</text>
            </g>"""

for i in range(25,0,-1):
    y_val = round(mm_scaler * i, 2)
    print(fmt.format(y_val * -1, i))