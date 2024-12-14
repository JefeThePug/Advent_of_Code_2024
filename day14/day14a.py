"""
--- Day 14: Restroom Redoubt ---
 https://adventofcode.com/2024/day/14 
"""

import numpy as np
import re

class Robot:
    def __init__(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        grid[x, y] += 1
        
    def move(self) -> None:
        grid[self.x, self.y] -= 1
        self.x = (self.x + self.dx)%grid.shape[0]
        self.y = (self.y + self.dy)%grid.shape[1]
        grid[self.x, self.y] += 1     
        
with open("data.txt") as f:
    # size = (11, 7) # Test Input
    size = (101, 103) # Puzzle Input
    grid = np.zeros(size, dtype=int)
    robots = [Robot(*map(int, re.findall(r"-?\d+", d))) for d in f.readlines()]

for _ in range(100):
    for r in robots: 
        r.move()
        
mid_row, mid_col = grid.shape[0]//2, grid.shape[1]//2
result = np.sum(grid[:mid_row, :mid_col])
result *= np.sum(grid[:mid_row, mid_col+1:])
result *= np.sum(grid[mid_row+1:, :mid_col])
result *= np.sum(grid[mid_row+1:, mid_col+1:])
print(result)
        
#Safety Factor at 100 Seconds: 231221760
