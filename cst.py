# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:01:21 2016

@author: KB
"""

#Listes des images du jeu
import pygame

dossier = "./Img_FS/"
extension1 = ".png"
extension2 = ".jpg"

image_accueil = dossier + "accueil" + extension1

image_fond = dossier + "back1" + extension2

image_mur = dossier + "mur" + extension1

image_persos = dossier + "persos" + extension1

image_monstres = dossier + "monstres" + extension1


#Paramètres de la fenêtre

nombre_sprite_cote = 25

taille_sprite = 42

cote_fenetre = nombre_sprite_cote * taille_sprite


#Personnalisation de la fenêtre

titre_fenetre = "Fear Shadows"
