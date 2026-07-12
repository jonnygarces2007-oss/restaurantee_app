from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que gestiona productos y clientes"""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self._lista_productos: List[Producto] = []
        self._lista_clientes: List[Cliente] = []

    # ------------------- Gestión de productos -------------------
    def registrar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto a la lista"""
        self._lista_productos.append(producto)

    def listar_productos(self) -> None:
        """Muestra todos los productos registrados"""
        if not self._lista_productos:
            print("No hay productos registrados todavía.")
            return
        print("\n--- Lista de Productos ---")
        for prod in self._lista_productos:
            print(prod.mostrar_informacion())

    def buscar_producto(self, nombre_buscar: str) -> Optional[Producto]:
        """Busca un producto por su nombre"""
        nombre_buscar = nombre_buscar.strip().lower()
        for prod in self._lista_productos:
            if prod.nombre.lower() == nombre_buscar:
                return prod
        return None

    # ------------------- Gestión de clientes -------------------
    def registrar_cliente(self, cliente: Cliente) -> None:
        """Agrega un nuevo cliente a la lista"""
        self._lista_clientes.append(cliente)

    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados"""
        if not self._lista_clientes:
            print("No hay clientes registrados todavía.")
            return
        print("\n--- Lista de Clientes ---")
        for cli in self._lista_clientes:
            print(cli)

    def buscar_cliente(self, id_buscar: int) -> Optional[Cliente]:
        """Busca un cliente por su ID"""
        for cli in self._lista_clientes:
            if cli.id_cliente == id_buscar:
                return cli
        return None
