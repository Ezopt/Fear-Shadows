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
fenetre = pygame.display.set_mode((840, 520))

#Image fond
fond = pygame.image.load("./Img_FS/back1.jpg").convert()
fenetre.blit(fond, (0,0))

depart = pygame.image.load("./Img_FS/depart.png").convert()
fenetre.blit(depart, (0,0))
            
perso = pygame.image.load("./Img_FS/chlgr.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)
            
monstre = pygame.image.load("./Img_FS/zigler.png").convert_alpha()
position_monstre = monstre.get_rect()
fenetre.blit(monstre, position_monstre)

#Rafraîchissement de l'image
pygame.display.flip()

pygame.key.set_repeat(400, 100)

open = True
while open:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            
            if event.type == KEYDOWN:
                
                    if event.key == K_s:	#Si "flèche bas"
                        #On descend le perso
                        position_perso = position_perso.move(0,40)
                    if event.key == K_w:	#Si "flèche haut"                       
                        #On monte le perso                        
                        position_perso = position_perso.move(0,-40)
                    if event.key == K_a:	#Si "flèche gauche"                       
                        #On va vers la gauche                                                
                        position_perso = position_perso.move(-40,0)
                    if event.key == K_d: #Si "flèche droite"                       
                        #On va vers la droite                                                                       
                        position_perso = position_perso.move(40,0)
                        
                    if event.key == K_DOWN:	#Si "flèche bas"
                        #On descend le monstre
                        position_monstre = position_monstre.move(0,40)
                    if event.key == K_UP:	#Si "flèche haut"
                        #On monte le monstre
                        position_monstre = position_monstre.move(0,-40)
                    if event.key == K_LEFT:	#Si "flèche gauche"                       
                        #On va vers la gauche                                                
                        position_monstre = position_monstre.move(-40,0)
                    if event.key == K_RIGHT: #Si "flèche droite"                       
                        #On va vers la droite                                  
                        position_monstre = position_monstre.move(40,0)
                    
           
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    open = 0      #On arrête la boucle
            
    #Re-collage
    fenetre.blit(fond,(0,0))	
    fenetre.blit(perso, position_perso)
    fenetre.blit(monstre, position_monstre)
    #Rafraîchissement de l'image)            
    pygame.display.flip()
    #Limitation de vitesse de la boucle
    #30 frames par secondes suffisent
    pygame.time.Clock().tick(30)
