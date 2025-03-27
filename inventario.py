from utils import logger

INVENTARIO_FILE = "data/inventario.txt"

def cargar_inventario():
    inventario = []
    try:
        with open(INVENTARIO_FILE, "r") as f:
            for linea in f:
                campos = linea.strip().split(",")
                if len(campos) == 7:
                    producto = {
                        "id": campos[0],
                        "nombre": campos[1],
                        "descripcion": campos[2],
                        "categoria": campos[3],
                        "precio": float(campos[4]),
                        "stock": int(campos[5]),
                        "sku": campos[6]
                    }
                    inventario.append(producto)
    except Exception as e:
        logger.error(f"Error al cargar inventario: {e}")
    return inventario

def guardar_inventario(inventario):
    try:
        with open(INVENTARIO_FILE, "w") as f:
            for p in inventario:
                linea = f"{p['id']},{p['nombre']},{p['descripcion']},{p['categoria']},{p['precio']},{p['stock']},{p['sku']}\n"
                f.write(linea)
        logger.info("Inventario guardado exitosamente")
    except Exception as e:
        logger.error(f"No se pudo guardar el inventario: {e}")

def generar_id(inventario):
    return str(len(inventario) + 1)

def agregar_producto(inventario):
    try:
        print("=== Agregar Producto ===")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio unitario: "))
        stock = int(input("Cantidad disponible: "))
        sku = input("SKU (código único): ")
        nuevo_producto = {
            "id": generar_id(inventario),
            "nombre": nombre,
            "descripcion": descripcion,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "sku": sku
        }
        inventario.append(nuevo_producto)
        guardar_inventario(inventario)
        logger.info(f"Producto agregado: {nombre}")
        print("✅ Producto agregado.")
    except Exception as e:
        logger.error(f"Error al agregar producto: {e}")

def consultar_productos(inventario):
    print("=== Productos en Inventario ===")
    for p in inventario:
        print(f"{p['id']} | {p['nombre']} | {p['categoria']} | {p['stock']} | ${p['precio']} | SKU: {p['sku']}")

def actualizar_producto(inventario):
    try:
        consultar_productos(inventario)
        pid = input("ID del producto a actualizar: ")
        for p in inventario:
            if p["id"] == pid:
                print("¿Qué campo deseas actualizar?")
                print("1. Nombre\n2. Descripción\n3. Categoría\n4. Precio\n5. Stock\n6. SKU")
                opcion = input("Elige una opción (1-6): ")

                if opcion == "1":
                    p["nombre"] = input("Nuevo nombre: ")
                elif opcion == "2":
                    p["descripcion"] = input("Nueva descripción: ")
                elif opcion == "3":
                    p["categoria"] = input("Nueva categoría: ")
                elif opcion == "4":
                    p["precio"] = float(input("Nuevo precio: "))
                elif opcion == "5":
                    p["stock"] = int(input("Nuevo stock: "))
                elif opcion == "6":
                    p["sku"] = input("Nuevo SKU: ")
                else:
                    print("❌ Opción inválida.")
                    return

                guardar_inventario(inventario)
                logger.info(f"Producto actualizado: ID {pid}, campo {opcion}")
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")
    except Exception as e:
        logger.error(f"Error al actualizar producto: {e}")

def eliminar_producto(inventario):
    try:
        consultar_productos(inventario)
        pid = input("ID del producto a eliminar: ")
        inventario[:] = [p for p in inventario if p["id"] != pid]
        guardar_inventario(inventario)
        logger.info(f"Producto eliminado: ID {pid}")
        print("✅ Producto eliminado.")
    except Exception as e:
        logger.error(f"Error al eliminar producto: {e}")

def buscar_filtrar(inventario):
    criterio = input("Buscar por nombre, categoría o SKU: ").lower()
    encontrados = [p for p in inventario if criterio in p["nombre"].lower() or criterio in p["categoria"].lower() or criterio in p["sku"].lower()]
    print(f"=== Resultados para '{criterio}' ===")
    for p in encontrados:
        print(f"{p['id']} | {p['nombre']} | {p['categoria']} | {p['stock']} | ${p['precio']} | SKU: {p['sku']}")

def generar_reporte(inventario):
    try:
        print("=== Reporte de Inventario ===")
        total = len(inventario)
        valor_total = sum(p["precio"] * p["stock"] for p in inventario)
        agotados = [p["nombre"] for p in inventario if p["stock"] == 0]
        print(f"Total productos: {total}")
        print(f"Valor total del inventario: ${valor_total:.2f}")
        print(f"Productos agotados: {', '.join(agotados) if agotados else 'Ninguno'}")
        logger.info("Se generó un reporte de inventario")
    except Exception as e:
        logger.error(f"Error al generar reporte: {e}")

