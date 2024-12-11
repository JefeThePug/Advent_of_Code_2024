"""
--- Part Two ---
 https://adventofcode.com/2024/day/4#part2 
"""

import numpy as np

def chain(x: int, y: int, offset_x: int, offset_y: int, letter: str) -> bool:
    opposite = {"S":"M", "M":"S"}[letter]
    
    if x + 2 >= word_array.shape[0] or y + 2 >= word_array.shape[1]: return False
    if word_array[x + offset_x, y + offset_y] != letter: return False
    if word_array[x + 1, y + 1] != "A": return False
    if word_array[x + 2, y + 2] != opposite: return False
    return word_array[x + offset_y, y + offset_x] == opposite

def find_words() -> int:
    offsets = [(2, 0), (0, 2)]
    total = 0

    for row in range(word_array.shape[0]):
        for col in range(word_array.shape[1]):
            if word_array[row, col] in "SM":
                total += sum(chain(row, col, *offset, word_array[row, col]) for offset in offsets)
    return total

with open("input.txt") as f:
    word_array = np.array([list(f) for f in f.read().split("\n")])
    print(find_words())
    
# X-MAS appearances 2029
