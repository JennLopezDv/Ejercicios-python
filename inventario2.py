

############ LÓGICA DE FUNCIÓN PARA CALCULAR INVENTARIO ########################

def agregar_producto(lista):
    
    producto = {}

    totalProd = int(input("Ingrese la cantidad de productos a ingresar: "))

    for i in range(1, totalProd+1):

        #Validar Nombre.
        while True:  
            nombre = input("Ingresa nombre del producto: ")    
            if nombre.isdigit() or nombre == "":  
                print("Debe ingresar un nombre válido") 
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
                    "cantidad": cantidad}
        lista.append(producto)

    return inventario

        # costo_total = precio * cantidad
        # print(f"Producto: {nombre} | Precio unidad: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

####################### Mostrar inventario ############################

def mostrar_inventario(lista):
    for producto in lista:
        print(producto) 

######################## MENÚ ############################
inventario = []

while True:
    print("Bienvenido, ¿Qué acción desea realizar?")
    print("1. Agregar producto.")
    print("2. Mostrar inventario.")
    print("3. Calcular estadísticas.")
    print("4. Salir.")
    
    opcion = int(input("Seleccione la opción: "))

    if opcion != 0:
        if opcion == 1:
            print("Opción elegida Agregar producto.")
            agregar_producto(inventario)
        elif opcion == 2:
            mostrar_inventario(inventario)
        elif opcion == 3:
            print("Opción elegida Calcular estadísticas.")
        elif opcion == 4:
            print("Saliendo...")      
            break

    else: 
        print("---> ¡Opción inválida! <---")
   






