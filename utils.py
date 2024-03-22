"""Utility classes to support the project"""
from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple


class Coordinates(NamedTuple):
    x: int
    y: int


class Colors(Enum):
    WALL = (0, 0, 0)
    VISITED = (60, 60, 60)
    TO_VISIT = (115, 70, 133)
    NOT_VISITED = (255, 255, 255)
    BACKGROUND = (0, 0, 0)
    START = (36, 199, 14)
    END = (227, 14, 31)


@dataclass
class Node:
    coord: Coordinates
    size: int
    cost: float
    color: Colors
    wall: bool = True

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Node):
            return False
        return self.coord == __value.coord

    def __hash__(self) -> int:
        return hash(self.coord)
