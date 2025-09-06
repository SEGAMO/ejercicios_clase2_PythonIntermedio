"""Ejercicio 3
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra """  

mi_diccionario = {"nombre": "Ana", "edad": 30}
clave_a_buscar = input("Ingrese dato : ")

try:
    valor = mi_diccionario[clave_a_buscar]
    print(f"El valor para '{clave_a_buscar}' es: {valor}")
except KeyError as e:
    print(f"Error: La clave '{clave_a_buscar}' no se encontró en el diccionario. {KeyError}{e}")