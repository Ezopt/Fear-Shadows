from random import choice
#c'est pour choisir l'élément au hasard dans la liste


class map :
#j'importe les fichiers textes des maps, pour les transformer en liste ensuite pour pouvoir les parcourir. 
#Faudra définir la map choisie
	def__init__(self,fichier) : 
		self.fichier = map
		self.structure = 0
	def generer(self):
		with open(self.fichier, "r") as map:  #with permet de refermer le fichier dès qu'on s'en sert plus dans la fonction
		structureNiveau = []  #liste vide au départ
		for ligne in map :
			ligneMap = []
			for sprite in ligne :
				if sprite != '\n'
					ligneMap.append(sprite)
			structureNiveau.append(ligneMap)
		self.structure = structureMap
		
	def afficher(self, fenetre)
#Donc, ça c'est pour afficher la map en fonction de la liste, 
#en gros si c'est 1 on affiche un mur et si c'est 0, le chemin
		numLigne = 0
		for ligne in self.structure:
			numCase = 0
			for sprite in ligne :
			x = numCase * 32
			y = numLigne * 32
			if sprite == 1
				fenetre.blit(mur, (x,y))
			elif sprite =! 1 :
				fenetre.blit(sol, (x,y))
			numCase = numCase +1
		numLigne = numLigne +1

 

def generationCaseMystere :
#je fais un tir au hasard d'un élément dans ma map/liste, si c'est un 1/mur, 
#alors il ne se passe rien, sinon, la case mystère apparaît 
	case = return choice(map)
	if case =! 1 :
		fenetre.blit(mystere, (case))  #Je ne suis pas sûre de cette ligne
