import pygame
import sys
from pygame.locals import *
from random import randint
from Products import *
import time
from Director import *
from Moves import *
from RMoves import *
import loadImages
from score import *


class Game():
    
    i=0
    width = 900
    height = 600
    colour = (227,166,162)
    empezar = True
    Gaticornio = rightGaticornio()
    auxlist = Gaticornio.get_sprites()
    

    pygame.init()                
    posX=100
    posY=320
    posTup = (posX,posY)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Prueba")
    speed=20
    auxDirector = Director()
    auxDirector.setBuilder(GaticornioMoves())
    charac= auxDirector.getChar()
    charac.defPositions(posX,posY)
    jugando =True
    background = loadImages.load("background/espace.jpg")
    segundos = 0
    pygame.mixer.music.load('Ragnarok.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()



    while empezar:
        for i in pygame.event.get():

            if i.type == QUIT:
                score.main(segundos)
                pygame.quit()
                empezar = False
                sys.exit()
            elif i.type == pygame.constants.USEREVENT:

                pygame.mixer.music.load('Ragnarok.mp3')
                pygame.mixer.music.play()


        screen.blit(background,(0,0))

        charac.update()

        charac.drawCharacter(screen)
        charac.drawCaida(screen)

        pygame.display.update()
        empezar = charac.colisiones()






        segundos += 0.06




        
         
        
        
        




