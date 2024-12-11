"""
--- Day 9: Disk Fragmenter ---
 https://adventofcode.com/2024/day/9 
"""

from itertools import chain

with open("input.txt") as f:
    blocks = [*chain.from_iterable(["."] * int(v) if i & 1 else [f"{i//2}"] * int(v) for i, v in enumerate(f.readline()))]
    files = [e for e in blocks if e != "."]
    result = [e if e != "." else files.pop() for e in blocks[:len(files)]]
    total = sum(i * int(n) for i, n in enumerate(result))
    print(total)

#Filesystem Checksum is 6386640365805
