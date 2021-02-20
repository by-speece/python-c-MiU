from rich.console import Console
from rich.table import Table

console = Console()

menu_table = Table(show_header=True, header_style="bold magenta")
menu_table.add_column("Numer", justify="left")
menu_table.add_column("Nazwa Modułu", justify="right")
menu_table.add_column("Data Aktualizacji",style="dim", justify="right")

menu_table.add_row(
    "1", "Spis Treści", "26-11-2020"
)
d
menu_table.add_row(
    "2",  "O projekcie", "26-11-2020"
)

menu_table.add_row(
    "3",   "O programie", "26-11-2020"
)

menu_table.add_row(
    "4",    "Licencja", "26-11-2020"
)

console.print(menu_table)
