#Apuntes
""" Tuplas.
    son estructuras de datos parecidas a las listas
    pero con algunas diferencias.

    -Son inmutables (No se pueden modificar).
    -Se definen mediante ().
    -Son una secuencia de elementos.

"""

#Forma 1 de definir una tupla 
tupla_1 = (1,2,3,4,5)
#Forma 2 de definir una tupla 
tupla_2= 1,2,3,4,5,6,7,"Holi"
#Forma 3 de definir una tupla 
tupla_3= tuple([1,"Chuau",333,True])
print(type(tupla_3))

#Acceder a datos
print(tupla_3[1])
#Rangos dentro de las tuplas
print(tupla_3[1:3])

