"""
--- Day 4: Ceres Search ---
 https://adventofcode.com/2024/day/4 
"""

import numpy as np

def chain(x: int, y: int, offset_x: int, offset_y: int, i: int=0) -> bool:
    if i > 2: return True
    
    new_x = x + offset_x
    new_y = y + offset_y
    if new_x < 0 or new_y < 0 or new_x >= word_array.shape[0] or new_y >= word_array.shape[1]:
            return False
    
    if word_array[new_x, new_y] == "MAS"[i]:    
        return chain(new_x, new_y, offset_x, offset_y, i + 1)
    return False

def find_words() -> int:
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total = 0

    for row in range(word_array.shape[0]):
        for col in range(word_array.shape[1]):
            if word_array[row, col] == "X":
                total += sum(chain(row, col, *offset) for offset in offsets)
    return total

with open("input.txt") as f:
    word_array = np.array([list(f) for f in f.read().split("\n")])
    print(find_words())
    
# XMAS appearances 2567
