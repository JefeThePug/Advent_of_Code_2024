"""
--- Part Two ---
 https://adventofcode.com/2024/day/14#part2 
"""

import numpy as np
import re
from PIL import Image, ImageDraw, ImageFont

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
    size = (101, 103)
    grid = np.zeros(size, dtype=int)
    robots = [Robot(*map(int, re.findall(r"-?\d+", d))) for d in f.readlines()]

main_image = Image.new("RGB", (10000, 10000), color=(0, 0, 0))
for i in range(10_000):
    for r in robots: 
        r.move()
    image_data = np.where(grid == 0, 0, 255).astype(np.uint8)
    image = Image.fromarray(image_data, mode='L').convert("RGB")
    draw = ImageDraw.Draw(image)
    draw.text((5, 5), f"{i + 1}", fill=(0, 255, 0))
    row, col = divmod(i, 100)
    main_image.paste(image, (col*100, row*100)) 
main_image.save("robots.bmp")
print("Complete")

#Easter Egg Displayed at: 6771
