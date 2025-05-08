#!/usr/bin/python3

import sys
if len(sys.argv) == 1:
    for x in range(11):
        output_str = f"Table de {x}:"
        for y in  range(11):
            res = x * y
            output_str += f" {res}"
        print(output_str)
else:
    print("none")