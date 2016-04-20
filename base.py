# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:00:15 2016

@author: KB
"""

#Importation des bibliothèques Pygame 
import pygame
from pygame.locals import *
#from classes import *
from cst import *

#PENSER A MODIFIER LES VALEURS POUR LA FENÊTRE ET AUTRES, EN 32 PAR 32

#Initialisation
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((1344, 800))

fond = pygame.image.load(image_fond).convert()
accueil = pygame.image.load(image_accueil).convert()
persos = pygame.image.load(image_persos).convert()
monstres = pygame.image.load(image_monstres).convert()

x1_perso = 32
y1_perso = 704
x2_perso = x1_perso + 32
y2_perso = y1_perso + 32

x1_monstre = 1280
y1_monstre = 64
x2_monstre = x1_monstre + 32
y2_monstre = y1_monstre + 32

actif = {K_s: False, K_w: False, K_a: False, K_d: False, K_UP: False, K_DOWN: False, K_RIGHT: False, K_LEFT: False}


pygame.key.set_repeat(400, 100)

open = True
while open:

    menu = True
    reglages = False
    p = False
    m = False
    choix_perso = 0
    choix_monstre = 0

    #penser à importer les variables de surface, la création, etc.
    while menu == True:
	 
      fenetre.blit(accueil, (0,0))
      pygame.display.flip()
      
      if choix_perso==0:
          choix_perso = 1
      if choix_monstre==0:
          choix_monstre = 1
      

      for event in pygame.event.get() :
          if event.type == QUIT :
                 pygame.quit()
                 quit()
          if event.type == KEYDOWN :
                if event.key == K_p :
                    reglages = True
                    p = True
                if event.key == K_SEMICOLON :
                    reglages = True
                    m = True
                if event.key == K_RETURN :
                    menu = False

	
      while reglages == True :
		
          if p == True :
                fenetre.blit(persos,(0,0))
                pygame.display.flip()
                for event in pygame.event.get() :
                    if event.type == QUIT :
                            pygame.quit()
                            quit()
				
                    if event.type == KEYDOWN :
			
                            if event.key == K_s :
                                choix_perso = 1
                                reglages = False
                            if event.key == K_q :
                                choix_perso = 2
                                reglages = False
                            if event.key == K_v :
                                choix_perso = 3
                                reglages = False
                            if event.key == K_u :
                                choix_perso = 4
                                reglages = False
                            if event.key == K_c :
                                choix_perso = 5
                                reglages = False
                            if event.key == K_ESCAPE :
                                reglages = False
                            else :
                                choix_perso = 1
          elif m == True :
                fenetre.blit(monstres,(0,0))
                pygame.display.flip()
                for event in pygame.event.get() :
                    if event.type == QUIT :
                            pygame.quit()
                            quit()
       
                    if event.type == KEYDOWN :
					
                            if event.key == K_b :
                                choix_monstre = 1
                                reglages = False
                            if event.key == K_z :
                                choix_monstre = 2
                                reglages = False
                            if event.key == K_w :
                                choix_monstre = 3
                                reglages = False
                            if event.key == K_SEMICOLON :
                                choix_monstre = 4
                                reglages = False
                            if event.key == K_c :
                                choix_monstre = 5
                                reglages = False
                            if event.key == K_l :
                                choix_monstre = 6
                                reglages = False
                            if event.key == K_ESCAPE :
                                reglages = False
                            else :
                                choix_monstre = 1

    perso = pygame.image.load(dossier + "p" +str(choix_perso) + extension1).convert_alpha()

    monstre = pygame.image.load(dossier + "m" + str(choix_monstre) + extension1).convert_alpha()
    
    
    #Positionnement des images sur l'écran
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (x1_perso, y1_perso))
    fenetre.blit(monstre,(x1_monstre, y1_monstre))
    
    #Rafraîchissement de l'image
    pygame.display.flip()
    
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
