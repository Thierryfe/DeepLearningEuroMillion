import pandas as pnd
import numpy as np
#=============================================================
#=============================================================

# Cette Fonction à pour but de prendre un tableau de tirage pour keras, et d'en faire le tableau de reponse attendue
# utile pour pouvoir entrainer son reseau de neurone

def KerasSetResultat(Y):
#=====================================

	#on initialise le tableau des resulats ici
	tabresultat = []
#=====================================
	tab=[0]*62
	# On inialise le tableau tampon ici

#=====================================

	for x in range(1,len(Y)) :

	#Pour chaque sous tableau du tableau des tirages on crée un sous tableau tampon

		for i in range(50) :

		#Pour chaque tableau on initialise les valeurs à 0,
			tab[i] = 0

		#Ensuite on parcours pour chaque valeurs de 1 à 50  on check si la valeur i est presente dans le tirage
			for j in range(5) :

			# Si la valeur i appartient au tableau des tirages, alors on mets un 1

				if(i==Y[x][j]):
					tab[i-1]=1

		for i in range(50,62) :

	# on fait pareil mais avec les nombres des 2 derniers numéros

			tab[i] = 0
			for j in range(5,7) :
				if(i==Y[x][j]):
					tab[i-1]=1

	# on ajoute le tableau tampon au tableau resultat
		tabresultat.append(tab)

#=====================================

	# On le convertit au format Np array pour pouvoir l'utiliser nativement avec Keras

	tabresultat=np.asarray(tabresultat)

	# On retourne le nouveau ainsi construit

	return tabresultat;

#=====================================

#finfonction

#=============================================================
#=============================================================
