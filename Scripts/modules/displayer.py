# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif d'interpreter les résultats obtenus par les moteurs
Developpeur :
'''

import numpy
import csv
import datetime


# =======================================================================================================================
# ====================================== saveAndDisplayResultKeras ==================================================
# =======================================================================================================================

def saveAndDisplayResultKeras(Resultat_de_keras, nomFichier):
    # nomFichier = "resultat_keras.csv"

    """
    On initialise le tableau avec les indices des 5 premieres valeurs et on le tri.
    On trie les indices par ordre croissant des valeurs du tableau.
    """
    tabIndice = [0, 1, 2, 3, 4]
    for i in range(5):
        for j in range(i, 4):
            if Resultat_de_keras[tabIndice[j + 1]] < Resultat_de_keras[tabIndice[j]]:
                aux = tabIndice[j + 1]
                tabIndice[j + 1] = tabIndice[j]
                tabIndice[j] = aux

    tabIndiceEtoile = [50, 51]
    if Resultat_de_keras[tabIndiceEtoile[1]] < Resultat_de_keras[tabIndiceEtoile[0]]:
        aux = tabIndiceEtoile[1]
        tabIndiceEtoile[1] = tabIndiceEtoile[0]
        tabIndiceEtoile[0] = aux

    """
    Puisque le tableau tabIndice est trie par ordre croissant, l'indice de la plus petite valeur est en tabIndice[0]. Si on trouve une valeur de t qui est plus grande que t[tabIndice[0]], on met l'indice de cette valeur dans le tableau tabIndice et on retri le tableau. 
    """

    for i in range(5, 50):
        if Resultat_de_keras[i] > Resultat_de_keras[tabIndice[0]]:
            tabIndice[0] = i
            for j in range(5):
                for k in range(j, 4):
                    if Resultat_de_keras[tabIndice[k + 1]] < Resultat_de_keras[tabIndice[k]]:
                        aux = tabIndice[k + 1]
                        tabIndice[k + 1] = tabIndice[k]
                        tabIndice[k] = aux

    for i in range(51, 62):
        if Resultat_de_keras[i] > Resultat_de_keras[tabIndiceEtoile[0]]:
            tabIndiceEtoile[0] = i
            if Resultat_de_keras[tabIndiceEtoile[1]] < Resultat_de_keras[tabIndiceEtoile[0]]:
                aux = tabIndiceEtoile[1]
                tabIndiceEtoile[1] = tabIndiceEtoile[0]
                tabIndiceEtoile[0] = aux

    """
    Affichage des resultat dans le terminal., end = ''
    """

    print("Les prochains numero a jouer sont : \n")
    for i in range(4):
        print(str(tabIndice[i] + 1) + ", ", end='')
    print(str(tabIndice[4] + 1))
    print("Les numeros etoile sont : \n")
    print(str(tabIndiceEtoile[0] + 1 - 50) + ", " + str(tabIndiceEtoile[1] + 1 - 50))

    """
    On enregistre les donnees dans un fichier CSV de la facons suivante :
    Les indices sont en colonne 1 et les probabilites en colonne 2
    """
    date = datetime.datetime.now()
    with open(nomFichier, 'a') as csvfile:
        filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        filewriter.writerow([date.year, date.month, date.day, date.hour, date.minute, date.second])
        filewriter.writerow(Resultat_de_keras)


# =======================================================================================================================
# ====================================== saveAndDisplayResultKerasRnn ==================================================
# =======================================================================================================================

def saveAndDisplayResultKerasRnn(Resultat_de_keras, nomFichier):
    # nomFichier = "resultat_keras.csv"

    """
    On sépare les valeurs de chaque prédiction
    On met les 5 numéros normaux dans le premier et le deuxieme sers à stocker les numéros étoiles
    On les remets en format d'entier pour avoir un affichage propre
    """
    tabIndice = [0, 1, 2, 3, 4]
    for i in range(5):
        if (Resultat_de_keras[i] <= 49):
            tabIndice[i] = int(Resultat_de_keras[i])
        else:
            tabIndice[i] = 49

    tabIndiceEtoile = [5, 6]
    for i in range(2):
        tabIndiceEtoile[i] = int(Resultat_de_keras[i + 5])

    print("Les prochains numero a jouer sont : \n")
    for i in range(4):
        print(str(tabIndice[i] + 1) + ", ", end='')
    print(str(tabIndice[4] + 1))
    print("Les numeros etoile sont : \n")
    print(str(tabIndiceEtoile[0]) + ", " + str(tabIndiceEtoile[1]))

    """
    On enregistre les donnees dans un fichier CSV de la facons suivante :
    Les indices sont en colonne 1 et les probabilites en colonne 2
    """
    date = datetime.datetime.now()
    with open(nomFichier, 'a') as csvfile:
        filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        filewriter.writerow([date.year, date.month, date.day, date.hour, date.minute, date.second])
        filewriter.writerow(Resultat_de_keras)


# =======================================================================================================================
# ====================================== saveAndDisplayResultTensorlow ==================================================
# =======================================================================================================================

def saveAndDisplayResultTensorlow(Resultat_de_Tensorlow, nomFichier):
    # nomFichier = "resultat_Tensorlow.csv"

    """
    On initialise le tableau avec les indices des 5 premieres valeurs et on le tri.
    On trie les indices par ordre croissant des valeurs du tableau.
    """
    tabIndice = [0, 1, 2, 3, 4]
    for i in range(5):
        for j in range(i, 4):
            if Resultat_de_Tensorlow[tabIndice[j + 1]] < Resultat_de_Tensorlow[tabIndice[j]]:
                aux = tabIndice[j + 1]
                tabIndice[j + 1] = tabIndice[j]
                tabIndice[j] = aux

    tabIndiceEtoile = [50, 51]
    if Resultat_de_Tensorlow[tabIndiceEtoile[1]] < Resultat_de_Tensorlow[tabIndiceEtoile[0]]:
        aux = tabIndiceEtoile[1]
        tabIndiceEtoile[1] = tabIndiceEtoile[0]
        tabIndiceEtoile[0] = aux

    """
    Puisque le tableau tabIndice est trie par ordre croissant, l'indice de la plus petite valeur est en tabIndice[0]. Si on trouve une valeur de t qui est plus grande que t[tabIndice[0]], on met l'indice de cette valeur dans le tableau tabIndice et on refait un tri sur le tableau. 
    """

    for i in range(5, 50):
        if Resultat_de_Tensorlow[i] > Resultat_de_Tensorlow[tabIndice[0]]:
            tabIndice[0] = i
            for j in range(5):
                for k in range(j, 4):
                    if Resultat_de_Tensorlow[tabIndice[k + 1]] < Resultat_de_Tensorlow[tabIndice[k]]:
                        aux = tabIndice[k + 1]
                        tabIndice[k + 1] = tabIndice[k]
                        tabIndice[k] = aux

    for i in range(51, 62):
        if Resultat_de_Tensorlow[i] > Resultat_de_Tensorlow[tabIndiceEtoile[0]]:
            tabIndiceEtoile[0] = i
            if Resultat_de_Tensorlow[tabIndiceEtoile[1]] < Resultat_de_Tensorlow[tabIndiceEtoile[0]]:
                aux = tabIndiceEtoile[1]
                tabIndiceEtoile[1] = tabIndiceEtoile[0]
                tabIndiceEtoile[0] = aux

    """
    Affichage des resultat dans le terminal., end = ''
    """

    print("Les prochains numero a jouer sont : \n")
    for i in range(4):
        print(str(tabIndice[i] + 1) + ", ", end='')
    print(str(tabIndice[4] + 1))
    print("Les numeros etoile sont : \n")
    print(str(tabIndiceEtoile[0] + 1 - 50) + ", " + str(tabIndiceEtoile[1] + 1 - 50))

    """
    On enregistre les donnees dans un fichier CSV de la facons suivante :
    Les indices sont en colonne 1 et les probabilites en colonne 2
    """
    date = datetime.datetime.now()
    with open(nomFichier, 'a') as csvfile:
        filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        filewriter.writerow([date.year, date.month, date.day, date.hour, date.minute, date.second])
        filewriter.writerow(Resultat_de_Tensorlow)

