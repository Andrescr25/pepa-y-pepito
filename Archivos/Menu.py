
from Insercion import Insercionn 
from Insercion import Busqueda
from Insercion import Eliminar
from Insercion import Modificar

def menu():
    print("Veterinaria Jocris\nQue deseas hacer?")
    print("1) Insercion\n2) Busqueda\n3) Eliminar\n4) Modificar\n5) Reportes")
    opcion = int(input("> "))

    if opcion == 1:
        Insercionn()
        menu()
        

    if opcion == 2:
        Busqueda()
    
    if opcion == 3:
        Eliminar()
    
    if opcion == 4:
        Modificar()
menu()



    

        

