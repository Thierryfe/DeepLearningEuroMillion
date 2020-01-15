'''# coding=utf-8uteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de logger toutes les erreurs/warnings dans un fichier de logs. Avec niveau d'erreur, origine de l'erreur etc...

Developpeur :
'''

import logging
import datetime
import os


def writeLog(nom_fonction, niveau, message):
    date = datetime.date.today()

    filename = "logs/" + str(date) + ".log"

    logging.basicConfig(filename = filename, level = niveau, format = '[%(asctime)s %(levelname)s] -> %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')

    if niveau == "WARNING":
        logging.warning(nom_fonction + " " + message)
    elif niveau == "DEBUG":
        logging.debug(nom_fonction + " " + message)
    elif niveau == "INFO":
        logging.info(nom_fonction + " " + message)
    elif niveau == "ERROR":
        logging.error(nom_fonction + " " + message)
    elif niveau == "CRITICAL":
        logging.critical(nom_fonction + " " + message)
    else:
        writeLog("Logs.writeLog()", "ERROR", niveau + " n'est pas un niveau valide")
