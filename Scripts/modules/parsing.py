# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour but de récuperer les données et les mettres dans un format exploitable par l'application
Developpeur :
'''
import numpy as np
import csv
import pandas as pd
import os.path
import os

data_dir =  os.path.expanduser("..") + "/DataTirage"
pathDataCSV = data_dir + "/dataCSV"
pathFilesXLS = data_dir + "/dataXLS"

def setDataForTensorflow(annee_de_debut=2004,annee_de_fin=2005):
    resultat = np.matrix([[]],int)
    countTurnOne = 1
    for i in range(annee_de_debut, annee_de_fin + 1):
        with open(pathDataCSV + '/euromillions_' + str(i) + '.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:

                rowNumPy = np.matrix( [ [ int(row[1]), int(row[2]),int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7]) ] ] )

                if (countTurnOne==1):

                    resultat = np.concatenate((resultat, rowNumPy), axis=1)
                    countTurnOne+=1
                else:
                    resultat = np.concatenate((resultat, rowNumPy), axis=0)

    return resultat

# ----------------------------------------------------------------------------
# ---------------- Fonction de set des donnés pour keras ---------------------
# ----------------------------------------------------------------------------

def SetDataForKeras(date1=2004, date2=2005):
    # ---------------------------------------

    # chemin d'acces au fichier csv

    # -------------------------------
    # verification des dates, pour être sure qu'elles sont valables

    if (type(date1) != int):
        print("Date 1 need int")
        return
    if (type(date2) != int):
        print("Date 2 need int")
        return

    if (date1 > date2):
        ext = date1
        date1 = date2
        date2 = ext

    if (date1 < 2004):
        date1 = 2004
    # -------------------------------
    # on verifie que le dossier dataCSV existe vraiment pour eviter les problemes

    if (not os.path.isdir(pathDataCSV)):
        print("dossier avec csv non disponible")
        return

    # -------------------------------
    # on crée un tableau X dans lequel on stockera le contenus des différentes années

    X = np.array([], dtype=np.int64).reshape(0, 7)

    # -------------------------------
    # cette ligne nous permet de nous placer dans le dossier dataCSV, on a vérifié au prealable qu'il exister

    os.chdir(pathDataCSV)

    # -------------------------------

    # on traite maintenant chaque csv pour pouvoir recupérer ou non leur contenus

    for i in range(date1, date2 + 1):

        # creation des noms des fchiers csv avec la convention de nommage des fichiers csv

        document = "euromillions_" + str(i) + ".csv"

        # on verifie bien que chaque fichier csv existe avant de l'ouvrir

        if (os.path.isfile(document)):
            # le pandas.read_csv renvoie un dataframe,
            # qui avec l'option header=none lis bien tout les lignes du fichier
            # car sur nos donné n'ayant pas d'en tete on aurait pus lire une ligne de donnée en moins

            observations = pd.read_csv(document, header=None)

            # ici on choisis juste qu'elle collone du fichier nous allons sauvegarder dans notre tableau
            # par convention chaque ligne des fichiers csv commence par la date du tirage
            # nous avons donc gardé dans ce tableau la que les chiffres correspodnant au tirage

            Xtmp = observations[observations.columns[1:8]].values
            Xtmp = np.flip(Xtmp, 0)

            # dans cette dernière partie du code nous fusionnons simplement le tableau temporaire avec
            # le tableau dans lequel tous les resultats seront stocké à la fin

            X = np.vstack([X, Xtmp])

    # -------------------------------

    return X


SetDataForKeras()
# ---------------------------------------
# finfonction

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# pour utiliser cette fonction il suffide stocker le resultat dans un tableau
# et SetDataForKeras(2004,20XX) et d'appeller la fonction de cette manière
# exemple d'utilisations:

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
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
		tab = [0] * 62
		for i in range(50) :

		#Pour chaque tableau on initialise les valeurs à 0,


		#Ensuite on parcours pour chaque valeurs de 1 à 50  on check si la valeur i est presente dans le tirage
			for j in range(5) :

			# Si la valeur i appartient au tableau des tirages, alors on mets un 1
				if(i==Y[x][j]):
					tab[i-1]=1

		for i in range(51,62) :

	# on fait pareil mais avec les nombres des 2 derniers numéros
			#tab[i] = 0
			for j in range(5,7) :
				if(i==Y[x][j]):
					tab[i-1+50]=1

	# on ajoute le tableau tampon au tableau resultat
		#print(tab)
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
