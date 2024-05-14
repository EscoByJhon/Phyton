def main():
    total_ventas_dia = 0  # Variable para almacenar el total de ventas del día
    
    # Ciclo for para iterar sobre los 5 productos
    for i in range(1, 6):
        # Solicitar la cantidad vendida del producto
        cantidad = int(input(f"Ingrese la cantidad vendida del producto {i}: "))
        
        # Verificar si la cantidad es válida (mayor o igual a cero)
        if cantidad >= 0:
            precio_unitario = float(input(f"Ingrese el precio unitario del producto {i}: "))
            total_producto = cantidad * precio_unitario
            print(f"Total de ventas del producto {i}: ${total_producto:.2f}")
            total_ventas_dia += total_producto  # Sumar al total de ventas del día
        else:
            print("Error: La cantidad ingresada no es válida. Intente de nuevo.")

    # Imprimir el total de ventas del día
    print(f"\nTotal de ventas del día: ${total_ventas_dia:.2f}")


if __name__ == "__main__":
    main()


