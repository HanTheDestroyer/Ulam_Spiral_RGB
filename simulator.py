import pygame as pg
import numpy as np
import sys
import settings as st
import eratosthenes
import colorsys
import time


class Simulator:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(np.array(st.screen_size, dtype='int16'))
        self.screen.fill(pg.Color('black'))
        self.primes = eratosthenes.sieve_of_eratosthenes(100000)

        self.center = np.array([st.screen_size[0] / 2, st.screen_size[1] / 2])
        self.step_size = 5
        self.step = np.array([self.step_size, 0])
        self.number_counter = 0
        self.rotation_target = 1
        self.rotated = 0
        self.loop_counter = 2

        self.hue = 0
        self.hue_step = 0.0001

    def update(self):
        self.screen.fill(pg.Color('black'))
        time.sleep(5)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.logic()
            self.draw()
            pg.display.update()
            self.clock.tick()

    def draw(self):
        if self.loop_counter in self.primes:
            self.hue += self.hue_step
            if self.hue > 1:
                self.hue -= 1
            rgb = colorsys.hsv_to_rgb(self.hue, 1, 1)
            rgb = [int(c * 255) for c in rgb]
            pg.draw.circle(self.screen, color=rgb, center=self.center, radius=3)

        elif self.loop_counter not in self.primes:
            pg.draw.circle(self.screen, color=[120, 120, 120], center=self.center, radius=1)
            pass
        self.loop_counter += 1

    def logic(self):
        if self.rotated == 2:
            self.rotation_target += 1
            self.rotated = 0

        self.center += self.step
        self.number_counter += 1

        if self.number_counter == self.rotation_target:
            self.number_counter = 0
            self.rotated += 1
            if self.step[0] == self.step_size and self.step[1] == 0:
                self.step[0] = 0
                self.step[1] = -self.step_size
            elif self.step[0] == 0 and self.step[1] == -self.step_size:
                self.step[0] = -self.step_size
                self.step[1] = -0
            elif self.step[0] == -self.step_size and self.step[1] == 0:
                self.step[0] = 0
                self.step[1] = self.step_size
            elif self.step[0] == 0 and self.step[1] == self.step_size:
                self.step[0] = self.step_size
                self.step[1] = 0


if __name__ == '__main__':
    simulator = Simulator()
    simulator.update()
