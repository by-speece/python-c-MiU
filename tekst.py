#Biblioteki
import os
from rich.console import Console
from rich.markdown import Markdown
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
#Biblioteka Właściwa
console = Console()
with open ("resources/wstep.md") as readme:
    wstep = Markdown(readme.read())

with open ("resources/dokumentacja.md") as readme:
    dokumentacja = Markdown(readme.read())

with open ("resources/drukowanie_natryskowe.md") as readme:
    drukowanie_natryskowe = Markdown(readme.read())

with open ("resources/fleksografia.md") as readme:
    fleksografia = Markdown(readme.read())

with open ("resources/druk_offsetowy.md") as readme:
    druk_offsetowy = Markdown(readme.read())

with open ("resources/aparaty_fotograficzne.md") as readme:
    aparaty_fotograficzne = Markdown(readme.read())

with open ("resources/przesyl_w_drukarni.md") as readme:
    przesyl_w_drukarni = Markdown(readme.read())

with open ("resources/krajarki_i_gilotyny.md") as readme:
    krajarki_i_gilotyny = Markdown(readme.read())

with open ("resources/plotery_solwentowe.md") as readme:
    plotery_solwentowe = Markdown(readme.read())

with open ("resources/pozyskiwanie_materiaw_cyfrowych_i_analogowych.md") as readme:
    pozyskiwanie_materiaw_cyfrowych_i_analogowych = Markdown(readme.read())

with open ("resources/techniki_druku_z_tonera.md") as readme:
    techniki_druku_z_tonera = Markdown(readme.read())
