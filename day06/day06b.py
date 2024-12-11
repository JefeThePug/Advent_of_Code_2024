"""
--- Part Two ---
 https://adventofcode.com/2024/day/6#part2 
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
        self.mapping = {".":"X", "X":"+", "+":"*", "*":"O"}
        
    def move(self) -> None:
        if self.facing in ".X+*":
            self.x += self.dx
            self.y += self.dy
            self.occupy(self.mapping[sim[self.x, self.y]])
            if sim[self.x, self.y] == "O":
                self.out = True
                return
            self.look_ahead()
        elif self.facing == "#":
            self.dx, self.dy = self.dy, -self.dx
            self.look_ahead()
        elif self.facing == "@":
            self.out = True
            
    def occupy(self, val="X") -> None:
        sim[self.x, self.y] = val

    def look_ahead(self) -> None:
        self.facing = sim[self.x + self.dx, self.y + self.dy]

    
with open("input.txt") as f:
    map_data = np.array([list(line) for line in f.read().split("\n")])    
    grid = np.full((map_data.shape[0] + 2, map_data.shape[1] + 2), "@",)
    grid[1:-1, 1:-1] = map_data
    
guard_pos = np.where(grid == "^")
startX, startY = guard_pos[0][0], guard_pos[1][0]
path = [(0,0)]
loops = 0 

for block in path:
    sim = np.copy(grid)
    sim[block] = "#"
    guard = Guard(startX, startY, -1, 0)
    while not guard.out:
        guard.move()
    loops += np.count_nonzero(sim == "O")
    
    if block == (0, 0):
        path.extend([*zip(*np.where((sim == "X") | (sim == "+")))])
        path.remove((startX, startY))
        
print(loops)

#Possible Positions: 1748
