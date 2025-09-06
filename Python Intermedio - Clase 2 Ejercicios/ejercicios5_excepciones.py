import os
import datetime
"""Ejercicio 5 
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario."""

def dividir_numeros():
    while True :
        try:
            num1 = input("Introduce el primer número: ")
            num2 = input("Introduce el segundo número: ")

            # Convertir las entradas a números. Esto puede lanzar ValueError si la entrada no es un número.
            numero1 = float(num1)
            numero2 = float(num2)

            resultado = numero1 / numero2
            print(f"\nEl resultado de la división entre {numero1} y {numero2} es: {resultado:.2}\n")

        except ValueError:
            print(f"\nError: El primer número introducido no es válido.{ValueError}\n")
        except ZeroDivisionError:
            print(f"\nError: No se puede dividir por cero.{ZeroDivisionError}\n")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}\n")

dividir_numeros()

