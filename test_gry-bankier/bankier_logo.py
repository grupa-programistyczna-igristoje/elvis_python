from bankier_var import *
import os

def graLogo (log):
	if (not os.path.exists(gra_path_full +'/bankier.logo')): 
		print("Brak pliku \"bankier.logo\"")
		if(log == 1):
			log_temp = open(gra_path_full + "/" + 'bankier.error', "a+")
			log_temp.write(str("Brak pliku \"bankier.logo\" w lokalizacji \"%s\"" + "\n=====\n"))
			log_temp.close()
		print("BANKIER v%s" % gra_wersja)
	else:
		gra_logo = open(os.path.join(gra_path_full,'bankier.logo'), "r")
		print(gra_logo.read())
		gra_logo.close()