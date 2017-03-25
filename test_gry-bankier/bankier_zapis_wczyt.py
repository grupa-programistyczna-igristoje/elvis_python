from bankier_var import *
import pickle

def confWcz(log):
	with open(os.path.join(gra_path_full,'bankier.ustawienia'),"rb") as wcz_conf:
		if wcz_conf.mode == 'rb':
			wcz_conf_nazwa = pickle.load(wcz_conf)
			print("Pomyślnie wczytano profil \"%s" % wcz_conf_nazwa[0] + "\"")
			wcz_conf.close()
def confTworz(log):
	wcz_temp = input("Podaj nazwę profilu: ")
	gra_zapis_list.append(str(wcz_temp))
	os.system("clear")
	wcz_temp = input("Podaj swój wiek: ")
	os.system("clear")
	if(int(wcz_temp) <= 9 or int(wcz_temp) >=100 ):
		print("Niepoprawny wiek")
		print("Zapisywanie profilu zakończone niepowodzeniem")
		if (log == 1):
			log_temp = open(gra_path_full + "/" + 'bankier.error', "a+")
			log_temp.write(str("Wprowadzono niepoprawny wiek \"%s\"" % str(wcz_temp) + "\n=====\n"))
			log_temp.close()
		if (os.path.exists(gra_path_full +'bankier.ustawienia')): 
			os.remove(os.path.join(gra_path_full,'bankier.ustawienia'))
	elif(int(wcz_temp) > 9 and int(wcz_temp) <100):
		with open(os.path.join(gra_path_full,'bankier.ustawienia'),'wb') as wcz_conf:
			if wcz_conf.mode == 'wb':
				gra_zapis_list.append(int(wcz_temp))
				gra_zapis_list.append(user_pieniadze)
				gra_zapis_list.append(user_liczbaakcji)
				gra_zapis_list.append(user_liczbakrokow)
				pickle.dump(gra_zapis_list, wcz_conf)
				wcz_conf.close()
	else:
		print("Wpisałeś coś źle")
def zapDoPliku (nazwa_pliku,co_zapisac,log):
	if (not os.path.exists(gra_path_full + "/" + nazwa_pliku)):
		zapis = open(gra_path_full + "/" + nazwa_pliku, "w")
		zapis.write(str(co_zapisac))
		zapis.close() 
	else:
		if (log == 1):
			print("Plik \"%s\" już istnieje" % nazwa_pliku)
def wczPlik(nazwa_pliku,log):
	if (os.path.exists(gra_path_full + "/" + nazwa_pliku)):
		with open(os.path.join(gra_path_full + "/" + nazwa_pliku),"rb") as wczytaj:
			wczytaj_temp = pickle.load(wczytaj)
			return wczytaj_temp
			wczytaj.close()
	else:
		if (log == 1):
			log_temp = open(gra_path_full + "/" + 'bankier.error', "a+")
			log_temp.write(str("Błąd wczytywania \"%s\"" % nazwa_pliku + "\n=====\n"))
			log_temp.close()
