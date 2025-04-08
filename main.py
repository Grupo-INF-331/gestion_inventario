from login import login
from inventario import *


def mostrar_menu():
    print("""
=== MENÚ ===
1. Agregar producto
2. Consultar productos
3. Actualizar producto
4. Eliminar producto
5. Buscar producto
6. Reporte
7. Salir
""")

def main():
    while True:
        if not login():
            print("Login fallido, intente de nuevo")
            continue
        else:
            print("Login exitoso")
            break
    inventario = cargar_inventario()
    while True:
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            consultar_productos(inventario)
        elif opcion == "3":
            actualizar_producto(inventario)
        elif opcion == "4":
            eliminar_producto(inventario)
        elif opcion == "5":
            buscar_filtrar(inventario)
        elif opcion == "6":
            generar_reporte(inventario)
        elif opcion == "7":
            print("👋 Hasta luego.")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    main()
