"""Ejercicio 1 
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario."""

n1 = float (input("ingrese el dividendo : "))
n2 = float(input("ingrese el divisor : "))
try : 
    resultado = n1/n2
    print (f"ejecutado sin problemas. \n")
except ZeroDivisionError as e:   
    print(f"No se puede dividir por cero !! \nError : {ZeroDivisionError}")
else :
    print(f"Resultado : {resultado:.2}\n")
