import pygame as pg

from utils import Colors, Coordinates
from world import Labyrinth


class Canva:

    dimentions: Coordinates
    screen: pg.Surface
    window: pg.Surface

    def __init__(self, dimentions: Coordinates) -> None:
        pg.init()
        self.dimentions = dimentions
        self.window = pg.display.set_mode(dimentions)
        self.screen = pg.Surface(dimentions)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def draw(self, labyrinth: Labyrinth):
        self.screen.fill(Colors.VISITED.value)
        for node in labyrinth.world.values():
            pg.draw.rect(self.screen, node.color.value, (node.coord.x + 2,
                                                         node.coord.y + 2, node.size - 4, node.size - 4))
            pg.draw.rect(self.screen, (0, 0, 255),
                         (node.coord.x, node.coord.y, node.size, node.size), 2)
        self.window.blit(self.screen, (0, 0))
        pg.display.update()
