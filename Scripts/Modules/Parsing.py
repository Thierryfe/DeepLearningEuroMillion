# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour but de récuperer les données et les mettres dans un format exploitable par l'application
Developpeur :
'''
import numpy as np
import os.path
import csv

def setDataForTensorflow(annee_de_debut=2004,annee_de_fin=2019):
    resultat = np.matrix([[]],int)
    pathDataCSV = os.path.expanduser("~") + "/Documents/DataTirage" + "/dataCSV"
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

#print(setDataForTensorflow())