from random import choice


class map :
#j'importe les fichiers textes des maps, pour les transformer en liste ensuite pour pouvoir les parcourir. 
#Faudra définir la map choisie
	def__init__(self,fichier) : 
		self.fichier = map
		self.structure = 0
	def generer(self):
		with open(self.fichier, "r") as map:
		structureNiveau = []
		for ligne in map :
			ligneMap = []
			for sprite in ligne :
				if sprite != '\n'
					ligneMap.append(sprite)
			structureNiveau.append(ligneMap)
		self.structure = structureMap

 

def generationCaseMystere :
#je fais un tir au hasard d'un élément dans ma map/liste, si c'est un 1/mur, 
#alors il ne se passe rien, sinon, la case mystère apparaît 
	case = return choice(map)
	if case =! 1 :
		caseMystère = pygame.image.load("casemystère.jpg") in case #Je ne suis pas sûre de cette ligne
