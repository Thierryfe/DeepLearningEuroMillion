import numpy
import csv
import datetime


def saveAndDisplayResultKerasRnn(Resultat_de_keras, nomFichier):
    # nomFichier = "resultat_keras.csv"

    """
    On sépare les valeurs de chaque prédiction
    On met les 5 numéros normaux dans le premier et le deuxieme sers à stocker les numéros étoiles
    On les remets en format d'entier pour avoir un affichage propre
    """
    tabIndice = [0, 1, 2, 3, 4]
    for i in range(5):
        if(Resultat_de_keras[i]<=49):
            tabIndice[i]=int(Resultat_de_keras[i])
        else:
            tabIndice[i]=49


    tabIndiceEtoile = [5, 6]
    for i in range(2):
       tabIndiceEtoile[i]=int(Resultat_de_keras[i+5])

    print("Les prochains numero a jouer sont : \n")
    for i in range(4):
        print(str(tabIndice[i] + 1) + ", ", end='')
    print(str(tabIndice[4] + 1))
    print("Les numeros etoile sont : \n")
    print(str(tabIndiceEtoile[0] ) + ", " + str(tabIndiceEtoile[1] ))

    """
    On enregistre les donnees dans un fichier CSV de la facons suivante :
    Les indices sont en colonne 1 et les probabilites en colonne 2
    """
    date = datetime.datetime.now()
    with open(nomFichier, 'a') as csvfile:
        filewriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        filewriter.writerow([date.year, date.month, date.day, date.hour, date.minute, date.second])
        filewriter.writerow(Resultat_de_keras)