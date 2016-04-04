# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#Importation des bibliothèques Pygame 
import pygame
from pygame.locals import *
from menu import *
from classes import *
from cst import *


#Initialisation
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((840, 520))

#Image fond
fond = pygame.image.load("./Img_FS/back1.jpg").convert()
fenetre.blit(fond, (0,0))
            
perso = pygame.image.load("./Img_FS/chlgr.png").convert_alpha()
x_perso = 0
y_perso = 0
fenetre.blit(perso, (x_perso, y_perso))
            
monstre = pygame.image.load("./Img_FS/zigler.png").convert_alpha()
x_monstre = 0
y_monstre = 0
fenetre.blit(monstre,(x_monstre, y_monstre))

#Rafraîchissement de l'image
pygame.display.flip()

pygame.key.set_repeat(400, 100)
actif = {K_s: False, K_w: False, K_a: False, K_d: False, K_UP: False, K_DOWN: False, K_RIGHT: False, K_LEFT: False}

open = True
while open:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            
            if event.type == KEYDOWN:
                actif[event.key] = True
            elif event.type == KEYUP:
                actif[event.key] = False              
                
            if actif[K_s]:	#Si "flèche bas"
                #On descend le perso
                y_perso = y_perso + 40
            if actif[K_w]:	#Si "flèche haut"                       
                #On monte le perso
                y_perso = y_perso - 40
            if actif[K_a]:	#Si "flèche gauche"                       
                #On va vers la gauche
                x_perso = x_perso - 40
            if actif[K_d]: #Si "flèche droite"                       
                #On va vers la droite
                x_perso = x_perso + 40
                
            if actif[K_DOWN]:	#Si "flèche bas"
                #On descend le monstre
                y_monstre = y_monstre + 40
            if actif[K_UP]:	#Si "flèche haut"
                #On monte le monstre
                y_monstre = y_monstre - 40
            if actif[K_LEFT]:	#Si "flèche gauche"                       
                #On va vers la gauche
                x_monstre = x_monstre - 40
            if actif[K_RIGHT]: #Si "flèche droite"                       
                #On va vers la droite                                  
                x_monstre = x_monstre + 40
                    
           
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    open = 0      #On arrête la boucle
            
    #Re-collage
    fenetre.blit(fond,(0,0))	
    fenetre.blit(perso, (x_perso, y_perso))
    fenetre.blit(monstre, (x_monstre, y_monstre))
    #Rafraîchissement de l'image)            
    pygame.display.flip()
    #Limitation de vitesse de la boucle
    #30 frames par secondes suffisent
    pygame.time.Clock().tick(30)
