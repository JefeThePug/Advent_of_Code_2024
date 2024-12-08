"""
--- Part Two ---

Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into 
your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two 
antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the 
position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:
    T....#....
    ...T......
    .T....#...
    .........#
    ..#.......
    ..........
    ...#......
    ..........
    ....#.....
    ..........
    
In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! 
This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:
    ##....#....#
    .#.#....0...
    ..#.#0....#.
    ..##...0....
    ....0....#..
    .#...#A....#
    ...#..#.....
    #....#.#....
    ..#.....A...
    ....#....A..
    .#........#.
    ...#......##
    
Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map 
contain an antinode?

"""

from string import ascii_letters, digits
from itertools import combinations
import numpy as np

def add_antinodes(x: int, y: int, dx: int, dy: int) -> None:
    newx, newy = x, y
    while True:
        newx += dx
        newy += dy
        if newx not in range(grid.shape[0]) or newy not in range(grid.shape[1]): break
        antinodes[(newx, newy)] = "#"

def get_d(ax: int, ay: int, bx: int, by: int) -> tuple[int, int]:
    return (ax - bx, ay - by)

def generate_antinodes() -> None: 
    for freq in ascii_letters + digits:
        for a, b in combinations(zip(*np.where(grid == freq)), 2):
            if a == b: continue
            d = get_d(*a, *b)
            add_antinodes(*a, *d)
            add_antinodes(*b, -d[0], -d[1])
    
with open("input.txt") as f:
    grid = np.array([list(line) for line in f.read().split("\n")])
    antinodes = np.full_like(grid, ".")
    generate_antinodes()
    result = np.where(grid != '.', '#', antinodes)
    print(np.count_nonzero(result == "#"))

#Total Unique Locations: 1169
