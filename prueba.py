def main():
    # Definir los productos y sus precios en un diccionario
    productos = {
        "Pan ciabatta": 2000,
        "Pie de limon": 3500,
        "Café": 2200,
        "Té": 1600,
        "Alfajor": 1000
    }

    total_ventas_dia = 0  # Inicializar el total de ventas del día

    try:
        # Ciclo for para iterar sobre cada producto
        for producto, precio in productos.items():
            while True:
                try:
                    # Solicitar la cantidad vendida del producto
                    cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
                    # Verificar si la cantidad es válida (mayor o igual a cero)
                    if cantidad >= 0:
                        # Calcular el total de ventas del producto
                        total_producto = cantidad * precio
                        # Imprimir el total de ventas del producto
                        print(f"Total de ventas de {producto}: ${total_producto:.2f}")
                        # Sumar al total de ventas del día
                        total_ventas_dia += total_producto
                        break  # Salir del bucle while si la cantidad es válida
                    else:
                        print("Error: La cantidad ingresada no es válida. Intente de nuevo.")
                except ValueError:
                    print("Error: Por favor ingrese un valor numérico.")
    finally:
        # Imprimir el total de ventas del día
        print(f"\nTotal de ventas del día: ${total_ventas_dia:.2f}")



main()
