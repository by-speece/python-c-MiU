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

with open ("resources/cyfrowe_maszyny_drukujce.md") as readme:
        cyfrowe_maszyny_drukujce = Markdown(readme.read())

with open ("resources/podloza_w_druku_solwentowym.md") as readme:
        podloza_w_druku_solwentowym = Markdown(readme.read())

with open ("resources/oprogramowanie_wykorzystywane_w_prepressie.md") as readme:
        oprogramowanie_wykorzystywane_w_prepressie = Markdown(readme.read())

with open ("resources/przygotowanie_plikow_do_druku.md") as readme:
        przygotowanie_plikow_do_druku = Markdown(readme.read())

with open ("resources/druk_personalizowany.md") as readme:
        druk_personalizowany = Markdown(readme.read())

with open ("resources/podloza_drukowe.md") as readme:
        podloza_drukowe = Markdown(readme.read())

with open ("resources/wykorzystanie_komputerow_w_poligrafii_cyfrowej.md") as readme:
        wykorzystywanie_komputerow_w_poligrafii = Markdown(readme.read())

with open ("resources/sitodruk.md") as readme:
        sitodruk = Markdown(readme.read())

with open ("resources/o_mnie.md") as readme:
        o_mnie = Markdown(readme.read())

with open ("resources/gplv3.md") as readme:
        gplv3 = Markdown(readme.read())

with open ("resources/Start.md") as readme:
        starttext = Markdown(readme.read())
