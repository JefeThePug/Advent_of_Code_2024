"""
--- Part Two ---
 https://adventofcode.com/2024/day/10#part2 
"""

import numpy as np

OFFSETS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def path(x: int, y: int) -> int:
    if grid[x, y] == 9: return 1

    result = 0
    for dx, dy in OFFSETS:
        newx, newy = x + dx, y + dy
        if (
            all(d in range(r) for d, r in zip((newx, newy), grid.shape))
            and grid[newx, newy] == grid[x, y] + 1
        ):
            result += path(newx, newy)
    return result
    
with open("input.txt") as f:
    grid = np.array([list(map(int, line)) for line in f.read().split("\n")])
    zeros = [*zip(*np.where((grid == 0)))]
    print(sum(path(x, y) for x, y in zeros))

#Sum of Ratings: 1651
