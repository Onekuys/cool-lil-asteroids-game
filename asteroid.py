from logger import log_event
from random import uniform
import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt): 
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        log_event("asteroid_split")
        degree = uniform(20, 50)

        first_movement = self.velocity.rotate(degree)
        second_movement = self.velocity.rotate(-degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = first_movement * 1.2
        second_asteroid.velocity = second_movement * 1.2