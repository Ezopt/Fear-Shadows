# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#Importation des bibliothèques Pygame 
import pygame
from pygame.locals import *
#Initialisation
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((640, 480))

#Image fond
fond = pygame.image.load("./Img_FS/back1.jpg").convert()
fenetre.blit(fond, (0,0))
#Rafraîchissement de l'image
pygame.display.flip()


open = True
while open:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == KEYDOWN and event.key == K_SPACE:
            depart = pygame.image.load("./Img_FS/depart.png").convert()
            fenetre.blit(depart, (0,0))
            perso = pygame.image.load("./Img_FS/chlgr.png").convert_alpha()
            fenetre.blit(perso, depart.get_rect())
            #Rafraîchissement de l'image
            pygame.display.flip()
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            open = 0      #On arrête la boucle
