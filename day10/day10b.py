"""
--- Part Two ---

The reindeer spends a few minutes reviewing your hiking trail map before realizing something, disappearing for a few 
minutes, and finally returning with yet another slightly-charred piece of paper.

The paper describes a second way to measure a trailhead called its rating. A trailhead's rating is the number of 
distinct hiking trails which begin at that trailhead. For example:
    .....0.
    ..4321.
    ..5..2.
    ..6543.
    ..7..4.
    ..8765.
    ..9....
    
The above map has a single trailhead; its rating is 3 because there are exactly three distinct hiking trails which 
begin at that position:
    .....0.   .....0.   .....0.
    ..4321.   .....1.   .....1.
    ..5....   .....2.   .....2.
    ..6....   ..6543.   .....3.
    ..7....   ..7....   .....4.
    ..8....   ..8....   ..8765.
    ..9....   ..9....   ..9....
    
      (A)             (B)
    ..90..9          012345
    ...1.98          123456
    ...2..7          234567
    6543456          345678
    765.987          4.6789
    876....          56789.
    987....          
A) Here is a map containing a single trailhead with rating 13.
B) This map contains a single trailhead with rating 227 (because there are 121 distinct hiking trails 
   that lead to the 9 on the right edge and 106 that lead to the 9 on the bottom edge).

Using the larget example from before, considering its trailheads in reading order, they have ratings of 
20, 24, 10, 4, 1, 4, 5, 8, and 5. The sum of all trailhead ratings in this larger example topographic map is 81.

You're not sure how, but the reindeer seems to have crafted some tiny flags out of toothpicks and bits of paper 
and is using them to mark trailheads on your topographic map. What is the sum of the ratings of all trailheads?
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
