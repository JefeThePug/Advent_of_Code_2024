"""
--- Part Two ---
 https://adventofcode.com/2024/day/1#part2 
"""

def get_score(s: str) -> int:
    lista, listb = zip(*[[int(a), int(b)] for a, b in map(str.split, s.split("\n"))])
    return sum(a*listb.count(a) for a in lista)
    
with open("input.txt") as f:
    print(get_score(f.read()))
    
#similarity score is 23981443
