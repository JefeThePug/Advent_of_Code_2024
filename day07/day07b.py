"""
--- Part Two ---

The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety 
tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. 
For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example 
has three more equations that can be made true by inserting operators:

- 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
- 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
- 192: 17 8 14 can be made true using 17 || 8 + 14.

Adding up all six test values (the three that could be made before using only + and * plus the new three that can now 
be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. 
What is their total calibration result?

"""

import re
from itertools import product
from operator import add, mul

FUNS = {"+": add, "*": mul, "|": lambda x, y: int(f"{x}{y}")}

def possibility(total: int, values: list[int]) -> int:
    operations = product(FUNS.keys(), repeat=len(values) - 1)
    for op in operations:
        ops = list(op)
        vals = values[::]
        result = vals.pop(0)
        while ops:
            result = FUNS[ops.pop(0)](result, vals.pop(0))
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

#total calibration is 362646859298554
