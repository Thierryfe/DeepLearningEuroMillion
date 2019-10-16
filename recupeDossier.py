import os
import os.path



for i in range(2004,2020):
	
        fname = "euromillions-"+str(i)+".xls"
        if !os.path.isfile(fname):
#on verifie si le fichier n'existe pas
#si c'est le cas on recupere le fichier au format xls
		os.system("wget 'http://www.lottology.com/europe/euromillions/?do=past-draws-archive&tab=&as=XLS&year="+str(i)+"' -o ''")
