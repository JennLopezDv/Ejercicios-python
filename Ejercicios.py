#1. Panadería Don Pacho
# cantidad = int(input("Ingrese la cantidad de panes a comprar: "))
# precio = 300
# totalSinDes= (cantidad * precio)
# desc10 =  totalSinDes * 0.10
# desc20 = totalSinDes * 0.20
# total10= totalSinDes - desc10
# total20 = totalSinDes - desc20

# if cantidad <= 0:
#     print("Cantidad inválida")

# elif cantidad> 50:
#     print(f"Usted compró {cantidad} panes, tiene un descuento del 20 % por valor de {desc20} paga un todal de {total20}")
    

# elif cantidad > 20:
#     print(f"Usted compró {cantidad} panes, tiene un descuento del 10 % por valor de {desc10} paga un todal de {total10}")

# else:
#     print(f"Total a pagar {totalSinDes}")
    

#2. Cine “La Estrella” — Tarifas por edad

# edad = int(input("Ingrese su edad: "))

# if edad < 0:
#     print("Edad inválida.")
    
# elif edad >= 60:
#     print("Total a pagar: $4.000")    
   
# elif edad >= 12:
#     print("Total a pagar: $8.000")
    
# elif edad < 5:
#     print("Entrada gratis")
    
# else:
#     print("Total a pagar: $5.000")
    
#3. Gimnasio “Solo Leveling Fit” — Motivación + Bono

# dias = int(input("Ingrese la cantidad de días que entrenó esta semana: "))
# puntos = 0
# if dias >= 4:
#     print("¡Excelente disciplina! ganas 1 punto de energía")
#     puntos += 1
    
# elif dias > 2:
#     print("Bien, pero puedes dar más")
    
# elif dias >= 0:
#     print("No aflojes, tú puedes mejorar")
    
# else:
#     print("Ingrese solo números positivos")

#4. Heladería “Frosty” — Sabor y topping

<<<<<<< HEAD
# Sabores y precios:

#     chocolate → $4.000
#     vainilla → $3.500

# Opcional: topping cuesta $1.000.

# print("Bienvenido a la Heladería Frosty")
# print ("¿Qué sabor de helado deseas? ")
# print ("1. Chocolate.")
# print ("2. Vainilla.")

=======
>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)
# chocolate = 4000
# vainilla = 3500
# topping= 1000
# totalConTop1= chocolate + topping
# totalConTop2 = vainilla + topping
# totalSinTop1 = chocolate
# totalSinTop2= vainilla

<<<<<<< HEAD
# opcionSabor=int(input("Selecciona la opción que deseas: "))
=======
# print("Bienvenido a la Heladería Frosty")
# print ("¿Qué sabor de helado deseas? ")
# print ("1. Chocolate.")
# print ("2. Vainilla.")

# opcionSabor=int(input("Ingrese el número de la opción que deseas: "))
>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)

# if opcionSabor == 1:
#     print("¿Quiéres adicionar algún topping?")
#     print("1. Sí")
#     print("2. No")
<<<<<<< HEAD
#     opcionRespuesta = int(input("Seleccione su respuesta: "))
#     if opcionRespuesta == 1:
#         print(f"El valor total es de: {totalConTop1}")
#     elif opcionRespuesta == 2: 
#         print(f"El valor total es de: {totalSinTop1}")
=======
#     opcionRespuesta = int(input("Ingrese el número de su respuesta: "))
#     if opcionRespuesta == 1:
#         print(f"¡Disfruta tu helado! Total a pagar helado + topping: {totalConTop1}")
#     elif opcionRespuesta == 2: 
#         print(f"¡Disfruta tu helado!. Total a pagar: {totalSinTop1}")
>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)
#     else:
#         print("Opción no válida")

# elif opcionSabor == 2:
#     print("¿Quiéres adicionar algún topping?")
#     print("1. Sí")
#     print("2. No")
<<<<<<< HEAD
#     opcionRespuesta = int(input("Seleccione su respuesta: "))
#     if opcionRespuesta == 1:
#         print(f"El valor total es de: {totalConTop2}")
#     elif opcionRespuesta == 2: 
#         print(f"El valor total es de: {totalSinTop2}")
=======
#     opcionRespuesta = int(input("Ingrese el número de su respuesta: "))
#     if opcionRespuesta == 1:
#         print(f"¡Disfruta tu helado!. Total a pagar helado + topping:: {totalConTop2}")
#     elif opcionRespuesta == 2: 
#         print(f"¡Disfruta tu helado!. Total a pagar:: {totalSinTop2}")
>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)
#     else:
#         print("Opción no válida")
       
