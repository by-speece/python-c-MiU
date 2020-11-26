from rich.console import Console
from rich.table import Table

console = Console()

spistresci_table = Table(show_header=True, header_style="bold magenta")
spistresci_table.add_column("Numer")
spistresci_table.add_column("Nazwa Rozdziału")

spistresci_table.add_row(
    "1", "Dokumentacja Maszyn i Urządzeń",
)
spistresci_table.add_row(
    "2", "Oprogramowanie wykorzystywane w procesie prepressu"
)
spistresci_table.add_row(
    "3", "Wykorzystywanie komputerów w poligrafii cyfrowej"
)
spistresci_table.add_row(
    "4", "Przygotowywanie plików do druku cyfrowego i analogowego"
)
spistresci_table.add_row(
    "5", "Przepływ informacji w systemach komputerowych"
)
spistresci_table.add_row(
    "6", "Cyfrowe maszyny drukujące"
)
spistresci_table.add_row(
    "7", "Techniki druku z tonera"
)
spistresci_table.add_row(
    "8", "Drukowanie Natryskowe"
)
spistresci_table.add_row(
    "9", "Plotery"
)
spistresci_table.add_row(
    "10", "Podłoża do druku cyfrowego"
)
spistresci_table.add_row(
    "11", "Podłoża do druku solwentowego"
)
spistresci_table.add_row(
    "12", "Druk offsetowy"
)
spistresci_table.add_row(
    "13", "Fleksografia"
)
spistresci_table.add_row(
    "14", "Sitodruk"
)
spistresci_table.add_row(
    "15", "Druk personalizowany"
)
spistresci_table.add_row(
    "16", "Krajarki i gilotyny"
)
spistresci_table.add_row(
    "17", "Pozyskiwanie materiałów cyfrowych i analogowych "
)
spistresci_table.add_row(
    "18", "Aparaty Fotograficzne"
)
spistresci_table.add_row(
    "19", "Powrót do Menu Głównego"
)


console.print(spistresci_table)
