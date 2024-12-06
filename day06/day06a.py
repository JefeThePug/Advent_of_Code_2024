"""
--- Day 6: Guard Gallivant ---

The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit 
manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a 
group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The 
Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the 
perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.

   (1)                       (2)                       (3)                       (4)
....#.....                ....#.....                ....#.....                ....#.....
....^....#                ........>#                .........#                .........#
..........                ..........                ..........                ..........
..#.......                ..#.......                ..#.......                ..#.......
.......#..                .......#..                .......#..                .......#..
..........                ..........                ..........                ..........
.#........                .#........                .#......v.                .#........
........#.                ........#.                ........#.                ........#.
#.........                #.........                #.........                #.........
......#...                ......#...                ......#...                ......#v..
1) Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile 
   of failed suit prototypes)
2) Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new 
   facing direction.
3) Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward.
4) This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of 
   universal solvent).

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. 
Including the guard's starting position, the positions visited by the guard before leaving the area are marked with X:
    ....#.....
    ....XXXXX#
    ....X...X.
    ..#.X...X.
    ..XXXXX#X.
    ..X.X.X.X.
    .#XXXXXXX.
    .XXXXXXX#.
    #XXXXXXX..
    ......#X..
    
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

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
