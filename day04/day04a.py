"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. 
After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if 
you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. 
It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. 
Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. 
For example:               Where letters not involved in any XMAS have been replaced with .:
    MMMSXXMASM                    ....XXMAS.
    MSAMXMSMSA                    .SAMXMS...
    AMXSXMAAMM                    ...S..A...
    MSAMASMSMX                    ..A.A.MS.X
    XMASAMXAMM         =>         XMASAMX.MM
    XXAMMXXAMA                    X.....XA.A
    SMSMSASXSS                    S.S.S.S.SS
    SAXAMASAAA                    .A.A.A.A.A
    MAMMMXMMMM                    ..M.M.M.MM
    MXMXAXMASX                    .X.X.XMASX

In this word search, XMAS occurs a total of 18 times.

Take a look at the little Elf's word search. How many times does XMAS appear?

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
