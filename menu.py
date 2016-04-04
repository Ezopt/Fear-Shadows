#importation de la fonction jeu, et des autres variables depuis la base
import pygame
from pygame import *
from classes import *
from cst import *
from base import *

pygame.init()

#penser à importer les variables de surface, la création, etc.
while True:
	fond.blit(accueil,(0,0))
	pygame.display.flip()
	
	for event in pygame.event.get() :
		if event.type == KEYDOWN :
			if event.key == K_p :
				fond.blit(persos,(0,0))
				if event.key == K_s :
					choix_perso = 1
				if event.key == K_a :
					choix_perso = 2
				if event.key == K_v :
					choix_perso = 3
				if event.key == K_u :
					choix_perso = 4
				if event.key == K_c :
					choix_perso = 5
				else :
					choix_perso = 1
			if event.key == K_m :
				fond.blit(monstres,(0,0))
				if event.key == K_b :
					choix_monstre = 1
				if event.key == K_w :
					choix_monstre = 2
				if event.key == K_z :
					choix_monstre = 3
				if event.key == K_m :
					choix_monstre = 4
				if event.key == K_c :
					choix_monstre = 5
				if event.key == K_l :
					choix_monstre = 6
				else :
					choix_perso = 1
				
			if event.key == K_ENTER :
				fonction_jeu.fearshadows
		if event.type == QUIT
			pygame.quit()
			quit()
