import pandas as pd
import numpy as np
import os.path
import os

#----------------------------------------------------------------------------
#---------------- Fonction de set des donnés pour keras ---------------------
#----------------------------------------------------------------------------

def csvtotabforkeras(date1,date2):
#---------------------------------------

	#chemin d'acces au fichier csv

	pathData = os.path.expanduser("~") + "/Documents/DataTirage/dataCSV"
#-------------------------------
	#verification des dates, pour être sure qu'elles sont valables

	if(type(date1)!=int):
		print("Date 1 need int")
		return
	if(type(date2)!=int):
		print("Date 2 need int")
		return
	
	if(date1>date2):
		ext=date1
		date1=date2
		date2=ext

	if(date1<2004):
		date1=2004
#-------------------------------
	#on verifie que le dossier dataCSV existe vraiment pour eviter les problemes

	if (not os.path.isdir(pathData)):
		print("dossier avec csv non disponible")
		return

#-------------------------------
	#on crée un tableau X dans lequel on stockera le contenus des différentes années

	X = np.array([], dtype=np.int64).reshape(0,7)

#-------------------------------
	#cette ligne nous permet de nous placer dans le dossier dataCSV, on a vérifié au prealable qu'il exister

	os.chdir(pathData)

#-------------------------------

	#on traite maintenant chaque csv pour pouvoir recupérer ou non leur contenus

	for i in range(date1,date2+1):

		#creation des noms des fchiers csv avec la convention de nommage des fichiers csv

		document="euromillions_"+str(i)+".csv"

		#on verifie bien que chaque fichier csv existe avant de l'ouvrir

		if(os.path.isfile(document)):

			#le pandas.read_csv renvoie un dataframe, 
			#qui avec l'option header=none lis bien tout les lignes du fichier
			#car sur nos donné n'ayant pas d'en tete on aurait pus lire une ligne de donnée en moins

			observations = pd.read_csv(document,header=None)

			#ici on choisis juste qu'elle collone du fichier nous allons sauvegarder dans notre tableau
			#par convention chaque ligne des fichiers csv commence par la date du tirage
			#nous avons donc gardé dans ce tableau la que les chiffres correspodnant au tirage

			Xtmp = observations[observations.columns[1:8]].values

			#dans cette dernière partie du code nous fusionnons simplement le tableau temporaire avec 
			# le tableau dans lequel tous les resultats seront stocké à la fin

			X=np.vstack([X, Xtmp])

#-------------------------------

	return X
		
#---------------------------------------
#finfonction

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

#pour utiliser cette fonction il suffide stocker le resultat dans un tableau 
# et csvtotabforkeras(2004,20XX) et d'appeller la fonction de cette manière 
#exemple d'utilisations:


#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
