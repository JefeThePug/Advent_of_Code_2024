"""
--- Day 8: Resonant Collinearity ---

You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it seems to 
have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation 
Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific 
frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of 
these antennas. For example:
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    
The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. 
In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but 
only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same 
frequency, there are two antinodes, one on either side of them.


       (1)                       (2)                       (3)
    ..........                ..........                ..........
    ...#......                ...#......                ...#......
    ..........                #.........                #.........
    ....a.....                ....a.....                ....a.....
    ..........                ........a.                ........a.
    .....a....                .....a....                .....a....
    ..........                ..#.......                ..#.......
    ......#...                ......#...                ......A...
    ..........                ..........                ..........
    ..........                ..........                ..........
1) So, for these two antennas with frequency a, they create the two antinodes marked with #.
2) Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, 
   but two are off the right side of the map, so instead it adds only two.
3) Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However, 
   antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A 
   creates no antinodes but has a lowercase-a-frequency antinode at its location.

The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an 
antinode overlapping the topmost A-frequency antenna:
    ......#....#
    ...#....0...
    ....#0....#.
    ..#....0....
    ....0....#..
    .#....A.....
    ...#........
    #......#....
    ........A...
    .........A..
    ..........#.
    ..........#.
    
Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that 
contain an antinode within the bounds of the map.

Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?

"""

from string import ascii_letters, digits
from itertools import combinations
import numpy as np

def add_antinodes(x: int, y: int, dx: int, dy: int) -> None:
    newx, newy = x + dx, y + dy
    if newx in range(grid.shape[0]) and newy in range(grid.shape[1]):
        antinodes[(newx, newy)] = "#"
            
def get_d(ax: int, ay: int, bx: int, by: int) -> tuple[int, int]:
    return (ax - bx, ay - by)

def count_antinodes() -> int:         
    for freq in ascii_letters + digits:
        for a, b in combinations(zip(*np.where(grid == freq)), 2):
            d = get_d(*a, *b)
            add_antinodes(*a, *d)
            add_antinodes(*b, -d[0], -d[1])
    return np.count_nonzero(antinodes == "#")
    
with open("input.txt") as f:
    grid = np.array([list(line) for line in f.read().split("\n")])
    antinodes = np.full_like(grid, ".")
    print(count_antinodes())

#Total Unique Locations: 369
