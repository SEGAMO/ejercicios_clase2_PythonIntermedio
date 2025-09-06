import os
import datetime
"""Ejercicio 4 
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe."""

nombre_archivo = input("Ingrese el nombre del archivo a ejecutar : ")
fecha = datetime.datetime.now()
try:
    archivo = open (nombre_archivo,"r")
    print(f"{archivo}\n")
except FileNotFoundError as e :
    print (f"""
           No se encontro el Archivo Solicitado !! 
           \n {FileNotFoundError}{e}
           """)
    
    if input('\nDesea crear el Archivo ? (y/n) : ') == 'y':
        with open (nombre_archivo,"w")as f:
            f.write(f"Archivo {nombre_archivo} creado el {fecha}")
            print (f"\nArchivo : {nombre_archivo} creado exitosamente !! ")
            print (f"\nEl Archivo {nombre_archivo} esta listo para usarse !!\n")
           
    else :
        print("Adios")
        os.system("pause")
        os.system("cls")
else : 
    os.system("pause")