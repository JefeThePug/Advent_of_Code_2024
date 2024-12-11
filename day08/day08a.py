"""
--- Day 8: Resonant Collinearity ---
 https://adventofcode.com/2024/day/8 
"""

from string import ascii_letters, digits
from itertools import combinations
import numpy as np

def add_antinodes(x: int, y: int, dx: int, dy: int) -> None:
    newx, newy = x + dx, y + dy
    if newx in range(grid.shape[0]) and newy in range(grid.shape[1]):
        antinodes[(newx, newy)] = "#"
            
def get_d(ax: int, ay: int, bx: int, by: int) -> tuple[int, int]:
    return (ax - bx, ay - by)

def count_antinodes() -> int:         
    for freq in ascii_letters + digits:
        for a, b in combinations(zip(*np.where(grid == freq)), 2):
            d = get_d(*a, *b)
            add_antinodes(*a, *d)
            add_antinodes(*b, -d[0], -d[1])
    return np.count_nonzero(antinodes == "#")
    
with open("input.txt") as f:
    grid = np.array([list(line) for line in f.read().split("\n")])
    antinodes = np.full_like(grid, ".")
    print(count_antinodes())

#Total Unique Locations: 369
