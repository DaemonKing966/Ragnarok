from random import random, randint

import pygame
from pygame.sprite import Sprite
from pygame import*
import time


class Character(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.direction = 1
        self.cont = 0
        self.speed = randint(10,30)
        self.movementLeft = True
        self.movementRight = True
        self.posc = randint(0, 650)
        self.pos = 0

    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY
    def set_sprites(self, images):
        self.graphics = images
        self.image = self.graphics[self.direction][self.cont]


    def moveRight(self):
        if self.movementRight:
            pressed = pygame.key.get_pressed()
            if pressed[K_RIGHT]:
                self.posX += self.speed
                time.sleep(0.06)
                self.direction = 1

    def moveLeft(self):
        if self.movementLeft:
            pressed = pygame.key.get_pressed()
            if pressed[K_LEFT]:
                self.posX -= self.speed
                time.sleep(0.06)
                self.direction = 0

    


    def changeSprite(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_RIGHT] or pressed[K_LEFT]:
            try:
                self.image = self.graphics[self.direction][self.cont]
                self.cont += 1
                self.cont %= len(self.graphics[self.direction])

            except IndexError:
                self.cont = 0
            if self.posX < 0:
                self.movementLeft = False
                self.direction = 0
                try:
                    self.image = self.graphics[self.direction][self.cont]
                    self.cont += 0
                    self.cont %= len(self.graphics[self.direction])
                except:
                    print()
            else:
                self.movementLeft = True

            if self.posX > 650:
                self.movementRight = False
                try:
                    self.image = self.graphics[self.direction][self.cont]
                    self.cont += 1
                    self.cont %= len(self.graphics[self.direction])
                except:
                    print()
            else:
                self.movementRight = True
        else:
            self.cont = 0
            self.image = self.graphics[self.direction][0]


    def update(self):

        self.moveRight()
        self.moveLeft()
        self.changeSprite()
        self.moveCaida()




    def moveCaida(self):

        self.pos += 20
        time.sleep(0.06)
        if self.pos>450:
            self.pos=0
            self.posc=randint(0, 650)

    def drawCharacter(self, screen):
        screen.blit(self.image, (self.posX, self.posY))

    def drawCaida(self,screen):
        for j in range(1, 10, 1):
            self.imagei = self.graphics[2][0]
            screen.blit(self.imagei, (self.posc, self.pos))
    def colisiones(self):
        rec1 = self.image.get_rect()
        rec2=self.imagei.get_rect()
        if rec1.colliderect(rec2):
            return False
        else:
            return True



