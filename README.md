## Alumno: Pedro Alves Mesquita
##  PARCIAL 2 DE PROGRAMACION 1
## Profesor: Juan Pablo Sosa
## Carrera: Ciencia de Datos

# Gestor de Pedidos

## Descripción  
Este proyecto es un **gestor de pedidos** de línea de comandos, desarrollado en Python, que permite:  
- Registrar clientes  
- Crear, consultar y alterar status de pedidos  
- Almacenar y recuperar datos en archivos JSON  

## Objetivos  
1. Diseñar una aplicación modular que separe la lógica de negocio, el manejo de datos y la interfaz de usuario.  
2. Demostrar el uso de estructuras de datos dinámicas (listas y diccionarios) para almacenar clientes y pedidos.  
3. Facilitar el manejo de la información con serialización JSON.  

## Requirements  
- Python 3.8 o superior  
- Módulos de la librería estándar: `json`, `logging`, `os`, `typing`  
- (Opcional) Crear un entorno virtual:  
  ```bash
  python -m venv venv
  source venv/bin/activate   # macOS/Linux
  venv\Scripts\activate      # Windows
  pip install -r requirements.txt

## Estructura del Proyecto

Parcial2-Programacion1/
├── clients.py         # Definición de la clase Client y utilidades
├── orders.py          # Definición de la clase Order y métodos de cálculo
├── storage.py         # Funciones para guardar/cargar JSON
├── logger_cfg.py      # Configuración de logging
├── main.py            # Punto de entrada y menú interactivo
├── requirements.txt   # Dependencias (vacío si solo stdlib)
└── data/
    ├── clients.json   # Base de datos de clientes
    └── orders.json    # Base de datos de pedidos

## Módulos, Clases y Funciones

## Note: Para optimizar la vizualización del gestor, importamos rich que no es nativo.

## por files:

1. clients.py

class Client:
    def __init__(self, client_id: int, name: str, email: str):
        """Constructor: almacena id, nombre y correo."""
    def to_dict(self) -> dict:
        """Serializa un cliente a dict para JSON."""
    @staticmethod
    def from_dict(data: dict) -> 'Client':
        """Deserializa un dict a instancia Client."""

2. orders.py

class Order:
    def __init__(self, order_id: int, client_id: int):
        """Constructor: vincula pedido a cliente y arranca lista de ítems."""
    def add_item(self, product: str, qty: int, unit_price: float):
        """Agrega un ítem al pedido como tupla (producto, cantidad, precio)."""
    def calculate_total(self) -> float:
        """Devuelve la suma total de todos los ítems."""
    def to_dict(self) -> dict:
        """Serializa pedido (incluye lista de ítems)."""
    @staticmethod
    def from_dict(data: dict) -> 'Order':
        """Deserializa dict a instancia Order con sus ítems."""

3. storage.py

def load_clients(path: str) -> list[Client]:
    """Lee clients.json y devuelve una lista de Client."""
def save_clients(path: str, clients: list[Client]) -> None:
    """Serializa lista de Client a JSON."""
def load_orders(path: str) -> list[Order]:
    """Lee orders.json y devuelve una lista de Order."""
def save_orders(path: str, orders: list[Order]) -> None:
    """Serializa lista de Order a JSON."""


4. logger_cfg.py

import logging
def setup_logging(level: int = logging.INFO):
    """Configura formato y nivel de logging global para la app."""


5. main.py

def show_menu() -> None:
    """Imprime las opciones: registrar cliente, nuevo pedido, listar, salir."""
def create_client(clients: list[Client]) -> None:
    """Solicita datos, instancia Client y añade a la lista."""
def create_order(clients: list[Client], orders: list[Order]) -> None:
    """Genera un nuevo pedido, asocia ítems y lo almacena."""
def list_clients(clients: list[Client]) -> None:
    """Muestra todos los clientes registrados."""
def list_orders(orders: list[Order]) -> None:
    """Muestra todos los pedidos con totales y estado."""
def load_data() -> tuple[list[Client], list[Order]]:
    """Carga listas iniciales de JSON en disco."""
def save_data(clients: list[Client], orders: list[Order]) -> None:
    """Guarda las listas actuales en archivos JSON."""
def main() -> None:
    """Bucle principal de la aplicación: muestra menú y despacha acciones."""

## Manejo de Listas y Diccionarios

- Listas (list[Client], list[Order]) para mantener el orden de inserción y permitir recorrido secuencial.

- Diccionarios en memoria (opcional) para acceder rápidamente a clientes o pedidos por su ID:

clients_map = {c.client_id: c for c in clients}
orders_map  = {o.order_id: o for o in orders}

- Combinar ambos enfoques agiliza búsquedas (O(1) en dict) y mantiene un historial ordenado (lista).

- Crear un mapa de clientes/pedidos para búsquedas O(1)
# Tras cargar tu lista de Client:
clients_map: dict[int, Client] = {c.client_id: c for c in clients}

# Tras cargar tu lista de Order:
orders_map: dict[int, Order]  = {o.order_id: o for o in orders}
