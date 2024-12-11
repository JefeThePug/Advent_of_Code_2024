"""
--- Day 1: Historian Hysteria ---
 https://adventofcode.com/2024/day/1 
"""

def get_total_dist(s: str) -> int:
    lists = [sorted(x) for x in zip(*[[int(a), int(b)] for a, b in map(str.split, s.split("\n"))])]
    return sum(abs(a - b) for a, b in zip(*lists))
    
with open("input.txt") as f:
    print(get_total_dist(f.read()))
    
#total distance is 1258579
