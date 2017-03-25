import random
import os
import getpass
#----------ogólne zmienne
nazwa_komputer_user = getpass.getuser()
gra_path_short = os.path.join('/home', nazwa_komputer_user)
gra_path_full = gra_path_short + "/Documents/BANKIER"
gra_wersja, user_liczbakrokow, user_liczbaakcji, user_pieniadze = "0.25", 0, 0, 0
gra_zarabianie_la_1, gra_zdobacakcje_la_2 = 3, 2
gra_error = "Błąd"
#----------liczby losowe
liczba_los, liczba_los2 = random.randint(0,100), random.randint(0,10)
#----------pętle
mainMenu_petla1 = 0
#----------wczytywanie
gra_zapis_list = []
#0 pozycja we wczytywaniu ustawień to nazwa profilu
#1 pozycja to wiek
#2 to pieniądze
#3 to liczba akcji
#4 to liczba kroków

#----------menu
