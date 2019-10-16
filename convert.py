import xlrd
import csv

#converti les fichiers xls en csv


for i in range(2004,2020):
    if (i<10):
        fname = 'euromillions-'+str(i)+'.xls'
    wb = xlrd.open_workbook(fname)
    sh = wb.sheet_by_index(0)
#creer le fichier 'euromillions-2004.csv'
    your_csv_file = open('euromillions-'+str(i)+'.csv', 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()
