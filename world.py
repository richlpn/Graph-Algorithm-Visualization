
from random import choice

from utils import Colors, Coordinates, Node


class Labyrinth:
    world: dict[Coordinates, Node]
    world_coords: Coordinates
    size: int

    def __init__(self, size: int, world_max_coords: Coordinates) -> None:
        self.world = {}
        self.world_coords = world_max_coords
        self.size = size
        self._init_world()

    def _init_world(self):

        for y in range(0, self.world_coords.y, self.size):
            for x in range(0, self.world_coords.x, self.size):

                node_coord = Coordinates(x, y)
                is_wall = choice([False, True, False, False])
                color = Colors.WALL if is_wall else Colors.NOT_VISITED

                self.world[node_coord] = Node(
                    node_coord, self.size, 0, color, is_wall)

    def get_node(self, coord: Coordinates) -> Node:
        """Returns the node at the given coordinate
        :param coord coordinate of the desired node
        :return Returns the node at the informed coordinate
        :raises Raises KeyError if the coordinate does not exists
        """
        return self.world[coord]

    def is_coord_valid(self, coord: Coordinates) -> bool:
        return (
            (coord.x < self.world_coords.x) and
            (coord.y < self.world_coords.y) and
            (coord.x >= 0) and
            (coord.y >= 0)
        )

    def get_neighbors(self, coord: Coordinates) -> list[Node]:
        mask = [
            Coordinates(coord.x - self.size, coord.y),
            Coordinates(coord.x + self.size, coord.y),
            Coordinates(coord.x, coord.y - self.size),
            Coordinates(coord.x, coord.y + self.size),
        ]

        neighbors = []
        for neighbor_coord in mask:

            if self.is_coord_valid(neighbor_coord):
                node = self.get_node(neighbor_coord)
                if not node.wall:
                    neighbors.append(node)

        return neighbors
