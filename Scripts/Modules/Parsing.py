# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour but de récuperer les données et les mettres dans un format exploitable par l'application
Developpeur :
'''

import csv
import xlrd
import csv
import os
import datetime

def parsingAllTirages(quiet=false,annee = date.year+1,nomDuFichier = "tirages.csv"):
    file = open(nomDuFichier, "w")
    writer = csv.writer(file)

    for i in range(2004, annee):
        fname = 'euromillions-' + str(i) + '.csv'

        with open(fname, 'r') as f:
            reader = csv.reader(f)
            tmp = 0
            for row in reader:
                if (row[0] == 'Date'):
                    tmp = 1
                if (tmp == 2):
                    if not(quiet):
                     log(int(float(row[1])), int(float(row[2])), int(float(row[3])), int(float(row[4])), int(float(row[5])), int(float(row[6])), int(float(row[7]))) #retourne en log les resultats
                    writer.writerow(int(float(row[1])), int(float(row[2])), int(float(row[3])), int(float(row[4])), int(float(row[5])), int(float(row[6])), int(float(row[7]))) #ecrit les donnees  dans un fichier

                if (tmp == 1):
                    tmp = 2


def convertXLStoCSV(cheminXLS = "donneeXLS", cheminCSV = "donneeCSV", annee=date.year+1):

        try:
            os.mkdir(cheminXLS)
        except:
            print('dossier '++' déjà éxistant')

        try:
            os.mkdir(cheminCSV)
        except:
            print('dossier '++' déjà éxistant')

        for i in range(2004,annee):
            fname = 'euromillions-' + str(i) + '.xls'
            wb = xlrd.open_workbook(cheminXLS+fname)
            sh = wb.sheet_by_index(0)
            # creer le fichier 'euromillions-2004.csv'
            your_csv_file = open(cheminCSV+'/euromillions-' + str(i) + '.csv', 'w')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
            for rownum in range(sh.nrows):
                wr.writerow(sh.row_values(rownum))

            your_csv_file.close()