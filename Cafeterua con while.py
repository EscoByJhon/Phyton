def main():
    total_ventas_dia = 0  # Variable para almacenar el total de ventas del día
    producto = 1  # Variable para mantener el número del producto que se está procesando, empezamos con el producto 1
    
    # Ciclo while para solicitar la cantidad vendida de cada producto
    while producto <= 5:  # Mientras el número del producto sea menor o igual a 5, el ciclo se ejecutará
        # Solicitar la cantidad vendida del producto
        cantidad = int(input(f"Ingrese la cantidad vendida del producto {producto}: "))  # Solicitamos al usuario la cantidad vendida del producto
        
        # Verificar si la cantidad es válida (mayor o igual a cero)
        if cantidad >= 0:  # Si la cantidad es mayor o igual a cero, procedemos con el cálculo
            precio_unitario = float(input(f"Ingrese el precio unitario del producto {producto}: "))  # Solicitamos al usuario el precio unitario del producto
            total_producto = cantidad * precio_unitario  # Calculamos el total de ventas del producto multiplicando la cantidad vendida por el precio unitario
            print(f"Total de ventas del producto {producto}: ${total_producto:.2f}")  # Mostramos el total de ventas del producto con formato de dos decimales
            total_ventas_dia += total_producto  # Sumamos el total de ventas del producto al total de ventas del día
            producto += 1  # Pasamos al siguiente producto incrementando en 1 el número del producto
        else:
            print("Error: La cantidad ingresada no es válida. Intente de nuevo.")  # Si la cantidad no es válida, mostramos un mensaje de error y solicitamos nuevamente la cantidad
        
    # Imprimir el total de ventas del día
    print(f"\nTotal de ventas del día: ${total_ventas_dia:.2f}")  # Mostramos el total de ventas del día con formato de dos decimales



main()