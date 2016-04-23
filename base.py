# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:00:15 2016

@author: KB
"""

#Importation des bibliothèques Pygame 
import pygame
import time
from pygame.locals import *
#from classes import *
from cst import *
from classes import *


#Initialisation
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((1344, 800))

fond = pygame.image.load(image_fond).convert()
pause = pygame.image.load(image_pause).convert()
accueil = pygame.image.load(image_accueil).convert()
persos = pygame.image.load(image_persos).convert()
monstres = pygame.image.load(image_monstres).convert()
game_over = pygame.image.load(image_fin).convert()
tache = pygame.image.load(image_tache).convert()

x1_perso = 32
y1_perso = 704

x1_monstre = 1280
y1_monstre = 64

actif = {K_s: False, K_w: False, K_a: False, K_d: False, K_UP: False, K_DOWN: False, K_RIGHT: False, K_LEFT: False}

menu = True
stop = False
jeu = False
reglages = False
p = False
m = False
tstop = 0
t0 = 0
t = 0
score = 0
recordp = 0
recordm = 1000
choix_perso = 0
choix_monstre = 0

myfont = pygame.font.SysFont("monospace", 16)

pygame.key.set_repeat(400, 100)

open = True
while open:

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
                    m = False
                if event.key == K_SEMICOLON :
                    reglages = True
                    m = True
                    p = False
                if event.key == K_ESCAPE :
                    pygame.quit()
                    quit()
                if event.key == K_RETURN :
                    menu = False
                    jeu = True
                    t0 = time.time()

	
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
                           

    while jeu == True :
    
        x2_perso = x1_perso + 32
        y2_perso = y1_perso + 32
        
        x2_monstre = x1_monstre + 32
        y2_monstre = y1_monstre + 32
        
        t = time.time() - t0
        
        perso = pygame.image.load(dossier + "p" +str(choix_perso) + extension1).convert_alpha()

        monstre = pygame.image.load(dossier + "m" + str(choix_monstre) + extension1).convert_alpha()
        monstreXL = pygame.image.load(dossier + "mXL" + str(choix_monstre) + extension1).convert_alpha()
        
        temps_display = myfont.render(str(t), 1, (56,180,0))
        
        #Positionnement des images sur l'écran
        print(t)
        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, (x1_perso, y1_perso))
        fenetre.blit(monstre,(x1_monstre, y1_monstre))
        fenetre.blit(temps_display, (672, 50))
    
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
                    
           
            if x2_monstre > 1344:
                x1_monstre = 0
            if x1_monstre < 0:
                x2_monstre = 1344
                x1_monstre = x2_monstre - 32
            
            if x2_perso > 1344:
                x1_perso = 0
            if x1_perso < 0:
                x2_perso = 1344
                x1_perso = x2_perso - 32
            
            if y2_perso > 800:
                y1_perso = 0
            if y1_perso < 0:
                y2_perso = 800 
                y1_perso = y2_perso - 32
                
            if y2_monstre > 800:
                y1_monstre = 0  
            if y1_monstre < 0:
                y2_monstre = 800
                y1_monstre = y2_monstre - 32
           
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                    open = 0      #On arrête la boucle
            
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    stop = True
                    t = time.time() - t0
                    tstop = t
                    while stop:
                        
                        fenetre.blit(pause,(378.5,200))
                     
                        #Rafraîchissement de l'image
                        pygame.display.flip()
                        
                        actif[event.key] = False
                        
                        if event.key == K_ESCAPE:
                                stop = False                            
                                pygame.quit()
                                quit()
                    
                        if event.key == K_RETURN:
                                                            
                                menu = True
                                jeu = False
                                stop = False
                                x1_perso = 32
                                y1_perso = 704
                                x1_monstre = 1280
                                y1_monstre = 64
                                
                    
                        if event.key == K_SPACE:
                                
                                tstop = t
                                fenetre.blit(temps_display, (672, 50))
                                fenetre.blit(fond, (0,0))
                                fenetre.blit(perso, (x1_perso, y1_perso))
                                fenetre.blit(monstre,(x1_monstre, y1_monstre))
                        
                                pygame.display.flip()
                                stop = False
                    
            
            #Re-collage
            
            fenetre.blit(fond,(0,0))	
            fenetre.blit(perso, (x1_perso, y1_perso))
            fenetre.blit(monstre, (x1_monstre, y1_monstre))
            #Rafraîchissement de l'image)            
            pygame.display.flip()
            #Limitation de vitesse de la boucle
            #30 frames par secondes suffisent
            pygame.time.Clock().tick(30)
    
        while x1_perso == x1_monstre and y1_perso == y1_monstre or -32 < x1_monstre-x1_perso < 32 and y1_perso == y1_monstre or -32 < y1_monstre-y1_perso < 32 and x1_perso == x1_monstre :
            
            score = t
            if score > recordp:
                recordp = score
                
            if score < recordm:
                recordm = score
            
            
            fenetre.blit(game_over,(0,0))
            fenetre.blit(monstreXL,(504,200))
            fenetre.blit(tache,(612,380))
            fenetre.blit(perso,(640.5,400))
            
            score_display = myfont.render(str(score), 1, (56,180,0))
            fenetre.blit(score_display, (576, 150))
            
            recordm_display = myfont.render("Record de l'ombre : " + str(recordm), 1, (56,180,0))
            fenetre.blit(recordm_display, (100, 180))
            
            recordp_display = myfont.render("Record du challenger : " + str(recordp), 1, (56,180,0))
            fenetre.blit(recordp_display, (832, 180))
            
            pygame.display.flip()
            pygame.display.flip()
        
            for event in pygame.event.get() :
                    if event.type == QUIT :
                            pygame.quit()
                            quit()
       
                    if event.type == KEYDOWN :
					
                            if event.key == K_ESCAPE :
                                pygame.quit()
                                quit()
                                
                            if event.key == K_RETURN :
                                menu = True
                                jeu = False
                                x1_perso = 32
                                y1_perso = 704
                                x1_monstre = 1280
                                y1_monstre = 64
                                
                            if event.key == K_SPACE :
                                x1_perso = 32
                                y1_perso = 704
                                x1_monstre = 1280
                                y1_monstre = 64
                                t0 = time.time()
