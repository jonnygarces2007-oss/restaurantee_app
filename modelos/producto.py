class Producto:
    """Clase que representa un producto del restaurante, con encapsulación y validaciones"""

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Atributos con guion bajo para indicar que son protegidos
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._disponible = disponible

    # Propiedad para acceder al nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip().capitalize()

    # Propiedad para acceder a la categoría
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = valor.strip().capitalize()

   
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = round(valor, 2)

    
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise ValueError("El valor de disponibilidad debe ser verdadero o falso.")
        self._disponible = valor

    def mostrar_informacion(self) -> str:
        """Devuelve los datos del producto en formato legible"""
        estado = "Disponible" if self._disponible else "No disponible"
        return (f"Nombre: {self._nombre} | Categoría: {self._categoria} | "
                f"Precio: ${self._precio:.2f} | Estado: {estado}")
