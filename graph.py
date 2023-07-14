import pygame as pg
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

sc = pg.display.set_mode((300, 200))


pg.draw.line(sc, WHITE, 
                 [10, 30], 
                 [290, 15], 3)

# здесь будут рисоваться фигуры
 
pg.display.update()
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)
