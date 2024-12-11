"""
--- Day 7: Bridge Repair ---
 https://adventofcode.com/2024/day/7 
"""

import re
from itertools import product
from operator import add, mul

FUNS = {"+": add, "*": mul}

def possibility(total: int, values: list[int]) -> int:
    operations = product(FUNS.keys(), repeat=len(values) - 1)
    for op in operations:
        ops = list(op)
        vals = values[::]
        result = vals.pop(0)
        while ops:
            result = FUNS[ops.pop(0)](result, vals.pop(0))
            if result > total: continue
        if result == total:
            return total
    return 0
    
with open("input.txt") as f:
    totals, equations = zip(*re.findall(r"(\d+): ([\d ]+)", f.read()))
    total = 0
    for i in range(len(totals)):
        values = [*map(int, equations[i].split())]
        total += possibility(int(totals[i]), values)
    print(total)

#total calibration is 2299996598890
