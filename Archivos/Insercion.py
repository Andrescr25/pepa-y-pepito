def Insercionn():
    print("Que deseas incluir?")
    print("1)Pais\n2)Ciudad\n3)Cliente\n4)Mascota\n5)Visita\n6)Tratamiento\n7)Medicacion")
    opcion = int(input(">"))
    
    if opcion == 1:
        with open("Paises.txt", "r") as archivo:
            paises_existentes = [linea.split(";")[1].strip() for linea in archivo]
        
        nombre_pais = input("Escribe el pais que deseas insertar: ")
            
        if nombre_pais in paises_existentes:
            print("El pais ya existe")
        else:
            numeros_usados = [int(linea.split(";")[0]) for linea in open("Paises.txt")]
            num_pais = 1
            while num_pais in numeros_usados:
                num_pais += 1
            with open("Paises.txt", "a") as archivo:
                archivo.write(f"{num_pais};{nombre_pais}\n")
                print(f"\nEl pais {nombre_pais} ha sido agregado con exito\n") 
                    
    elif opcion == 2:
        print("Has escogido Ciudad")
            
    elif opcion == 3:
        with open("Clientes.txt", "r") as archivo:
            clientes_existentes = [linea.split(";")[1].strip() for linea in archivo]
        
        nombre_cliente = input("Escribe el nombre del cliente que deseas insertar: ")
            
        if nombre_cliente in clientes_existentes:
            print("El cliente ya existe")
        else:
            numeros_usados = [int(linea.split(";")[0]) for linea in open("Clientes.txt")]
            num_cliente = 1
            while num_cliente in numeros_usados:
                num_cliente += 1
            with open("Clientes.txt", "a") as archivo:
                archivo.write(f"{num_cliente};{nombre_cliente}\n")
                print(f"\nEl cliente {nombre_cliente} ha sido agregado con exito\n") 

    elif opcion == 4:
        with open("Clientes.txt", "r") as archivo:
            clientes_existentes = [linea.split(";")[1].strip() for linea in archivo]
        nombre_cliente = input("Escribe el nombre del dueño de la mascota: ")
        
        if nombre_cliente in clientes_existentes:
            with open("Mascotas.txt", "r") as archivo_mascotas:
                numeros_usados = [int(linea.split(";")[1]) for linea in archivo_mascotas if linea.startswith(str(num_cliente))] 
                num_mascota = 1
                while num_mascota in numeros_usados:
                    num_mascota += 1
                with open("Mascotas.txt", "a") as archivo:
                    nombre_mascota = input("Escriba el nombre de la mascota: ")
                    archivo.write(f"{num_cliente};{num_mascota};{nombre_mascota}\n")
                    print(f"\nLa mascota {nombre_mascota} ha sido agregada con éxito\n") 
        else:
            print("El cliente no existe")






   
        
        
    if opcion==5:
       print("Has escogido Visita")
    if opcion==6:
       print("Has escogido Tratamiento")
    if opcion==7:
        print("Has escogido Visita")
    if opcion==8:
       print("Has escogido Medicacion")














def Busqueda():
    print("Que deseas buscar?")
    print("1)Pais\n2Ciudad\n3)Cliente\n4)Mascota\n5)Visita\n6)Tratamiento\n7)Medicacion")
    opcion=int(input(">"))
    if opcion==1:
       print("Has escogido Pais")
    if opcion==2:
       print("Has escogido Ciudad")
    if opcion==3:
       print("Has escogido Cliente")
    if opcion==4:
       print("Has escogido Visita")
    if opcion==5:
       print("Has escogido Tratamiento")
    if opcion==6:
        print("Has escogido Visita")
    if opcion==7:
       print("Has escogido Medicacion")
def Eliminar():
    print("Que deseas Eliminar?")
    print("1)Pais\n2Ciudad\n3)Cliente\n4)Mascota\n5)Visita\n6)Tratamiento\n7)Medicacion")
    opcion=int(input(">"))
    if opcion==1:
       print("Has escogido Pais")
    if opcion==2:
       print("Has escogido Ciudad")
    if opcion==3:
       print("Has escogido Cliente")
    if opcion==4:
       print("Has escogido Visita")
    if opcion==5:
       print("Has escogido Tratamiento")
    if opcion==6:
        print("Has escogido Visita")
    if opcion==7:
       print("Has escogido Medicacion")
def Modificar():
    print("Que deseas modificar?")
    print("1)Pais\n2Ciudad\n3)Cliente\n4)Mascota\n5)Visita")
    opcion=int(input(">"))
    if opcion==1:
       print("Has escogido Pais")
    if opcion==2:
       print("Has escogido Ciudad")
    if opcion==3:
       print("Has escogido Cliente")
    if opcion==4:
       print("Has escogido Visita")
    if opcion==5:
       print("Has escogido Tratamiento")
    
    
