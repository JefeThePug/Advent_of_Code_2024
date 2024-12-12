"""
--- Part Two ---
 https://adventofcode.com/2024/day/12#part2 
"""

import numpy as np

def dfs(i: int, j: int, kind: str, area: list[tuple[int, int]]) -> None:
    if i not in range(garden.shape[0]): return
    if j not in range(garden.shape[1]): return
    if visited[i, j]: return
    if garden[i, j] != kind: return

    visited[i, j] = True
    area.append((i, j))
    
    dfs(i - 1, j, kind, area)
    dfs(i + 1, j, kind, area)
    dfs(i, j - 1, kind, area)
    dfs(i, j + 1, kind, area)

def get_sides(area: list[tuple[int, int]]):
    rows, cols = zip(*area)
    min_r, max_r = min(rows), max(rows)
    min_c, max_c = min(cols), max(cols)
    block = np.zeros((max_r - min_r + 3, max_c - min_c + 3))
    
    for x, y in area:
        block[x - min_r + 1, y - min_c + 1] = 1
    
    double_corner = [(1,0,0,1), (0,1,1,0)]    
    corner = [
        (0,0,0,1), (0,0,1,0), (0,1,0,0), (1,0,0,0), (1,1,1,0), 
        (1,1,0,1), (1,0,1,1), (0,1,1,1), (1,0,0,1), (0,1,1,0),
    ]

    corners = 0
    for i in range(block.shape[0] - 1):
        for j in range(block.shape[1] - 1):
            b = tuple(block[i:i+2, j:j+2].flatten())
            corners += (b in corner) + (b in double_corner)
    return corners

def get_fences() -> None:
    for i in range(garden.shape[0]):
        for j in range(garden.shape[1]):
            if not visited[i, j]:
                area = []
                dfs(i, j, garden[i, j], area)
                areas.append(len(area) * get_sides(area))
    
with open("data.txt") as f:
    garden = np.array([list(line) for line in f.read().split("\n")])
    visited = np.zeros_like(garden, dtype=bool)
    neighbors = (garden.shape[0] + 1, garden.shape[1] + 1)

areas = []
get_fences()
print(sum(areas))

#Total Fencing Price 886364
