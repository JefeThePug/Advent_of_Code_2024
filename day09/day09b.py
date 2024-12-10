"""
--- Part Two ---

Upon completion, two things immediately become clear. First, the disk definitely has a lot more contiguous free space, 
just like the amphipod hoped. Second, the computer is running much more slowly! Maybe introducing all of that file 
system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual blocks, he'd like to try compacting the files on
his disk by moving whole files instead.

This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to 
move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID 
number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does 
not move.

The first example from above now proceeds differently:
    00...111...2...333.44.5555.6666.777.888899
    0099.111...2...333.44.5555.6666.777.8888..
    0099.1117772...333.44.5555.6666.....8888..
    0099.111777244.333....5555.6666.....8888..
    00992111777.44.333....5555.6666.....8888..
    
The process of updating the filesystem checksum is the same; now, this example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method instead. 
What is the resulting filesystem checksum?

"""

from itertools import chain
    
with open("input.txt") as f:
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
