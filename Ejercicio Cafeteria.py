#ctv: calculo total de ventas, tv: total de ventas, tvp: total venta producto

def ctv(productosvendidos):

    precios={

        "Pan ciabatta":2000,
        "Pie de limon":3500,
        "Cafe":2200,
        "Te":1600,
        "Alfajor":1000,
    }

    tv=0

    for producto, cantidad in productosvendidos.item():
    
        if cantidad >= 0:
            tvp = cantidad * precios.get (producto,0)
            tv += tvp

    else:
        print(f"error: La cantidad vendida de {producto} no es válida.")

        return tv
    
def proceso():

    productosvendidos = {}

    try:
        for _ in range (5):
            producto = input("Ingrese el nombre del producto vendido: ")
            cantidad = int(input("Ingrese la cantidad vendida: "))
            productosvendidos[producto] = cantidad
    
    except ValueError:
        print("Error: Por favor ingrese un valor numérico para la cantidad.")
    
    finally:
        tv = ctv(productosvendidos)
        print(f"Total de ventas del día: ${tv:.2f}")

proceso()