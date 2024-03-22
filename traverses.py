
from collections import deque
from canva import Canva
from utils import Colors, Coordinates, Node
from world import Labyrinth


class Traverses:

    world: Labyrinth
    canva: Canva
    start_node: Node
    end_node: Node

    def __init__(self, world: Labyrinth, canva: Canva, start: Coordinates, end: Coordinates) -> None:
        self.world = world
        self.canva = canva
        self.start_node = self.world.get_node(start)
        self.end_node = self.world.get_node(end)
        self.start_node.color = Colors.START
        self.end_node.color = Colors.END

    def dfs(self):
        visited: list[Node] = []
        before: dict[Node, Node | None] = {}
        to_visit: deque[Node] = deque()
        to_visit.append(self.start_node)
        came_from = None

        while len(to_visit) > 0:
            current = to_visit.pop()
            current.color = Colors.VISITED

            visited.append(current)
            before[current] = came_from

            if current == self.end_node:
                return self.find_path(current, before)

            for neighbor in self.world.get_neighbors(current.coord):
                if neighbor.color != Colors.NOT_VISITED:
                    continue

                neighbor.color = Colors.TO_VISIT
                to_visit.append(neighbor)

            self.canva.draw(self.world)
            came_from = current

    def _dfs_recursive(self, visited: list[Node],
                       before: dict[Node, Node | None],
                       to_visit: deque[Node], came_from: Node | None = None) -> list[Node]:
        current = to_visit.pop()
        current.color = Colors.VISITED

        visited.append(current)
        before[current] = came_from

        if current == self.end_node:
            return self.find_path(current, before)

        for neighbor in self.world.get_neighbors(current.coord):
            neighbor.color = Colors.TO_VISIT
            to_visit.append(neighbor)

        self.canva.draw(self.world)
        return self._dfs_recursive(visited, before, to_visit, current)

    def find_path(self, node: Node, before: dict[Node, Node | None]) -> list[Node]:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = before[current]
        path.sort(reverse=True)
        return path