# else:
<<<<<<< HEAD
#     print ("Sabor no disponible")
=======
#     print ("Opción no disponible")

>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)

#5. Librería “El Saber” — Descuento estudiante + cupón
# Libro cuesta $25.000.

#     Si es estudiante → 15% descuento
#     Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

# Validar:

#     Si no es estudiante, el cupón no aplica.
#     Si ingresa cupón incorrecto, ignorarlo.

# Mostrar total.
<<<<<<< HEAD
# 

#6. Parqueadero "RapidCar" -Tarifa escalonada.
#7. Restaurante "El sabor Colombiano" -Menú + bebida opcional +IVA

# precioMenu = 12000
# iva = 0.08
# bebida = 3000

# tarifaConBebida = precioMenu + bebida

# impuestoIva = tarifaConBebida * iva
# impuestoIva2 = precioMenu * iva

# totalConBebida = tarifaConBebida + impuestoIva
# totalSinBebida = precioMenu + impuestoIva2

# print ("Bienvenido al Restaurante El sabor Colombiano.")
# bebida = (input("¿Desea agregar bebida?: Sí, No ")).lower()

# if bebida == "si":
#     print("Total a pagar:",totalConBebida )

# else:
#     print ("Total a pagar:",totalSinBebida)

#8. Empresa TecnoPlus -Evaluación compuesta.
# notaPruebaTecnica = float(input("Ingrese la nota de la prueba Técnica: "))
# notaPruebaLogica = float(input("Ingrese la nota de la pruena Lógica: "))
=======
costoLibro = 25000
descuesto = costoLibro * 0.15
totalDesc = costoLibro - descuesto
cupon = 0.10
valorCupon = totalDesc * cupon
totalCupon = totalDesc - valorCupon

print("Bienvenido a la Librería El saber.")
print("¿Desea comprar un libro?")
print("1. Sí")
print("2. No")

opcionCompra = int(input("Seleccione la opción: "))

if opcionCompra == 1:
    print("¿Es estudiante?")
    print("1. Sí")
    print("2. No")
    opcionPersona = int(input("Seleccione la opción: "))

    if opcionPersona == 1:
        print("Usted tiene un descuento del 15% en el costo de su libro.")
        print(f"Costo total: {totalDesc}")
        print("¿Tiene cupón?")
        print("1. Sí")
        print("2. No")
        opcionCupon = int(input("Seleccione la opción: "))

        if opcionCupon == 1:
            valorCupon = (input("Ingrese cupón: "))
            if valorCupon == "LIBRO10":
                print("Adicional a tu descuesto tienes un 10% descuento más en tu compra.")
                print(f"Costo total: {totalCupon}")

            else:
                print(f"Error al ingresar cupón. Valor total: {totalDesc}")                   
         

        elif opcionCupon == 2:
            print(f"Valor Total: {totalDesc}")
            
    elif opcionPersona == 2:
        print (f"Valor Total: {costoLibro}")    

else: 
    print("Esperamos verte pronto.")

# 6. Parqueadero “RapidCar” — Tarifa escalonada

# hora = 2000
# cantidadHoras = int(input("Ingresa la cantidad de horas: "))
# totalPagar = hora * cantidadHoras
# multa = 5000

# if cantidadHoras <0:
#     print("Cantidad inválidad.")

# elif cantidadHoras in range (5):
#     if cantidadHoras == 0:
#         totalPagar = hora
#     print(f"Total a pagar: ", totalPagar)

# else:
#     print(f"Total a pagar: ", totalPagar + multa)


#7. Restaurante el Sabor Colombiano, Menú + bebida opcional + IVA

# menu = 12000
# bebida = 3000
# iva = 0.08

# print("Bienvenido al restaurante el Sabor Colombiano.")
# opcionBebida = int(input("Costo del Menú $12.000, ¿Desea incluír bebida?: 1. Sí, 2. No ---> "))

