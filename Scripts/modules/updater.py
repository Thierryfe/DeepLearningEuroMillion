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
import datetime
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

lien_par_defaut = "http://www.lottology.com/europe/euromillions/?do=past-draws-archive"
#data_dir = "/home/etudiant/Téléchargements/euromilions results xls/csv"
data_dir =  os.path.expanduser("..") + "/DataTirage" 
pathDataCSV = data_dir + "/dataCSV"
pathFilesXLS = data_dir + "/dataXLS"

## fonction pour télécharger les sources en format CSV. format du nom "euromillions_XXXX.csv". télécharge également les source au format xls : "euromillion_XXXX.xls"
def downloadFile(annee_de_debut=2004,annee_de_fin=datetime.datetime.now().year,url="http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&as=XLS&year="):
    if(annee_de_debut<=annee_de_fin):
        if((annee_de_debut>=2004)and(annee_de_fin<= datetime.datetime.now().year)):
            #pathData = os.path.expanduser("~") + "/Documents/DataTirage"
            
            if (os.path.isdir(pathFilesXLS)):
                print("")
            else:
                os.makedirs(pathFilesXLS)

            for i in range(annee_de_debut, annee_de_fin+1):
                fname = "euromillions_" + str(i) + ".xls"
                if not (os.path.isfile(pathFilesXLS + "/" + fname)):
                    urlretrieve(
                        url + str(i) + " ",
                        "" + pathFilesXLS + '/' + fname)
            convertXLStoCSV(pathFilesXLS,annee_de_debut,annee_de_fin)
        else:
            print("pas de tirages presents pour annee_de_debut et annee_de_fin")
    else:
        print("annee_de_debut doit etre anterieure a annee_de_fin")

## fonction utiliser pour convertir les fichiers du forma xls au format csv    
def convertXLStoCSV(pathDataXLS, anne_de_debut,anne_de_fin):
    
    if os.path.isdir(pathDataCSV):
	    print("")
    else:
        os.makedirs(pathDataCSV)

    for i in range(anne_de_debut, anne_de_fin+1):
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
#dowloadFile(2004,2005)
def checkUpdate(file_path,url=lien_par_defaut):
    # recuperation de la date du dernier tirage sauvegardé sur le fichier de l'année actuelle
    file_path = pathDataCSV + "/euromillions_" + str(datetime.date.today().year) + ".csv"
    if(os.path.isfile(file_path)):
            with open(file_path, newline='') as fichier_annee_courante:
                reader = csv.reader(fichier_annee_courante, delimiter=',', quoting=csv.QUOTE_NONE)
                for row in reader:
                    dernier_tirage = row[0]
                    break

            date_dernier_tirage = datetime.datetime.strptime(dernier_tirage, '%d %B %Y').date()

            # recupération de tous les tags td contenants les dates des tirages
            uClient = urlopen(url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            table = page_soup.findAll("td", {"class": "lightblue text-left nowrap date"})

            # test et recuperation de toutes les dates manquantes et les mettre dans un tableau

            i = 0
            tableau_de_dates = []
            while datetime.date.fromisoformat(table[i].a["href"][23:]) > date_dernier_tirage:
                tableau_de_dates.append(table[i].a["href"][23:])
                i = i + 1
            return tableau_de_dates
    


def update(url=lien_par_defaut):
    file_path = pathDataCSV + "/euromillions_" + str(datetime.date.today().year) + ".csv"
    if (os.path.isdir(data_dir) and os.path.isfile(file_path)):
        tableau_de_dates=checkUpdate(file_path)
        if len(tableau_de_dates) > 0:  # si on a des dates manquantes
            # recuperer la page web    if(os.path.isfile(file_path)):
            uClient = urlopen(url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            # recuperer tous les tirage manquants et les dates
            trs = page_soup.findAll("tr")
            trs = trs[6:]
            tds = []
            for j in range(0, len(tableau_de_dates)):
                tdsm = []
                tds_ = trs[j].findAll("td")
                tdsm.append(tds_[0].a["title"][20:])
                for i in range(1, 8):
                    tdsm.append(tds_[i].text)
                tds.append(tdsm)
            with open(file_path, 'r+', newline="") as f:
                content = f.read()
                f.seek(0, 0)
                writer = csv.writer(f)
                writer.writerows(tds)
                for line in content:
                    f.writelines(line)
        else:
            print("le fichier de l'année courante est à jour, il n'y a pas de nouveaux tirages. \n")
    else:
        os.makedirs(data_dir)
        downloadFile()
    

    