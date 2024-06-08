import csv

def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"Archivo {nombre_archivo} creado exitosamente.")

def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return list(csv.reader(archivo))

datos_csv = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Juan', 30, 'Concepción'],
    ['Carlos', 22, 'Viña del mar'],
    ['Estela', 25, 'Puerto Montt'],
    ['Maria', 21 , 'Puente alto']
]

crear_archivo_csv('ejemplo.csv', datos_csv)