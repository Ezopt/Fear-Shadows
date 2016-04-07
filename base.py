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

#PENSER A MODIFIER LES VALEURS POUR LA FENÊTRE ET AUTRES, EN 32 PAR 32

#Initialisation
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((1344, 800))

perso = pygame.image.load("./Img_FS/p"choix_perso".png").convert_alpha()

monstre = pygame.image.load("./Img_FS/m"choix_monstre".png").convert_alpha()

x1_perso = 32
y1_perso = 704
x2_perso = x1_perso + 32
y2_perso = y1_perso + 32

x1_monstre = 1280
y1_monstre = 64
x2_monstre = x1_monstre + 32
y2_monstre = y1_monstre + 32

actif = {K_s: False, K_w: False, K_a: False, K_d: False, K_UP: False, K_DOWN: False, K_RIGHT: False, K_LEFT: False}

#Positionnement des images sur l'écran
fenetre.blit(fond, (0,0))
fenetre.blit(perso, (x1_perso, y1_perso))
fenetre.blit(monstre,(x1_monstre, y1_monstre))

#Rafraîchissement de l'image
pygame.display.flip()

pygame.key.set_repeat(400, 100)

open = True
while open:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            
            if event.type == KEYDOWN:
                actif[event.key] = True
            elif event.type == KEYUP:
                actif[event.key] = False              
                
            if actif[K_s]:	#Si "flèche bas"
                #On descend le perso
                y1_perso = y1_perso + 32
            if actif[K_w]:	#Si "flèche haut"                       
                #On monte le perso
                y1_perso = y1_perso - 32
            if actif[K_a]:	#Si "flèche gauche"                       
                #On va vers la gauche
                x1_perso = x1_perso - 32
            if actif[K_d]: #Si "flèche droite"                       
                #On va vers la droite
                x1_perso = x1_perso + 32
                
            if actif[K_DOWN]:	#Si "flèche bas"
                #On descend le monstre
                y1_monstre = y1_monstre + 32
            if actif[K_UP]:	#Si "flèche haut"
                #On monte le monstre
                y1_monstre = y1_monstre - 32
            if actif[K_LEFT]:	#Si "flèche gauche"                       
                #On va vers la gauche
                x1_monstre = x1_monstre - 32
            if actif[K_RIGHT]: #Si "flèche droite"                       
                #On va vers la droite                                  
                x1_monstre = x1_monstre + 32
                    
           
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    open = 0      #On arrête la boucle
            
    #Re-collage
    fenetre.blit(fond,(0,0))	
    fenetre.blit(perso, (x1_perso, y1_perso))
    fenetre.blit(monstre, (x1_monstre, y1_monstre))
    #Rafraîchissement de l'image)            
    pygame.display.flip()
    #Limitation de vitesse de la boucle
    #30 frames par secondes suffisent
    pygame.time.Clock().tick(30)
