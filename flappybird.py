import pygame
from pygame.locals import *
from sys import exit 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 8
GRAVITY = 1

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.speed = SPEED

        imagem_original = pygame.image.load('Flappy-Bird-Pixel-Art-Transparent-Images.webp').convert_alpha()
        
        self.image = pygame.transform.scale(imagem_original, (108, 80))
        
        self.rect = self.image.get_rect()

        self.rect[0] = SCREEN_WIDTH / 3
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        self.rect[1] += self.speed
        self.speed += GRAVITY

    def bump(self):
        self.speed = -SPEED

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('flappy-bird-background-gecj5m4a9yhhjp87.jpg').convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0, 0))
    bird_group.update()
    bird_group.draw(screen)
    pygame.display.update()
