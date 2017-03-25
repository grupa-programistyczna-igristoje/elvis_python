from bankier_var import *
from bankier_zapis_wczyt import *
from bankier_logo import *
from bankier_intro import *
import random
import os
import getpass
import pickle

def rysMainMenu (*arg_1):
	graLogo(1)
	if (not os.path.exists(gra_path_full +'/bankier.main_menu')): 
		print("Błąd wczytywania pliku \"bankier.main_menu\"")
	else:
		wcz_mainMenu = open(os.path.join(gra_path_full,'bankier.main_menu'), "r")
		template_mainMenu = wcz_mainMenu.read()
		wcz_mainMenu.close()
		with open(os.path.join(gra_path_full,'bankier.ustawienia'),"rb") as wcz_conf:
			if wcz_conf.mode == 'rb':
				wcz_conf_nazwa = pickle.load(wcz_conf)
		print(template_mainMenu.format(
			wcz_conf_nazwa[0],
			"",

			'Pozostała liczba kroków: ',
			str(user_liczbakrokow)+"🕒",

			"Wpisz numer akcji",

			"Liczba akcji: ",
			str(user_liczbaakcji)+"🔨",

			"Pieniądze: ",
			str(user_pieniadze)+"$",

			"1",
			"Zarabianie",
			str(gra_zarabianie_la_1)+"🔨",

			"2",
			"Zdobądź akcje",
			str(gra_zdobacakcje_la_2)+"🔨",

			"3",
			"Blabla    ",
			"",

			"4",
			"Zapisz i wyjdź",

			))

def wybMainMenu(*arg_1):
	user_menu1 = input()
	return user_menu1