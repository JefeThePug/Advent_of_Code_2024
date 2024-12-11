"""
--- Day 6: Guard Gallivant ---
 https://adventofcode.com/2024/day/6 
"""

import numpy as np

class Guard:
    def __init__(self, x: int, y: int, dx: int, dy: int):
        self.x = x
        self.y = y
        self.occupy()
        self.dx = dx
        self.dy = dy
        self.facing = None
        self.look_ahead()
        self.out = False
        
    def move(self) -> None:
        if self.facing in ".X":
            self.x += self.dx
            self.y += self.dy
            self.occupy()
            self.look_ahead()
        elif self.facing == "#":
            self.dx, self.dy = self.dy, -self.dx
            self.look_ahead()
        elif self.facing == "@":
            self.out = True
            
    def occupy(self) -> None:
        grid[self.x, self.y] = "X"

    def look_ahead(self) -> None:
        self.facing = grid[self.x + self.dx, self.y + self.dy]

    
with open("input.txt") as f:
    map_data = np.array([list(line) for line in f.read().split("\n")])
    grid = np.full((map_data.shape[0] + 2, map_data.shape[1] + 2), "@",)
    grid[1:-1, 1:-1] = map_data
    
guard_pos = np.where(grid == "^")
guard = Guard(guard_pos[0][0], guard_pos[1][0], -1, 0)

while not guard.out:
    guard.move()
    
print(np.count_nonzero(grid == "X"))
    
#total positions 5312
