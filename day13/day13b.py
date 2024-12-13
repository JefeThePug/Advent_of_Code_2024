"""
--- Part Two ---
 https://adventofcode.com/2024/day/13#part2 
"""

import re
from z3 import Int, Solver
        
def cashout(A: int, B: int) -> int:
    return A*3 + B

def solve(x1: int, y1: int, x2: int, y2: int, xc: int, yc: int) -> tuple[int, int]:
    A = Int('A')
    B = Int('B')

    solver = Solver()

    solver.add(x1 * A + x2 * B == 10_000_000_000_000 + xc)
    solver.add(y1 * A + y2 * B == 10_000_000_000_000 + yc)
    solver.add(A >= 0)
    solver.add(B >= 0)

    if f"{solver.check()}" == "sat":
        model = solver.model()
        return model[A].as_long(), model[B].as_long()
    else:
        return 0, 0

with open("input.txt") as f:
    machines = (map(int, re.findall(r"\d+", x)) for x in f.read().split("\n\n"))

print(sum(cashout(*solve(*m)) for m in machines))

#Fewest Tokens: 95688837203288