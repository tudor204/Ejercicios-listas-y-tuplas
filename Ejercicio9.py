"""
Escribir un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""

precios = [50,75,46,22,80,65,8]

minimo = maximo = precios[0]
for precio in precios:
    if precio < minimo:
        minimo = precio
    elif precio > maximo:
        maximo = precio
print("El mínimo es " + str(minimo))
print("El máximo es " + str(maximo))