import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Gemini_Generated_Image_6zkm0p6zkm0p6zkm.png').convert_alpha()
        self.rect = self.image.get_rect()
        print(self.rect)
    def update(self):
        pass

pygame.init()
screen = pygame.display.set_mode((1280, 720))

BACKGROUND = pygame.image.load('flappy-bird-background-gecj5m4a9yhhjp87.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (1280, 720))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

while True:
    for event in pygame.event.get():
        if event.type == quit:
            pygame.quit()

    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()
    bird_group.draw(screen)

    pygame.display.update()