"""
--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's 
an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written 
forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:
    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. 
How many times does an X-MAS appear?

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
