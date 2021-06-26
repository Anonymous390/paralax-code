import random
from dataclasses import dataclass

from .shapes import I, J, L, O, S, T, Z


@dataclass
class Shape:
    shapes = [S, Z, I, O, J, L, T]
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0),
                    (255, 165, 0), (0, 0, 255), (128, 0, 128)]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(self.shapes)
        self.color = self.shape_colors[self.shapes.index(self.shape)]
        self.rotation = 0
