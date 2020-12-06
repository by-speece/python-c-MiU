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
with open ("resources/wstep.md", encoding="utf8") as readme:
    wstep = Markdown(readme.read(), justify="full")

with open ("resources/dokumentacja.md", encoding="utf8") as readme:
    dokumentacja = Markdown(readme.read(), justify="full")

with open ("resources/drukowanie_natryskowe.md", encoding="utf8") as readme:
    drukowanie_natryskowe = Markdown(readme.read(), justify="full")

with open ("resources/fleksografia.md", encoding="utf8") as readme:
    fleksografia = Markdown(readme.read(), justify="full")

with open ("resources/druk_offsetowy.md", encoding="utf8") as readme:
    druk_offsetowy = Markdown(readme.read(), justify="full")

with open ("resources/aparaty_fotograficzne.md", encoding="utf8") as readme:
    aparaty_fotograficzne = Markdown(readme.read(), justify="full")

with open ("resources/przesyl_w_drukarni.md", encoding="utf8") as readme:
    przesyl_w_drukarni = Markdown(readme.read(), justify="full")

with open ("resources/krajarki_i_gilotyny.md", encoding="utf8") as readme:
    krajarki_i_gilotyny = Markdown(readme.read(), justify="full")

with open ("resources/plotery_solwentowe.md", encoding="utf8") as readme:
    plotery_solwentowe = Markdown(readme.read(), justify="full")

with open ("resources/pozyskiwanie_materiaw_cyfrowych_i_analogowych.md", encoding="utf8") as readme:
    pozyskiwanie_materiaw_cyfrowych_i_analogowych = Markdown(readme.read(), justify="full")

with open ("resources/techniki_druku_z_tonera.md", encoding="utf8") as readme:
    techniki_druku_z_tonera = Markdown(readme.read(), justify="full")

with open ("resources/cyfrowe_maszyny_drukujce.md", encoding="utf8") as readme:
        cyfrowe_maszyny_drukujce = Markdown(readme.read(), justify="full")

with open ("resources/podloza_w_druku_solwentowym.md", encoding="utf8") as readme:
        podloza_w_druku_solwentowym = Markdown(readme.read(), justify="full")

with open ("resources/oprogramowanie_wykorzystywane_w_prepressie.md", encoding="utf8") as readme:
        oprogramowanie_wykorzystywane_w_prepressie = Markdown(readme.read(), justify="full")

with open ("resources/przygotowanie_plikow_do_druku.md", encoding="utf8") as readme:
        przygotowanie_plikow_do_druku = Markdown(readme.read(), justify="full")

with open ("resources/druk_personalizowany.md", encoding="utf8") as readme:
        druk_personalizowany = Markdown(readme.read(), justify="full")

with open ("resources/podloza_drukowe.md", encoding="utf8") as readme:
        podloza_drukowe = Markdown(readme.read(), justify="full")

with open ("resources/wykorzystanie_komputerow_w_poligrafii_cyfrowej.md", encoding="utf8") as readme:
        wykorzystywanie_komputerow_w_poligrafii = Markdown(readme.read(), justify="full")

with open ("resources/sitodruk.md", encoding="utf8") as readme:
        sitodruk = Markdown(readme.read(), justify="full")

with open ("resources/o_mnie.md", encoding="utf8") as readme:
        o_mnie = Markdown(readme.read(), justify="full")

with open ("resources/gplv3.md", encoding="utf8") as readme:
        gplv3 = Markdown(readme.read(), justify="full")

with open ("resources/Start.md", encoding="utf8") as readme:
        starttext = Markdown(readme.read(), justify="full")
