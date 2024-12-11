"""
--- Part Two ---
 https://adventofcode.com/2024/day/2#part2 
"""

def check_part(arr: list[int]) -> bool:
    gap = all(abs(a - b) < 4 for a, b in zip(arr, arr[1:]))
    inc = all(a < b for a, b in zip(arr, arr[1:]))
    dec = all(a > b for a, b in zip(arr, arr[1:]))
    return gap and (inc or dec)

def check(arr: list[int]) -> bool:
    if check_part(arr): 
        return True
    for i in range(len(arr)):
        if check_part(arr[:i] + arr[i + 1:]): 
            return True
    return False

def get_num_safe(s: str) -> int:
    return sum(check(r) for r in map(lambda x: [*map(int, x.split())], s.split("\n")))
    
with open("input.txt") as f:
    print(get_num_safe(f.read()))
    
#717 reports safe
