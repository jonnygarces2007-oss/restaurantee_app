from dataclasses import dataclass


@dataclass
class Cliente:
    
    id_cliente: int
    nombre: str
    correo: str

    def __str__(self) -> str:
       
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"
