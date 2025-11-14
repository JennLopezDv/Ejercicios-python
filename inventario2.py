

############ LÓGICA DE FUNCIÓN PARA CALCULAR INVENTARIO ########################

def agregar_producto(lista):
    
    producto = {} #Diccionario vacío.
    while True:
        totalProd = input("Ingrese la cantidad de productos a ingresar: ")
        if totalProd.isdigit(): #Condición para validar que el dato ingresado sea digíto.
            totalProd = int(totalProd) #Si se cumple, lo convierte a entero.
            break 
        else:
            print("Debe ingresar un número entero") #En caso que la condición anterior no se cumpla, mostrar al usuario error.

    for i in range(1, totalProd+1):

        #Validar Nombre.
        while True:  
            nombre = input("Ingresa nombre del producto: ")    
            if nombre.isdigit() or nombre == "":  #Condición para validar si el dato ingresado es digíto o esta vacío.
                print("Debe ingresar un nombre válido") #Imprima error.
            else:
                break 

        # Validar Precio.
        while True:
            precio_input = input("Ingrese el precio del producto: ")
            # Verificamos si el precio es un número válido (aceptamos decimales)
            if precio_input.replace('.', '', 1).isdigit():
                precio = float(precio_input)
                if precio <= 0:
                    print("El valor no puede ser 0 o negativo, intente de nuevo.")
                else:
                    break
            else:
                print("Valor inválido, ingrese un número válido.")

        # Validar Cantidad (solo enteros)
        while True:
            cantidad_input = input("Ingrese la cantidad de productos que lleva el cliente: ")
            if cantidad_input.isdigit():
                cantidad = int(cantidad_input)
                break
            else:
                print("Valor inválido, ingrese un número entero positivo.")

        producto = {"nombre": nombre,
                    "precio": precio, 
                    "cantidad": cantidad} #Aquí se ingresan datos al diccionario
        lista.append(producto) #Se agrega el product recien creado a  la lista.

    return lista

####################### Mostrar inventario ############################

def mostrar_inventario(lista):
    if not lista: #Condición para validar si la lista esta vacía.
        print("Inventario vacío: No hay productos. ")
    
    else:
        for producto in lista:
            print(f"producto: {producto['nombre']} | precio: {producto['precio']} | cantidad: {producto['cantidad']}") 


############# Calcular estadíticas ##################
def calcular_estadisticas(lista):
    if not lista: #Condición para validar si la lista esta vacía.
        print("Inventario vacío: No hay productos para hacer el cálculo.")
    else:
        cantProd = 0
        totalInventario =0
        for producto in lista:
            totalInventario += producto["precio"] * producto["cantidad"]
            cantProd += 1

        print(f"Valor total inventario: {totalInventario} \nCantidad de productos: {cantProd}")

######################## MENÚ ############################
inventario = []
def menu():
    while True:
        print("Bienvenido, ¿Qué acción desea realizar?")
        print("1. Agregar producto.")
        print("2. Mostrar inventario.")
        print("3. Calcular estadísticas.")
        print("4. Salir.")

        opcion = input("Seleccione la opción: ")

        if opcion in ("1","2","3","4"):
            if opcion == "1":
                print("Opción elegida Agregar producto.")
                agregar_producto(inventario)
            elif opcion == "2":
                mostrar_inventario(inventario)
            elif opcion == "3":
                calcular_estadisticas(inventario)
            elif opcion == "4":
                print("Saliendo...")      
                break

        else: 
            print("---> ¡Opción inválida! <---")
   
menu()


"""Descripción funcionamiento:
Primero está la función agregar_producto, que recibe una lista y crea un diccionario para guardar los datos que ingresa el usuario. 
La función comienza pidiendo cuántos productos se agregarán, validando que el valor sea un número entero. 
Luego, por cada producto, se solicita el nombre, el precio y la cantidad, usando ciclos while para asegurarse de que cada dato sea válido: 
el nombre no puede ser número ni estar vacío, el precio debe ser un número positivo y la cantidad debe ser un entero. 
Cuando todos los datos son correctos, se guardan en un diccionario y este se agrega a la lista, que finalmente se retorna.
La función mostrar_inventario recibe la lista y verifica si está vacía. 
Si no hay productos, muestra un mensaje. Si sí los hay, recorre la lista con un for e imprime el nombre, precio y cantidad de cada producto con un formato ordenado.
Luego está la función calcular_estadisticas, que también revisa si la lista está vacía. 
Si tiene productos, define variables para el total del inventario y la cantidad de productos. 
Recorre la lista, multiplica precio por cantidad para obtener el valor total de cada producto y lo suma al total general. 
También lleva un conteo de cuántos productos hay. Al final imprime el valor completo del inventario y la cantidad total registrada.
Finalmente, el código tiene un menú principal que trabaja con una lista vacía llamada inventario. 
El menú se ejecuta en un ciclo infinito, mostrando opciones del 1 al 4: agregar producto, mostrar inventario, calcular estadísticas o salir. 
Se valida que la opción ingresada sea correcta y, dependiendo de la elección, se llama a la función correspondiente. 
Si la opción no existe, muestra un mensaje de error. 
El ciclo se detiene cuando el usuario elige salir."""







