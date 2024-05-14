def proceso():
    productos = {
        "Pan ciabatta": 2000,
        "Pie de limon": 3500,
        "Café": 2200,
        "Té": 1600,
        "Alfajor": 1000
    }

    total_ventas_dia = 0
    
    archivo = None  # Inicializamos archivo como None

    try:
        with open("ventas.txt", "w") as archivo:  
            for producto, precio in productos.items():
                while True:
                    try:
                        cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
                        if cantidad >= 0:
                            total_producto = cantidad * precio
                            archivo.write(f"Total de ventas de {producto}: ${total_producto:.2f}\n")  
                            total_ventas_dia += total_producto
                            break
                        else:
                            archivo.write(f"Error: La cantidad ingresada de {producto} no es válida.\n")
                    except ValueError:
                        archivo.write("Error: Por favor ingrese un valor numérico para la cantidad.\n")
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")
    else:
        archivo.write(f"\nTotal de ventas del día: ${total_ventas_dia:.2f}\n")  
        print("Los resultados se han guardado en el archivo 'ventas.txt'.")
    finally:
        if archivo is not None:  # Verificamos si el archivo está definido
            archivo.close()


proceso()

