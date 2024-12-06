"""
--- Part Two ---

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the 
lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of 
the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is 
simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place 
the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions 
for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there 
right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck 
in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard 
moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves 
both up/down and left/right.

   (1)               (2)               (3)               (4)               (5)               (6)
....#.....        ....#.....        ....#.....        ....#.....        ....#.....        ....#.....
....+---+#        ....+---+#        ....+---+#        ....+---+#        ....+---+#        ....+---+#
....|...|.        ....|...|.        ....|...|.        ....|...|.        ....|...|.        ....|...|.
..#.|...|.        ..#.|...|.        ..#.|...|.        ..#.|...|.        ..#.|...|.        ..#.|...|.
....|..#|.        ..+-+-+#|.        ..+-+-+#|.        ..+-+-+#|.        ..+-+-+#|.        ..+-+-+#|.
....|...|.        ..|.|.|.|.        ..|.|.|.|.        ..|.|.|.|.        ..|.|.|.|.        ..|.|.|.|.
.#.O^---+.        .#+-^-+-+.        .#+-^-+-+.        .#+-^-+-+.        .#+-^-+-+.        .#+-^-+-+.
........#.        ......O.#.        .+----+O#.        ..|...|.#.        ....|.|.#.        .+----++#.
#.........        #.........        #+----+...        #O+---+...        #..O+-+...        #+----++..
......#...        ......#...        ......#...        ......#...        ......#...        ......#O..

- Option one, put a printing press next to the guard's starting position:
- Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:
- Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:
- Option four, put an alchemical retroencabulator near the bottom left corner:
- Option five, put the alchemical retroencabulator a bit to the right instead:
- Option six, put a tank of sovereign glue right next to the tank of universal solvent:

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into 
position without the guard noticing. The important thing is having enough options that you can find one that minimizes 
time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. 
How many different positions could you choose for this obstruction?

"""

import numpy as np

class Guard:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.occupy()
        self.dx = dx
        self.dy = dy
        self.facing = None
        self.look_ahead()
        self.out = False
        self.mapping = {".":"X", "X":"+", "+":"*", "*":"O"}
        
    def move(self):
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
            
    def occupy(self, val="X"):
        sim[self.x, self.y] = val

    def look_ahead(self):
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
