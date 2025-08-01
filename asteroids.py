import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(self, x, y, velocity)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", position, radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
