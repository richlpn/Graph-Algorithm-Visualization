from canva import Canva
from traverses import Traverses
from utils import Coordinates
from world import Labyrinth

DIMENTIONS = Coordinates(400, 400)
SIZE = 20

labyrinth = Labyrinth(SIZE, DIMENTIONS)
canva = Canva(DIMENTIONS)

start, end = Coordinates(0, 0), Coordinates(
    DIMENTIONS.x - SIZE, DIMENTIONS.y - SIZE)
traverser = Traverses(labyrinth, canva, start, end)

canva.draw(labyrinth)
traverser.dfs()
