import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        # Immediately kill itself and maybe we spawn more.
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            min_angle = 20
            max_angle = 50
            random_angle = random.uniform(min_angle, max_angle)
            first_spawn_angle = self.velocity.rotate(random_angle)
            second_spawn_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # spawn new asteroids
            first_spawn = Asteroid(self.position[0], self.position[1], new_radius)
            second_spawn = Asteroid(self.position[0], self.position[1], new_radius)

            first_spawn.velocity = first_spawn_angle * 1.2
            second_spawn.velocity = second_spawn_angle * 1.2