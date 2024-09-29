from os import kill
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.handle_input()
        for updatable_object in updatable:
            updatable_object.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print(f"Game over! Your Score: {player.score}")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split(player)
        screen.fill((0, 0, 0))
        for drawable_object in drawable:
            drawable_object.draw(screen)
        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Position is (10, 10) for top-left corner
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()