"""
--- Day 2: Red-Nosed Reports ---
 https://adventofcode.com/2024/day/2 
"""

def check(arr: list[int]) -> bool:
    gap = all(abs(a - b) < 4 for a, b in zip(arr, arr[1:]))
    inc = all(a < b for a, b in zip(arr, arr[1:]))
    dec = all(a > b for a, b in zip(arr, arr[1:]))
    return gap and (inc or dec)

def get_num_safe(s: str) -> int:
    return sum(check(r) for r in map(lambda x: [*map(int, x.split())], s.split("\n")))
    
with open("input.txt") as f:
    print(get_num_safe(f.read()))
    
#686 reports safe
