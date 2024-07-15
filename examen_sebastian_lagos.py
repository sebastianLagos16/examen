import random
import csv
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]


def asignar_sueldos_aleatorios ():
    sueldos = [random.randint(300.000,2500000)for trabajadores in range (10)]
        
    print ("Sueldos generados aleatoriamente")
    

    
def salir_programa ():
    print ("Finalizando programa")
    print ("programa desarrollado por sebastian lagos")
    print ("RUT 19.997.124-7")
    exit ()
def menu():
    while  True:
        
            print("Seleccione una opción")
            print("1. Asignar sueldos aleatorios")
            print("2. Clasificar sueldos")
            print("3. Ver estadísticas.")
            print("4. Reporte de sueldos")
            print("5. Salir del programa")
            opcion = int (input("ingrese una opcion valida"))
            if opcion == 1:
                asignar_sueldos_aleatorios()
            if opcion == 5:
                salir_programa()
                
        
            
menu()
