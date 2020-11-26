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
    "8", "Techniki druku cyfrowego"
)
spistresci_table.add_row(
    "9", "Plotery"
)
spistresci_table.add_row(
    "10", "Podłoża do druku cyfrowego"
)
spistresci_table.add_row(
    "11", "Druk offsetowy"
)
spistresci_table.add_row(
    "12", "Fleksografia"
)
spistresci_table.add_row(
    "13", "Sitodruk"
)
spistresci_table.add_row(
    "14", "Druk spersonalizowany"
)
spistresci_table.add_row(
    "15", "Gilotyny i wykrawarki"
)
spistresci_table.add_row(
    "16", "Pozyskiwanie materiałów do druku"
)
spistresci_table.add_row(
    "17", "Aparaty fotograficzne"
)


console.print(spistresci_table)
