from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# List modul yang ingin dicek (modul_name, pip_name)
modules = [
    ("rich", "rich"),
    ("rich_cli", "rich-cli"),
    ("httpie", "cloudscraper"),
    ("requests", "requests"),
    ("prompt_toolkit", "prompt_toolkit"),
]

missing = []

def check_modules():
    console.print(Panel("📦 [bold cyan]Mengecek dependensi Python...[/bold cyan]", expand=False))

    table = Table(title="Status Modul", show_lines=True)
    table.add_column("Modul", style="cyan", justify="left")
    table.add_column("Status", style="green", justify="center")
    table.add_column("Install Dengan", style="magenta", justify="left")

    for module, pip_name in modules:
        try:
            __import__(module)
            table.add_row(module, "[bold green]✓ Tersedia[/bold green]", "-")
        except ImportError:
            table.add_row(module, "[bold red]✗ Tidak Ada[/bold red]", f"pip install {pip_name}")
            missing.append(pip_name)

    console.print(table)

    if missing:
        console.print(
            Panel(
                f"[bold yellow]Beberapa modul tidak ditemukan![/bold yellow]\n\n"
                f"[bold red]Jalankan ini:[/bold red]\n"
                f"[italic green]pip install {' '.join(missing)}[/italic green]",
                title="🚨 [red]Perlu Install Modul[/red]",
                border_style="red"
            )
        )
    else:
        console.print(Panel("[bold green]✅ Semua modul sudah terinstall![/bold green]", expand=False))


if __name__ == "__main__":
    check_modules()
