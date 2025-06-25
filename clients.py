
from storage import load_data, save_data
from logger_cfg import logger
from rich.console import Console
from rich.table import Table

DATA_FILE = "clients.json"
console   = Console()

def list_clients():
    clients = load_data(DATA_FILE)
    if not clients:
        console.print("[yellow]No hay clientes registrados aún.[/]")
        return []

    table = Table(title="📋 Listado de Clientes")
    table.add_column("ID", justify="right")
    table.add_column("Nombre", style="cyan")
    table.add_column("Email",  style="magenta")

    for c in clients:
        table.add_row(str(c["id"]), c["nombre"], c["email"])
    console.print(table)
    return clients

def add_client(nombre: str, email: str):
    clients = load_data(DATA_FILE)
    new_id = max((c["id"] for c in clients), default=0) + 1
    clients.append({"id": new_id, "nombre": nombre, "email": email})
    save_data(DATA_FILE, clients)
    logger.info(f"Cliente {new_id} agregado: {nombre} – {email}")
    console.print(f"[green]✅ Cliente #{new_id} agregado.[/]")
    return new_id

def edit_client(client_id: int, nuevo_nombre: str, nuevo_email: str):
    clients = load_data(DATA_FILE)
    for c in clients:
        if c["id"] == client_id:
            old = (c["nombre"], c["email"])
            c["nombre"], c["email"] = nuevo_nombre, nuevo_email
            save_data(DATA_FILE, clients)
            logger.info(f"Cliente {client_id} editado: {old} → {(nuevo_nombre, nuevo_email)}")
            console.print(f"[green]✅ Cliente #{client_id} actualizado.[/]")
            return True
    console.print(f"[red]✖ ID {client_id} no encontrado.[/]")
    return False

def remove_client(client_id: int):
    clients = load_data(DATA_FILE)
    for i, c in enumerate(clients):
        if c["id"] == client_id:
            clients.pop(i)
            save_data(DATA_FILE, clients)
            logger.info(f"Cliente {client_id} eliminado: {c}")
            console.print(f"[green]✅ Cliente #{client_id} eliminado.[/]")
            return True
    console.print(f"[red]✖ ID {client_id} no encontrado.[/]")
    return False

if __name__ == "__main__":
    list_clients()