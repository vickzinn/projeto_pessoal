import pygame, random
from pygame.locals import *
from sys import exit 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
SPEED = 8
GRAVITY = 1
GAMESPEED = 10
GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGTH = 100
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
PIPE_GAP = 200

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.speed = SPEED

        imagem_original = pygame.image.load('Flappy-Bird-Pixel-Art-Transparent-Images.webp').convert_alpha()
        
        self.image = pygame.transform.scale(imagem_original, (108, 80))
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image, 127)

        self.rect[0] = SCREEN_WIDTH / 3
        self.rect[1] = SCREEN_HEIGHT / 2

    def update(self):
        # update heigth
        self.rect[1] += self.speed
        self.speed += GRAVITY

    def bump(self):
        self.speed = -SPEED

class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('203-2032468_8-bit-mario-pipe-hd-png-download.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = -(self.rect[3] - ysize)
        else:
            self.rect[1] = SCREEN_HEIGHT - ysize

        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect[0] -= GAMESPEED


class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('0a369167f640e62.webp').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGTH))
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image, 127)

        self.rect[0] = xpos
        self.rect[1] = SCREEN_HEIGHT - GROUND_HEIGTH

    def update(self):
        self.rect[0] -= GAMESPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_pipes(xpos):
    size = random.randint(100, 300)
    pipe = Pipe(False, xpos, size)
    pipe_inv = Pipe(True, xpos, SCREEN_HEIGHT - size - PIPE_GAP)
    return (pipe, pipe_inv)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('mr2h2imr2h2imr2h.png').convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(3):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

groupipe = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(SCREEN_WIDTH * i + 600)
    groupipe.add(pipes[0])
    groupipe.add(pipes[1])


clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0, 0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(GROUND_WIDTH - 15)
        ground_group.add(new_ground)

    if is_off_screen(groupipe.sprites()[0]):
        groupipe.remove(groupipe.sprites()[0])
        groupipe.remove(groupipe.sprites()[0])

        pipes = get_random_pipes(SCREEN_WIDTH * 2)
        groupipe.add(pipes[0])
        groupipe.add(pipes[1])


    bird_group.update()
    ground_group.update()
    groupipe.update()

    bird_group.draw(screen)
    groupipe.draw(screen)
    ground_group.draw(screen)

    if (pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(bird_group, groupipe, False, False, pygame.sprite.collide_mask)):
        break
    
    pygame.display.update()