# opcion1 = (menu + bebida) * iva
# opcion2 = menu * iva

# total1= menu + bebida + opcion1
# total2 = menu + opcion2

# if opcionBebida == 1:
#     print("Total a pagar: ", total1)

# elif opcionBebida == 2:
#     print("Total a pagar: ", total2)
# else:
#     print("Opción no válida.")

#8. Empresa TecnoPlus - Evaluación compuesta.
>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)

# porcentajePruebaTecnica = 0.70
# porcentajePruebaLogica = 0.30

<<<<<<< HEAD
# totalTecnica = notaPruebaTecnica * porcentajePruebaTecnica
# totalLogica= notaPruebaLogica * porcentajePruebaLogica

# notaFinal = totalTecnica + totalLogica

# if notaFinal <2:
#     print("Reprobado")

# elif notaFinal <3:
#     print("Revisión")

# else: 
#     print("Aprobado")

#9. Supermercado AhorroMax -Descuentos y envío

# valorProducto = 2000
# descuento10 = 0.05
# descuesto30 = 0.15
# envio = 5000

# cantidadProductos = int(input("Ingrese la cantidad de productos: "))
# tarifa = cantidadProductos * valorProducto
# precio = tarifa

# masDe10 = tarifa * descuento10
# masDe30= tarifa * descuesto30

# totalDescuento10 = tarifa - masDe10
# totalDescuento30 = tarifa - masDe30

# if precio < 50000:
#     print("El total a pagar es: ", totalDescuento10 + envio)
    
#10. Club Noche Estelar -Acceso + validación documento
IngresarDocumento = int(input("Por favor ingrese su número de documento: "))
IngresoEdad = int(input("Ingrese su edad: "))

if IngresoEdad < 0:
    print("Edad no válida.")
    
elif IngresoEdad < 18:
    print("Entrada denegada")
    
else:
    print("Debe presentar documento.")
=======
# notaTecnica = float(input("Ingrese la nota de la prueba Técnica: "))
# notaLogica = float(input("Ingrese la nota de la prueba Lógica: "))

# valorTecnica = notaTecnica * porcentajePruebaTecnica
# valorLogica = notaLogica * porcentajePruebaLogica

# notaFinal = valorTecnica + valorLogica

# if notaFinal <2:
#     if notaFinal <0:
#         print("Valor inválido.")
#     print(f"{notaFinal}, Reprobado")

# elif notaFinal >= 2 and notaFinal < 3:
#     print(f"{notaFinal}, Revisión")

# elif notaFinal <=5:
#     print(f"{notaFinal}, Aprobado")
    
# else:
#     print("Valor no permitido")


#9. Supermercado Ahorro Max -DEscuesto y envío.

# producto = 2000
# mas10  = 0.05
# mas30 = 0.15
# envio = 5000

# cantidadProductos = int(input("Ingresar cantidad de Productos: "))
# totalSinDescuesto = cantidadProductos * producto
# descuestoMas10 = totalSinDescuesto * mas10
# descuestoMas30 = totalSinDescuesto * mas30

# totalPagar = totalSinDescuesto - descuestoMas10
# totalPagar2 = totalSinDescuesto - descuestoMas30

# if cantidadProductos <=0:
#     print("Error. Ingrese cantidad correcta.")

# elif cantidadProductos <=9:
#     print("Total a pagar: ", totalSinDescuesto + envio)

# elif cantidadProductos >=30:    
#     print("Total a pagar: ", totalPagar2)

# elif cantidadProductos >=10:    
#     print("Total a pagar: ", totalPagar)

# if totalPagar < 50000:
#     totalPagar = totalPagar + envio

#10. Club Noche Estelar -Acceso + validación documento
# IngresarDocumento = int(input("Por favor ingrese su número de documento: "))
# IngresoEdad = int(input("Ingrese su edad: "))

# if IngresoEdad < 0:
#     print("Edad no válida.")
    
# elif IngresoEdad < 18:
#     print("Entrada denegada")
    
# else:
#     print("Debe presentar documento.")
     

>>>>>>> bd94108 (Se terminaron de realizar los demás ejercicios.)
