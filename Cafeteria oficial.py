def main():
    productos = {
        "Pan ciabatta": 2000,
        "Pie de limon": 3500,
        "Café": 2200,
        "Té": 1600,
        "Alfajor": 1000
    }

    total_ventas_dia = 0
    
    with open("ventas.txt", "w") as archivo:  
        for producto, precio in productos.items():
            cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
            if cantidad >= 0:
                total_producto = cantidad * precio
                archivo.write(f"Total de ventas de {producto}: ${total_producto:.2f}\n")  
                total_ventas_dia += total_producto
            else:
                print("Error: La cantidad ingresada no es válida. Intente de nuevo.")

        archivo.write(f"\nTotal de ventas del día: ${total_ventas_dia:.2f}\n")  

    print("Los resultados se han guardado en el archivo 'ventas.txt'.")

main()
