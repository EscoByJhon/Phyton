def calcular_total_ventas(productos_vendidos):
    # Diccionario con los productos y sus precios
    precios = {
        "Pan ciabatta": 2000,
        "Pie de limon": 3500,
        "Café": 2200,
        "Té": 1600,
        "Alfajor": 1000
    }

    total_ventas = 0  # Inicializar el total de ventas del día

    # Iterar sobre los productos vendidos
    for producto, cantidad in productos_vendidos.items():
        # Verificar si la cantidad es válida (mayor o igual a cero)
        if cantidad >= 0:
            # Calcular el total de ventas del producto
            total_ventas_producto = cantidad * precios.get(producto, 0)  # Obtener el precio del producto
            total_ventas += total_ventas_producto  # Sumar al total de ventas del día
        else:
            print(f"Error: La cantidad vendida de {producto} no es válida.")
    return total_ventas


def main():
    productos_vendidos = {}  # Diccionario para almacenar los productos vendidos y sus cantidades

    try:
        # Solicitar la cantidad vendida de cada producto
        for _ in range(5):
            producto = input("Ingrese el nombre del producto vendido: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            productos_vendidos[producto] = cantidad
    except ValueError:
        print("Error: Por favor ingrese un valor numérico para la cantidad.")
    finally:
        # Calcular el total de ventas
        total_ventas = calcular_total_ventas(productos_vendidos)
        # Imprimir el total de ventas del día
        print(f"Total de ventas del día: ${total_ventas:.2f}")


if __name__ == "__main__":
    main()
