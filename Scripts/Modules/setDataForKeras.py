import pandas as pd
import numpy as np
import os.path

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

def setDataForKeras(document):
#---------------------------------------
	if(type(document)!=str):
		return
	test=document.split(".")
	if(test[-1]=="csv"):
		if( os.path.isfile(document)):
		#On récupère les données issu du fichier csv,
		# X qui est de type :<class 'numpy.ndarray'>
			X = np.loadtxt(document, delimiter=',', dtype=np.int32)
			np.save('resultat.npy', X);
			print(X)

		else:
			print("chemin non existant")

	else:
		print("mauvais fichier")
	return X
#---------------------------------------
#finfonction

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

