"""
--- Part Two ---
 https://adventofcode.com/2024/day/3#part2 
"""

import re

def parse(s: str) -> int:
    return sum(get_sum(p.split("don't()")[0]) for p in s.split("do()"))

def get_sum(s: str) -> int:
    return sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", s))

with open("input.txt") as f:
    print(parse(f.read()))
    
# sum is 82868252
