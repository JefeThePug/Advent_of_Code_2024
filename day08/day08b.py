"""
--- Part Two ---
 https://adventofcode.com/2024/day/8#part2 
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
