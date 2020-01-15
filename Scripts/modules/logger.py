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

    try:
        os.mkdir("logs")
        date = datetime.date.today()
        seconde = datetime.datetime.now().time().minute
        filename = "logs/" + str(date) + "_log" + str(seconde)
    except FileExistsError:
        date = datetime.date.today()
        seconde = datetime.datetime.now().time()
        filename = "logs/" + str(date) + "_log" + str(seconde)

    if niveau == "WARNING":
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
        logging.warning(nom_fonction + " " +message)
    elif niveau == "DEBUG":
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
        logging.debug(nom_fonction + " " +message)
    elif niveau == "INFO":
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
        logging.info(nom_fonction + " " +message)
    elif niveau == "ERROR":
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
        logging.error(nom_fonction + " " +message)
    elif niveau == "CRITICAL":
        logging.basicConfig(filename=filename, level=niveau, format='%(asctime)s:%(levelname)s:%(message)s')
        logging.critical(nom_fonction + " " +message)
    else:
        writeLog("Logs.writeLog()","ERROR",niveau + " n'est pas un niveau valide")