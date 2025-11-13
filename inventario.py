"""Variables, y tipo de datos: string, float, int"""

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

costo_total = precio * cantidad
print(f"Producto: {nombre} | Precio unidad: {precio} | Cantidad: {cantidad} | Total: {costo_total}")
    
   

#EXPLICACIÓN FUNCIONAMIENTO:
"""Se crearon 3 variables: nombre, precio, cantidad, y costo total. Para cada una de ellas se definio un tipo de dato (string, float, int, respectivamente),
para hacer el código más limpio se organizo en bloques con sus respectivos comentarios:"""

"""#Bloque 1. Validad Nombre: 
Se inicia un ciclo while True, es decir, un bucle infinito.
que estará pidiendo el nombre del producto constantemente mediante input(), hasta que el usuario ingrese un valor válido.
Una vez el usuario haya ingresado un dato, valida si se cumple la condición, preguntando si el valor ingresado es un digito con .isdigit() o si esta vacío,
de ser así, muestre al usuario en pantalla por medio de un print "Debe ingresar un nombre válido".
Pero Si No es dígito ni está vacío, rompa el ciclo. """

"""#Bloque 2. Validad Precio: 
Se inicia un ciclo while True, es decir, un bucle infinito 
que estará pidiendo el precio del producto constantemente mediante input(), hasta que el usuario ingrese un valor válido.
Una vez ingresado el dato, el programa utiliza .replace('.', '', 1) para permitir que el número tenga como máximo un punto decimal, 
y luego usa .isdigit() para verificar que el resto del contenido sea numérico.
Si esta validación se cumple, el valor ingresado se convierte a tipo float y se guarda en la variable precio.
Después de eso, se revisa si precio es menor o igual a 0. 
Si ese es el caso, se muestra el mensaje "El valor no puede ser 0 o negativo, intente de nuevo.", 
y el ciclo continúa pidiendo un nuevo valor.
Si el valor es válido (es decir, si es un número mayor que 0), entonces el programa hace break y sale del bucle.
Por otro lado, si el dato ingresado no cumple las condiciones de número válido, 
se muestra el mensaje "Valor inválido, ingrese un número válido.", y el programa volverá a pedir el precio."""

"""#Bloque 3. Validar Cantidad: 
Se inicia un ciclo while True, es decir, un bucle infinito que estará pidiendo la cantidad de productos mediante input(), hasta que el usuario ingrese un valor válido.
Una vez ingresado el dato, el programa valida con .isdigit() que el valor ingresado sea completamente numérico.
Si esta validación se cumple, el valor se convierte a tipo int y se guarda en la variable cantidad.
En ese momento, el programa ejecuta break y sale del bucle.
Por el contrario, si el dato ingresado no cumple con la condición de ser un número entero positivo, se muestra el mensaje:
"Valor inválido, ingrese un número entero positivo.", y el ciclo vuelve a pedir la cantidad hasta recibir un número válido. """

"""#VARIABLE, costo_total
Aquí se guardará el dato de la multiplicación entre el precio por la cantidad. Y mostrará en pantalla, de acuerdo al formato realizado, 
el mensaje de los valores guardados en: Producto (el nombre), Precio unitario, cantidad, y total"""

