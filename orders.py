
from storage    import load_data, save_data
from logger_cfg import logger
from rich.console import Console
from rich.table   import Table

DATA_FILE = "orders.json"
console   = Console()

def list_orders():
    orders = load_data(DATA_FILE)
    if not orders:
        console.print("[yellow]No hay pedidos registrados aún.[/]")
        return []

    table = Table(title="📁 Listado de Pedidos")
    table.add_column("ID", justify="right")
    table.add_column("Cliente ID", justify="right")
    table.add_column("Detalles", style="cyan")
    table.add_column("Estado", style="magenta")

    for o in orders:
        table.add_row(
            str(o["id"]),
            str(o["cliente_id"]),
            o["detalles"],
            o["estado"]
        )
    console.print(table)
    return orders

def add_order(cliente_id: int, detalles: str):
    orders = load_data(DATA_FILE)
    new_id = max((o["id"] for o in orders), default=0) + 1
    order = {
        "id": new_id,
        "cliente_id": cliente_id,
        "detalles": detalles,
        "estado": "pendiente"
    }
    orders.append(order)
    save_data(DATA_FILE, orders)
    logger.info(f"Pedido {new_id} creado para cliente {cliente_id}: {detalles}")
    console.print(f"[green]✅ Pedido #{new_id} agregado.[/]")
    return new_id

def approve_order(order_id: int):
    orders = load_data(DATA_FILE)
    for o in orders:
        if o["id"] == order_id:
            o["estado"] = "aprobado"
            save_data(DATA_FILE, orders)
            logger.info(f"Pedido {order_id} aprobado")
            console.print(f"[green]✅ Pedido #{order_id} aprobado.[/]")
            return True
    raise ValueError(f"ID de pedido {order_id} no existe")

def reject_order(order_id: int):
    orders = load_data(DATA_FILE)
    for o in orders:
        if o["id"] == order_id:
            o["estado"] = "rechazado"
            save_data(DATA_FILE, orders)
            logger.info(f"Pedido {order_id} rechazado")
            console.print(f"[green]✅ Pedido #{order_id} rechazado.[/]")
            return True
    raise ValueError(f"ID de pedido {order_id} no existe")

if __name__ == "__main__":
    list_orders()