#Biblioteki
import os
from rich.console import Console
from rich.markdown import Markdown
#Import Bibliotek Własnych
from tekst import *
from spistresci import *
from menu import *
#Style tekstu
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#Podsystem Czyszczenia
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#Podsystem Powrotu
def powrot_menu():
    powrot = input((color.RED + color.BOLD + "Naciśnij Enter by wrócić do Menu...." + color.END))
    if enter == '':
        menu()
    else:
        print("Nieznana Akcja")
        powrot_menu()
#Wiadomośc powitalna
def startx():
    cls()
    console.print(starttext)
    startxenter = input(color.RED + color.BOLD + "Naciśnij Enter by zaakceptować" + color.END)
    if startxenter == '':
        menu()
    else:
        print("Nie zaakceptowałeś licencji!")
        startx()
#Program Właściwy
def menu():
    cls()
    console.print(menu_table)
    choice = input(color.RED + color.BOLD + "Wybierz numer i naciśnij Enter:" + color.END)

    if choice == "1":
        def spis():
            #Podsystem Spisu Treści
            def monit():
                enter = input(color.RED + color.BOLD + "Naciśnij Enter by wrócić do Spisu Treści...." + color.END)
                if enter == '':
                    spis()
            cls()
            console.print(spistresci_table)
            spistresci = input(color.RED + color.BOLD + "Wybierz numer i naciśnij Enter:" + color.END)

            if spistresci == "1":
                cls()
                console.print(dokumentacja)
                monit()

            if spistresci == "2":
                cls()
                console.print(wykorzystywanie_komputerow_w_poligrafii)
                monit()

            if spistresci == "3":
                cls()
                console.print(oprogramowanie_wykorzystywane_w_prepressie)
                monit()

            if spistresci == "4":
                cls()
                console.print(przygotowanie_plikow_do_druku)
                monit()

            if spistresci == "5":
                cls()
                console.print(przesyl_w_drukarni)
                monit()

            if spistresci == "6":
                cls()
                console.print(cyfrowe_maszyny_drukujce)
                monit()

            if spistresci == "7":
                cls()
                console.print(techniki_druku_z_tonera)
                monit()

            if spistresci == "8":
                cls()
                console.print(drukowanie_natryskowe)
                monit()

            if spistresci == "9":
                cls()
                console.print(plotery_solwentowe)
                monit()
            if spistresci == "10":
                cls()
                console.print(podloza_w_druku_solwentowym)
                monit()

            if spistresci == "11":
                cls()
                console.print(podloza_drukowe)
                monit()

            if spistresci == "12":
                cls()
                console.print(druk_offsetowy)
                monit()

            if spistresci == "13":
                cls()
                console.print(fleksografia)
                monit()

            if spistresci == "14":
                cls()
                console.print(sitodruk)
                monit()

            if spistresci == "15":
                cls()
                console.print(druk_personalizowany)
                monit()

            if spistresci == "16":
                cls()
                console.print(krajarki_i_gilotyny)
                monit()

            if spistresci == "17":
                cls()
                console.print(pozyskiwanie_materiaw_cyfrowych_i_analogowych)
                monit()

            if spistresci == "18":
                cls()
                console.print(aparaty_fotograficzne)
                monit()
        spis()
    if choice == "2":
        cls()
        console.print(wstep)
        powrot_menu()
    if choice == "3":
        cls()
        console.print(o_mnie)
        powrot_menu()
    if choice == "4":
        cls()
        console.print(gplv3)
        powrot_menu
startx()
