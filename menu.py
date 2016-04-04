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
			if event.key = K_ENTER :
				fonction_jeu.fearshadows
		if event.type == QUIT
			pygame.quit()
			quit()
