import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0
        

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('#000000')

        for entity in drawable:
            entity.draw(screen)
            
        pygame.display.flip()
        deltaTime = clock.tick(60)
        dt = deltaTime / 1000

        updatable.update(dt)

        for asteroid in asteroids:
            if player.isColliding(asteroid):
                print("Game over!")
                sys.exit()
            
            for bullet in shots:
                if bullet.isColliding(asteroid):
                    bullet.kill()
                    asteroid.split()

if __name__ == "__main__":
    main()