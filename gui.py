import pygame as p

from enums.colors import Colors


def init_gui(dimensions, surface, init_cooridinates):
    p.init()
    p.display.set_caption('Reinforcment learning')

    for row in range(dimensions[0]):
        for col in range(dimensions[1]):
            p.draw.rect(surface, Colors.WHITE.value, p.Rect(row * 101, col * 101, 99, 99))

    reset_gui(dimensions, surface, init_cooridinates)


def reset_gui(dimensions, surface, init_cooridinates):
    p.draw.rect(surface, Colors.GOLD.value, p.Rect((dimensions[0] - 1) * 101, (dimensions[1] - 1) * 101, 99, 99))
    p.draw.rect(surface, Colors.RED.value, p.Rect(init_cooridinates[0], init_cooridinates[1], 99, 99))
    p.display.flip()


def color_rectangle(color, coordinates, surface):
    p.draw.rect(surface, color, p.Rect(coordinates[0] * 101, coordinates[1] * 101, 99, 99))
    p.display.flip()
