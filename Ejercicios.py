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

# Sabores y precios:

#     chocolate → $4.000
#     vainilla → $3.500

# Opcional: topping cuesta $1.000.

# print("Bienvenido a la Heladería Frosty")
# print ("¿Qué sabor de helado deseas? ")
# print ("1. Chocolate.")
# print ("2. Vainilla.")

# chocolate = 4000
# vainilla = 3500
# topping= 1000
# totalConTop1= chocolate + topping
# totalConTop2 = vainilla + topping
# totalSinTop1 = chocolate
# totalSinTop2= vainilla

# opcionSabor=int(input("Selecciona la opción que deseas: "))

# if opcionSabor == 1:
#     print("¿Quiéres adicionar algún topping?")
#     print("1. Sí")
#     print("2. No")
#     opcionRespuesta = int(input("Seleccione su respuesta: "))
#     if opcionRespuesta == 1:
#         print(f"El valor total es de: {totalConTop1}")
#     elif opcionRespuesta == 2: 
#         print(f"El valor total es de: {totalSinTop1}")
#     else:
#         print("Opción no válida")

# elif opcionSabor == 2:
#     print("¿Quiéres adicionar algún topping?")
#     print("1. Sí")
#     print("2. No")
#     opcionRespuesta = int(input("Seleccione su respuesta: "))
#     if opcionRespuesta == 1:
#         print(f"El valor total es de: {totalConTop2}")
#     elif opcionRespuesta == 2: 
#         print(f"El valor total es de: {totalSinTop2}")
#     else:
#         print("Opción no válida")
       
# else:
#     print ("Sabor no disponible")

#5. Librería “El Saber” — Descuento estudiante + cupón
# Libro cuesta $25.000.

#     Si es estudiante → 15% descuento
#     Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

# Validar:

#     Si no es estudiante, el cupón no aplica.
#     Si ingresa cupón incorrecto, ignorarlo.

# Mostrar total.
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

# porcentajePruebaTecnica = 0.70
# porcentajePruebaLogica = 0.30

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