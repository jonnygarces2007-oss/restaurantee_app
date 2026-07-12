from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu() -> None:
  
    print("\n========================================")
    print("        SISTEMA DE GESTIÓN RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")
    print("========================================")


def main():
   
    mi_restaurante = Restaurante(nombre="Sabor Andino")

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Por favor ingrese un número válido.")
            continue

      
        if opcion == 1:
            print("\n--- Registrar Producto ---")
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría (Comida / Bebida / Postre): ")
                precio = float(input("Precio: $"))
                disponible = input("¿Está disponible? (s/n): ").strip().lower() == "s"

                # Creamos el objeto usando el constructor
                nuevo_producto = Producto(nombre, categoria, precio, disponible)
                mi_restaurante.registrar_producto(nuevo_producto)
                print("✅ Producto registrado con éxito.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == 2:
            mi_restaurante.listar_productos()

        elif opcion == 3:
            print("\n--- Buscar Producto ---")
            nombre_buscar = input("Ingrese el nombre del producto: ")
            encontrado = mi_restaurante.buscar_producto(nombre_buscar)
            if encontrado:
                print("🔍 Producto encontrado:")
                print(encontrado.mostrar_informacion())
            else:
                print("❌ Producto no encontrado.")

      
        elif opcion == 4:
            print("\n--- Registrar Cliente ---")
            try:
                id_cliente = int(input("ID único del cliente: "))
                nombre = input("Nombre completo: ")
                correo = input("Correo electrónico: ")

                # Creamos el objeto usando @dataclass
                nuevo_cliente = Cliente(id_cliente, nombre, correo)
                mi_restaurante.registrar_cliente(nuevo_cliente)
                print("✅ Cliente registrado con éxito.")
            except ValueError:
                print("❌ El ID debe ser un número entero.")

        elif opcion == 5:
            mi_restaurante.listar_clientes()

        elif opcion == 6:
            print("\n--- Buscar Cliente ---")
            try:
                id_buscar = int(input("Ingrese el ID del cliente: "))
                encontrado = mi_restaurante.buscar_cliente(id_buscar)
                if encontrado:
                    print("🔍 Cliente encontrado:")
                    print(encontrado)
                else:
                    print("❌ Cliente no encontrado.")
            except ValueError:
                print("❌ El ID debe ser un número válido.")

        elif opcion == 7:
            print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("⚠️ Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()
