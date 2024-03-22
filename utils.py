"""Utility classes to support the project"""
from dataclasses import dataclass
from typing import NamedTuple


class Coordinates(NamedTuple):
    x: int
    y: int


@dataclass
class Node:
    coord: Coordinates
    size: int
    cost: float
    wall: bool = True

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Node):
            return False
        return self.coord == __value.coord
