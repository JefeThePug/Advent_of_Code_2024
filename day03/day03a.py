"""
--- Day 3: Mull It Over ---
 https://adventofcode.com/2024/day/3 
"""

import re

def get_sum(s: str) -> int:
    return sum(int(a)*int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", s))

with open("input.txt") as f:
    print(get_sum(f.read()))
    
# sum is 170778545
