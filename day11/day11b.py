"""
--- Part Two ---
https://adventofcode.com/2024/day/11#part2
"""

from functools import cache
from math import floor, log10

@cache
def process(n: int) -> int | tuple[int, int]:
    if n == 0: return 1
    digits = floor(log10(n)) + 1
    if not digits&1: return divmod(n, 10**(digits//2))
    return n*2024

@cache
def iterate(stone: int, i: int) -> int:
    if i == 0: return 1
    value = process(stone)
    if isinstance(value, tuple):
        return iterate(value[0], i - 1) + iterate(value[1], i - 1)
    else:
        return iterate(value, i - 1)
    
with open("input.txt") as f:
    line = map(int, f.read().split())

print(sum(iterate(stone, 75) for stone in line))

#Total Stones: 274229228071551
