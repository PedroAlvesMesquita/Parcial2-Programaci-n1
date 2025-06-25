
from rich.console import Console
from clients import list_clients, add_client, edit_client, remove_client
from orders  import add_order, list_orders, approve_order, reject_order

console = Console()

def login():
    console.print("[bold cyan]Seleccione un rol:[/]")
    console.print("1) Salesperson")
    console.print("2) Credit Analyst")
    console.print("3) SalesOps")
    choice = console.input("Opción [1-3]: ")
    return {"1":"salesperson", "2":"credit", "3":"salesops"}.get(choice)

def menu_salesperson():
    while True:
        console.print("\n[bold green]=== Salesperson Menu ===[/]")
        console.print("1) Listar clientes")
        console.print("2) Crear pedido")
        console.print("3) Listar pedidos")
        console.print("4) Salir")
        opt = console.input("Seleccione [1-4]: ")

        if opt == "1":
            list_clients()

        elif opt == "2":
            # Muestro clientes y valido ID
            clientes = list_clients()
            valid_ids = [c["id"] for c in clientes]
            while True:
                raw = console.input("ID cliente: ")
                try:
                    cid = int(raw)
                    if cid in valid_ids:
                        break
                    console.print(f"[red]ID {cid} no existe. Elija uno de {valid_ids}[/]")
                except ValueError:
                    console.print("[red]Ingrese un número válido[/]")

            detalles = console.input("Detalles del pedido: ")
            add_order(cid, detalles)

        elif opt == "3":
            list_orders()

        elif opt == "4":
            break

        else:
            console.print("[red]Opción inválida[/]")

def menu_credit():
    while True:
        console.print("\n[bold yellow]=== Credit Analyst Menu ===[/]")
        console.print("1) Listar pedidos")
        console.print("2) Aprobar pedido")
        console.print("3) Rechazar pedido")
        console.print("4) Salir")
        opt = console.input("Seleccione [1-4]: ")

        if opt == "1":
            list_orders()
        elif opt == "2":
            try:
                oid = int(console.input("ID de pedido a aprobar: "))
                approve_order(oid)
            except ValueError as e:
                console.print(f"[red]{e}")
        elif opt == "3":
            try:
                oid = int(console.input("ID de pedido a rechazar: "))
                reject_order(oid)
            except ValueError as e:
                console.print(f"[red]{e}")
        elif opt == "4":
            break
        else:
            console.print("[red]Opción inválida[/]")

def menu_salesops():
    while True:
        console.print("\n[bold magenta]=== SalesOps Menu ===[/]")
        console.print("1) Listar clientes")
        console.print("2) Agregar cliente")
        console.print("3) Editar cliente")
        console.print("4) Eliminar cliente")
        console.print("5) Salir")
        opt = console.input("Seleccione [1-5]: ")

        if opt == "1":
            list_clients()
        elif opt == "2":
            nombre = console.input("Nombre: ")
            email  = console.input("Email: ")
            add_client(nombre, email)
        elif opt == "3":
            try:
                cid = int(console.input("ID a editar: "))
                newn= console.input("Nuevo nombre: ")
                newe= console.input("Nuevo email: ")
                edit_client(cid, newn, newe)
            except ValueError:
                console.print("[red]ID inválido[/]")
        elif opt == "4":
            try:
                cid = int(console.input("ID a eliminar: "))
                remove_client(cid)
            except ValueError:
                console.print("[red]ID inválido[/]")
        elif opt == "5":
            break
        else:
            console.print("[red]Opción inválida[/]")

if __name__ == "__main__":
    role = login()
    if   role == "salesperson":
        menu_salesperson()
    elif role == "credit":
        menu_credit()
    elif role == "salesops":
        menu_salesops()
    else:
        console.print("[red]Rol inválido, saliendo...[/]")