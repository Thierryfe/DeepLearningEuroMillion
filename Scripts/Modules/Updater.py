# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de verifier si les données sont à jour, si ce n'est pas le cas, il faut les mettre à jour
Developpeur :
'''
import datetime
from urllib.request import urlretrieve

def dowloadTirages(cheminArriver = "./donneeXLS",year=date.year+1):
    for i in range(2004,year):
        fname = "euromillions-"+str(i)+".xls"
        if not(os.path.isfile(fname)):
            os.mkdir(cheminArriver)
            urlretrieve("http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&as=XLS&year="+str(i), 'xls/'+fname)
