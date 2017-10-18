#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
import math

DIMENSION_X = 600
DIMENSION_Y = 400
Y = 200
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
BLUE = (0, 0, 250)
RED = (250, 0, 0)

iniPos = 50  # Posición inicial de la partícula
VP = 1e10  # Velocidad de la partícula
intervalo = 1  # Cada cuántos segundos se graficarán las ondas


# Default variables:
refindex1 = 1.1 		# Refraction index 1
refindex2 = 1.1 		# Refraction index 1
col1 = (255, 229, 204)  # Color 1
col2 = (255, 255, 204)  # Color 1
c = 3 					# Light's speed in void
v = (0.9999) * c 		# Particle's speed in a medium

tetha = math.acos(c / (v * refindex1))  # Ángulo de emisión


# Initialize window size and title:
pygame.init()
window = pygame.display.set_mode((DIMENSION_X, DIMENSION_Y))
pygame.display.set_caption("Animación efecto Cerenkov")
# Fill background
background = pygame.Surface(window.get_size())
background = background.convert()


def blueRay(origin, time, xp, rads, v):
    x = v * time * math.cos(tetha)
    x = x + origin
    y = v * time * math.sin(tetha)
    y = y + Y
    au = 2 * (y - Y)
    y = y - au
    pygame.draw.line(window, BLUE, [origin, Y], [int(x), int(y)], 2)
    pygame.draw.line(window, RED, [int(x), int(y)], [xp, Y], 2)


def moveParticle(initx, posx, posy, color, r, surface, background_col, trace_width, trace_col, rads, vl):
    surface.fill(background_col)
    pygame.draw.line(surface, trace_col, (initx, posy),
                     (posx, posy), trace_width)
    n = len(rads)
    for i in range(n):
        if posx >= rads[i][0]:
            pygame.draw.circle(window, trace_col, (rads[i][0], posy), int(
                v * rads[i][1]) + 1, trace_width)
            # blueRay(rads[i][0], rads[i][1], posx, rads, vl)
            rads[i][1] += c / refindex1 * 0.1
    pygame.draw.circle(surface, color, (posx, posy), r)
    pygame.display.update()


rads = [[i, 0] for i in range(1000) if i % 50 == 0]

# Main:


def main():
    x = 0
    initx = x
    while True:
        # Fill background:
        window.blit(background, (0, 0))
        moveParticle(initx, int(x), Y, RED, 3, window,
                     WHITE, 1, (22, 44, 66), rads, v)
        x += 1.0
        # Check events on window:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    pygame.quit()
                    sys.exit()

        # Update window:
        pygame.display.update()


if __name__ == '__main__':
    main()
