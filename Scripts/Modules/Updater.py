# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de verifier si les données sont à jour, si ce n'est pas le cas, il faut les mettre à jour
Developpeur :
'''
import requests
import os.path
import xlrd
import csv
from urllib.request import urlretrieve


def dowloadFile(anne_de_debut=2004,anne_de_fin=2005,url="http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&as=XLS&year="):
    pathData = os.path.expanduser("~") + "/Documents/DataTirage"
    pathFilesXLS = pathData + "/dataXLS"
    if not (os.path.isdir(pathFilesXLS)):
        os.makedirs(pathFilesXLS)

    for i in range(anne_de_debut, anne_de_fin):
        fname = "euromillions_" + str(i) + ".xls"
        if not (os.path.isfile(pathFilesXLS + "/" + fname)):
            urlretrieve(
                url + str(i) + " ",
                "" + pathFilesXLS + '/' + fname)
    convertXLStoCSV(pathData,pathFilesXLS,anne_de_debut,anne_de_fin)

def convertXLStoCSV(pathData,pathDataXLS, anne_de_debut,anne_de_fin):
    pathDataCSV = pathData + "/dataCSV"
    if not(os.path.isdir(pathDataCSV)):
        os.makedirs(pathDataCSV)

    for i in range(anne_de_debut, anne_de_fin):
        fname = 'euromillions_' + str(i) + '.xls'
        wb = xlrd.open_workbook(pathDataXLS+"/"+ fname)
        sh = wb.sheet_by_index(0)
        # creer le fichier 'euromillions-2004.csv'
        your_csv_file = open(pathDataCSV + '/euromillions_' + str(i) + '.csv', 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            if(rownum>4):
                row = [sh.row_values(rownum)[0] , int(float(sh.row_values(rownum)[1])), int(float(sh.row_values(rownum)[2])) ,int(float(sh.row_values(rownum)[3])) ,int(float(sh.row_values(rownum)[4])),int(float(sh.row_values(rownum)[5])), int(float(sh.row_values(rownum)[6])) , int(float(sh.row_values(rownum)[7]))  ]
                print(row)
                wr.writerow(row)

        your_csv_file.close()

#pour tester la fonction dowloadFile(2004,2020) et recuperer tout les fichier xls et csv
dowloadFile(2004,2005)

