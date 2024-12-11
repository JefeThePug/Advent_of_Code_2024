"""
--- Part Two ---
 https://adventofcode.com/2024/day/9#part2 
"""

from itertools import chain
    
with open("data.txt") as f:
    blocks = [*chain.from_iterable([-1] * int(v) if i & 1 else [i // 2] * int(v) for i, v in enumerate(f.readline()))]

length = len(blocks)
i = 0
j = length - 1

while j > 0:
    if blocks[j] != -1:
        jstart = j
        size = 1
        while jstart > 0 and blocks[jstart - 1] == blocks[j]:
            jstart -= 1
            size += 1
        i = 0
        j = jstart
        while i < j and blocks[i:i + size].count(-1) != size:
            i += 1
        blocks[i:i + size], blocks[j:j + size] = blocks[j:j + size], blocks[i:i + size]
    j -= 1

    
total = sum(i * n for i, n in enumerate(blocks) if n != -1)
print(total)

#Filesystem Checksum is 6423258376982
