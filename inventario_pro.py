# ==========================================
# TAREA 1: CREAR EL INVENTARIO EN MEMORIA
# Conceptos: Variables, Listas, Diccionarios y For
# ==========================================

# 1. VARIABLES BÁSICAS
# Definimos datos simples para interactuar con el sistema
nombre_tienda = "Mi Tienda Tecnológica"
version_sistema = 1.0

print(f"--- Bienvenido a {nombre_tienda} (v{version_sistema}) ---")


# 2. EL INVENTARIO EN MEMORIA (DICCIONARIO DE DICCIONARIOS)
# Estructura ideal: La clave es el CÓDIGO único del producto.
# El valor es otro diccionario con los detalles del artículo.
inventario = {
    "PROD01": {
        "nombre": "Laptop Gamer",
        "precio": 1200.00,
        "stock": 10
    },
    "PROD02": {
        "nombre": "Mouse Óptico",
        "precio": 25.50,
        "stock": 50
    },
    "PROD03": {
        "nombre": "Teclado Mecánico",
        "precio": 85.00,
        "stock": 15
    }
}


# 3. LISTAS (Para registrar operaciones o categorías)
# Usamos una lista simple para guardar el historial de las últimas ventas hechas en el día
historial_ventas = ["PROD01", "PROD02", "PROD02"]


# 4. RECORRIDO CON BUCLE 'FOR' (Mostrar el reporte en pantalla)
# Usamos .items() para obtener al mismo tiempo el código (clave) y los datos (valor)
print("\n--- REPORTE DE INVENTARIO ACTUAL ---")

for codigo, datos in inventario.items():
    # Extraemos los datos del diccionario interno en variables locales
    nombre_articulo = datos["nombre"]
    precio_articulo = datos["precio"]
    stock_actual = datos["stock"]
    
    # Imprimimos de forma ordenada usando F-Strings
    print(f"Código: {codigo} | Producto: {nombre_articulo:<18} | Precio: ${precio_articulo:<7.2f} | Stock: {stock_actual}")

print("------------------------------------\n")


# 5. EXTRA: EJEMPLO DE USO DE LA LISTA CON FOR
# Recorremos la lista de ventas para mostrar qué se vendió hoy
print("--- HISTORIAL DE VENTAS DEL DÍA ---")
contador = 1
for codigo_vendido in historial_ventas:
    # Buscamos el nombre del producto en nuestro diccionario usando el código de la lista
    nombre_vendido = inventario[codigo_vendido]["nombre"]
    print(f"Venta #{contador}: Se vendió 1 unidad de {nombre_vendido} ({codigo_vendido})")
    contador += 1
