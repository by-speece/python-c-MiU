#Biblioteki
import os
from rich.console import Console
from rich.markdown import Markdown
#Import Bibliotek Własnych
from tekst import *
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

#Program Właściwy
def menu():
    cls()
    print(color.CYAN + color.BOLD + "==========Zbiór Wiedzy Poligraficznej==========" + color.END)
    print("1.Spis Treści \n2.O projekcie \n3.O Mnie \n4.O programie")
    choice = input()

    if choice == "1":
        def spis():
            #Podsystem Spisu Treści
            def monit():
                enter = input(color.RED + color.BOLD + "Naciśnij Enter by wrócić do Spisu Treści...." + color.END)
                if enter == '':
                    spis()
            cls()
            print(color.CYAN + color.BOLD + "==========Spis Treści==========" + color.END)
            print("1.#Wstęp")
            print("2.#Dokumentacja techniczna maszyn i urządzeń.")
            print("3.#Drukowanie natryskowe")
            print("4.#Fleksografia")
            print("5.#Druk offsetowy")
            print("6.#Aparaty Fotograficzne")
            print("7.#Przesył w Drukarni")
            spistresci = input()

            if spistresci == "1":
                cls()
                console.print(wstep)
                monit()

            if spistresci == "2":
                cls()
                console.print(dokumentacja)
                monit()

            if spistresci == "3":
                cls()
                console.print(drukowanie_natryskowe)
                monit()

            if spistresci == "4":
                cls()
                console.print(fleksografia)
                monit()

            if spistresci == "5":
                cls()
                console.print(druk_offsetowy)
                monit()

            if spistresci == "6":
                cls()
                console.print(aparaty_fotograficzne)
                monit()

            if spistresci == "7":
                cls()
                console.print(przesyl_w_drukarni)
                monit()
        spis()
    if choice == "2":
        menu()
    if choice == "3":
        menu()
    if choice == "4":
        menu()

menu()
