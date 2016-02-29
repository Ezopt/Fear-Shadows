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
            perso_x = 0
            perso_y = 0
            depart = pygame.image.load("./Img_FS/depart.png").convert()
            fenetre.blit(depart, (0,0))
            perso = pygame.image.load("./Img_FS/chlgr.png").convert_alpha()
            fenetre.blit(perso, (perso_x, perso_y))
            #Rafraîchissement de l'image
            pygame.display.flip()
            while event.type == KEYDOWN:
                
                    if event.key == K_LEFT and perso_x >= 0 and perso_x <= 640:
                        perso_x = perso_x - 40
                    else:
                        perso_x = perso_x
                    if event.key == K_RIGHT and perso_x >= 0 and perso_x <= 640:
                        perso_x = perso_x + 40
                    else:
                        perso_x = perso_x
                    if event.key == K_UP and perso_y >= 0 and perso_y <= 480:
                        perso_y = perso_y - 40
                    else:
                        perso_y = perso_y
                    if event.key == K_DOWN and perso_y >= 0 and perso_y <= 480:
                        perso_y = perso_y + 40
                    else:
                        perso_y = perso_y
            
                    fenetre.blit(perso, (perso_x, perso_y))
                    #Rafraîchissement de l'image)            
                    pygame.display.flip()
                    #Limitation de vitesse de la boucle
                    #30 frames par secondes suffisent
                    pygame.time.Clock().tick(30)

            
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                open = 0      #On arrête la boucle
