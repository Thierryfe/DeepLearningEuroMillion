# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de verifier si les données sont à jour, si ce n'est pas le cas, il faut les mettre à jour
Developpeur :
'''


def dowloadTirages():
    for i in range(2004,2020):
        fname = "euromillions-"+str(i)+".xls"
        if not(os.path.isfile(fname)):
            os.system("wget 'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&as=XLS&year="+str(i)+"' -O '"+fname+"'")
