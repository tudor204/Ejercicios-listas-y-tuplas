"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
palabra = input("Introduce una palabra: ")
palabra_invertida = palabra[::-1]
if palabra == palabra_invertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    