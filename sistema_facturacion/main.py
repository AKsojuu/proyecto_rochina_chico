# ================================================
# Tarea 1: Inventario en memoria
# Sistema de facturación - Tecnología Springfield
# ================================================

nombre_empresa = "Tecnología Springfield"
iva = 0.15

# Encabezado del sistema
print("================================")
print(nombre_empresa)
print("Sistema de facturación")
print("================================")
print(f"IVA configurado: {iva * 100}%\n")

# Inventario de productos
productos = [
    {
        "id": 1,
        "nombre": "Teclado",
        "precio": 15.00,
        "stock": 10
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "precio": 8.50,
        "stock": 20
    },
    {
        "id": 3,
        "nombre": "Monitor",
        "precio": 180.00,
        "stock": 5
    }

# Mostrar todos los productos
print("\n--- INVENTARIO ---")
for producto in productos:
    print(f"ID: {producto['id']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Stock: {producto['stock']}")
    print("-------------------")