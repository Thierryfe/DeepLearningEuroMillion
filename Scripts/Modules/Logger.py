'''# coding=utf-8uteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de logger toutes les erreurs/warnings dans un fichier de logs. Avec niveau d'erreur, origine de l'erreur etc...

Developpeur :
'''

import logging
import datetime


def writeLog(nom_fonction, niveau, message):
    #writeLog.id += 1
    print(writeLog.id)
    date = datetime.date.today()
    filename = str(date) + "_log" + str(writeLog.id+1)
    if niveau == "WARNING":
        logging.warning(nom_fonction + " " +message)
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
    elif niveau == "DEBUG":
        logging.debug(nom_fonction + " " +message)
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
    elif niveau == "INFO":
        logging.info(nom_fonction + " " +message)
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
    elif niveau == "ERROR":
        logging.error(nom_fonction + " " +message)
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
    elif niveau == "CRITICAL":
        logging.critical(nom_fonction + " " +message)
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
    else:
        print(niveau + " n'est pas un niveau valide")




#writeLog.id=0


#writeLog("testfunction", "niiii", "testMessage")
#writeLog("testfunction", "WARNING", "testMessage")

