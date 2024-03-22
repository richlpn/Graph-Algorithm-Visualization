# TODO: Implement a function that returns a matrix of size N x M
# TODO: Select a random start and End point
# TODO: Randomly implement walls on the matrix

from random import choice

from utils import Coordinates, Node


class Labyrinth:
    world: dict[Coordinates, Node]
    world_coords: Coordinates

    def __init__(self, size: int, world_max_coords: Coordinates) -> None:
        self.world = {}
        self.world_coords = world_max_coords
        self._init_world(size)

    def _init_world(self, size: int):

        for y in range(0, self.world_coords.y, size):
            for x in range(0, self.world_coords.x, size):
                node_coord = Coordinates(x, y)
                self.world[node_coord] = Node(
                    node_coord, size, 0, choice([False, True]))

    def get_node(self, coord: Coordinates) -> Node:
        """Returns the node at the given coordinate
        :param coord coordinate of the desired node
        :return Returns the node at the informed coordinate
        :raises Raises KeyError if the coordinate does not exists
        """
        return self.world[coord]
