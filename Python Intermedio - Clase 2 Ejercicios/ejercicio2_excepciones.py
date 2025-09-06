"""Ejercicio 2 
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario."""  

n1 = float (input("ingrese el dividendo : "))
n2 = str(input("ingrese el divisor : "))
try : 
    resultado = n1/n2
    print (f"ejecutado sin problemas. \n")
except TypeError as e :   
    print(f"Ambos deben ser numeros !! \nError : {TypeError} {e}")
else :
    print(f"Resultado : {resultado:.2}\n")