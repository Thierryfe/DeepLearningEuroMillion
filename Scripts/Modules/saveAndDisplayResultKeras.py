import numpy
import csv
import datetime

def saveAndDisplayResultKeras(Resultat_de_keras, nomFichier):
	#nomFichier = "resultat_keras.csv"

	"""
	On initialise le tableau avec les indices des 5 premieres valeurs et on le tri.
	On trie les indices par ordre croissant des valeurs du tableau.
	""" 
	tabIndice = [0,1,2,3,4]
	for i in range(5) :
		for j in range(i,4) :
			if Resultat_de_keras[tabIndice[j+1]] < Resultat_de_keras[tabIndice[j]] :
				aux = tabIndice[j+1]
				tabIndice[j+1] = tabIndice[j]
				tabIndice[j] = aux
 
	tabIndiceEtoile = [50,51]
	if Resultat_de_keras[tabIndiceEtoile[1]] < Resultat_de_keras[tabIndiceEtoile[0]] :
			aux = tabIndiceEtoile[1]
			tabIndiceEtoile[1] = tabIndiceEtoile[0]
			tabIndiceEtoile[0] = aux 

	"""
	Puisque le tableau tabIndice est trie par ordre croissant, l'indice de la plus petite valeur est en tabIndice[0]. Si on trouve une valeur de t qui est plus grande que t[tabIndice[0]], on met l'indice de cette valeur dans le tableau tabIndice et on retri le tableau. 
	"""

	for i in range(5,50) :
		if Resultat_de_keras[i] > Resultat_de_keras[tabIndice[0]] :
			tabIndice[0] = i
			for j in range(5) :
				for k in range(j,4) :
					if Resultat_de_keras[tabIndice[k+1]] < Resultat_de_keras[tabIndice[k]] :
						aux = tabIndice[k+1]
						tabIndice[k+1] = tabIndice[k]
						tabIndice[k] = aux

	for i in range(51,62) :
		if Resultat_de_keras[i] > Resultat_de_keras[tabIndiceEtoile[0]] :
			tabIndiceEtoile[0] = i
			if Resultat_de_keras[tabIndiceEtoile[1]] < Resultat_de_keras[tabIndiceEtoile[0]] :
				aux = tabIndiceEtoile[1]
				tabIndiceEtoile[1] = tabIndiceEtoile[0]
				tabIndiceEtoile[0] = aux
		

	"""
	Affichage des resultat dans le terminal., end = ''
	"""
	
	print("Les prochains numero a jouer sont : \n")
	for i in range(4) :
		print (str(tabIndice[i]+1) + ", ", end='')
	print(str(tabIndice[4]+1))
	print("Les numeros etoile sont : \n")
	print(str(tabIndiceEtoile[0]+1-50) + ", " + str(tabIndiceEtoile[1]+1-50))

	"""
	On enregistre les donnees dans un fichier CSV de la facons suivante :
	Les indices sont en colonne 1 et les probabilites en colonne 2
	"""
	date = datetime.datetime.now()
	with open(nomFichier, 'a') as csvfile:
		filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
		filewriter.writerow([date.year,date.month,date.day,date.hour,date.minute,date.second])
		filewriter.writerow(Resultat_de_keras)
