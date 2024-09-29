import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, player):
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.score += 1
            self.kill()
            return
        self.kill()
        player.score += 1
        random_angle = random.uniform(20, 50)
        rotate_1 = pygame.math.Vector2(self.velocity).rotate(random_angle)
        rotate_2 = pygame.math.Vector2(self.velocity).rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = rotate_1 * 1.2
        asteroid_2.velocity = rotate_2 * 1.2