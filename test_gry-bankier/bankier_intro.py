from bankier_var import *
from bankier_zapis_wczyt import *
from bankier_logo import*
import os

def graIntro (*arg_1):
	if (not os.path.exists(gra_path_full)): 
		os.makedirs(gra_path_full)
	print("Wczytywanie zapisu...")
	if (os.path.exists(gra_path_full + '/bankier.ustawienia')):
		confWcz(1)
	elif (not os.path.exists(gra_path_full + '/bankier.ustawienia')):
		print("Brak wcześniejszych zapisów\nTworzenie nowego profilu...")
		confTworz(1)
	else:
		print("Błąd wczytywania")