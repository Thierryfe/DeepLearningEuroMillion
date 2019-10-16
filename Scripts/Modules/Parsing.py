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


def recupeLesTirages():
    file = open("resultat.csv", "w")
    writer = csv.writer(file)

    for i in range(2004, 2020):
        fname = 'euromillions-' + str(i) + '.csv'

        with open(fname, 'r') as f:
            reader = csv.reader(f)
            tmp = 0
            for row in reader:
                if (row[0] == 'Date'):
                    tmp = 1
                if (tmp == 2):
                    print(int(float(row[1])), int(float(row[2])), int(float(row[3])), int(float(row[4])), int(float(row[5])), int(float(row[6])), int(float(row[7])))
                    writer.writerow([row[1], row[2], row[3], row[4], row[5], row[6], row[7]])

                if (tmp == 1):
                    tmp = 2

def convertXLStoCSV():

    # converti les fichiers xls en csv

    for i in range(2004, 2020):
        fname = 'euromillions-' + str(i) + '.xls'
        wb = xlrd.open_workbook(fname)
        sh = wb.sheet_by_index(0)
        # creer le fichier 'euromillions-2004.csv'
        your_csv_file = open('euromillions-' + str(i) + '.csv', 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()