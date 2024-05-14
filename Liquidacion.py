def calcular_sueldo_bruto(horas_trabajadas, tarifa_hora):
    return horas_trabajadas * tarifa_hora

def calcular_descuento_afp(sueldo_bruto):
    return sueldo_bruto * 0.1

def calcular_sueldo_neto(sueldo_bruto, descuento_afp):
    return sueldo_bruto - descuento_afp

def inicio():
    horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
    tarifa_hora = float(input("Ingrese la tarifa por hora: "))
    sueldo_bruto = calcular_sueldo_bruto(horas_trabajadas, tarifa_hora)
    descuento_afp = calcular_descuento_afp(sueldo_bruto)
    sueldo_neto = calcular_sueldo_neto(sueldo_bruto, descuento_afp)

    print("Liquidación de Sueldo")
    print("======================")
    print(f"Sueldo Bruto: {sueldo_bruto}")
    print(f"Descuento AFP: {descuento_afp}")
    print("======================")
    print(f"Sueldo Neto: {sueldo_neto}")

inicio()  





