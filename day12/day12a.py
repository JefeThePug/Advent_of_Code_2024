"""
--- Day 12: Garden Groups ---
 https://adventofcode.com/2024/day/12 
"""

import numpy as np

def dfs(neighbor: np.ndarray, i: int, j: int, kind: str, area: list[tuple[int, int]]) -> int:
    if i not in range(garden.shape[0]): return 0 if neighbor[i, j] else 1
    if j not in range(garden.shape[1]): return 0 if neighbor[i, j] else 1
    if visited[i, j]: return 0 if neighbor[i, j] else 1
    if garden[i, j] != kind: return 0 if neighbor[i, j] else 1

    visited[i, j] = True
    neighbor[i, j] = True
    area.append((i, j))
    
    result = dfs(neighbor, i - 1, j, kind, area)
    result += dfs(neighbor, i + 1, j, kind, area)
    result += dfs(neighbor, i, j - 1, kind, area)
    result += dfs(neighbor, i, j + 1, kind, area)
    return result

def get_fences() -> None:
    for i in range(garden.shape[0]):
        for j in range(garden.shape[1]):
            if not visited[i, j]:
                area = []
                perims = dfs(np.zeros(neighbors), i, j, garden[i, j], area)
                areas.append(len(area) * perims)
    
with open("input.txt") as f:
    garden = np.array([list(line) for line in f.read().split("\n")])
    visited = np.zeros_like(garden, dtype=bool)
    neighbors = (garden.shape[0] + 1, garden.shape[1] + 1)

areas = []
get_fences()
print(sum(areas))

#Total Fencing Price 1473408
