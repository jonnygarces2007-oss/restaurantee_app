# restaurantee_app
# 📋 Sistema de Gestión de Restaurante - Semana 7

**Asignatura:** Programación Orientada a Objetos  
**Semana:** 7  
**Estudiante:** [Tu Nombre Completo]

---

##  Objetivo
Este proyecto es una evolución del sistema anterior, aplicando conceptos avanzados de POO: constructores, encapsulación con `@property` y `@setter`, clases de datos con `@dataclass`, y un menú interactivo que permite crear objetos dinámicamente a partir de los datos ingresados por el usuario.

---

##  Conceptos aplicados
- **Constructor tradicional `__init__`:** Para inicializar los atributos de la clase `Producto`.
- **Encapsulación:** Uso de `@property` y `@setter` para controlar el acceso y modificación de atributos, con validaciones de datos.
- **Decorador `@dataclass`:** Simplifica la definición de la clase `Cliente` reduciendo código repetitivo.
- **Arquitectura modular:** Separación clara entre modelos, servicios y lógica de ejecución.
- **Menú interactivo:** Permite registrar, listar y buscar información sin tener datos fijos en el código.
- **Flujo completo:** Entrada de datos → creación de objeto → almacenamiento → consulta.

---

##  Estructura del proyecto

restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py # Clase con constructor, @property y @setter
│ └── cliente.py # Clase implementada con @dataclass
├── servicios/
│ ├── init.py
│ └── restaurante.py # Clase que gestiona listas y operaciones
└── main.py # Menú principal y ejecución




---

## 🚀 Funcionamiento
1. Ejecuta el programa con:
   ```bash
   python main.py

  *Aparecerá un menú con opciones para trabajar con productos y clientes.
*Todos los datos se ingresan en tiempo real y se transforman en objetos válidos.
*Las validaciones evitan que se guarden datos incorrectos o incompletos.
💡 Reflexión
Crear objetos a partir de información ingresada por el usuario es fundamental en cualquier aplicación real, ya que permite que el sistema sea dinámico y útil para cualquier persona. Al usar @property y @setter, nos aseguramos de que los datos sean siempre correctos y consistentes, mientras que la estructura modular facilita que el código se entienda, se mantenga y se amplíe en el futuro sin complicaciones.








