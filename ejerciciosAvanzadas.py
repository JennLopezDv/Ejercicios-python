"""1. Restaurante “Buen Sabor” – Cálculo de propina
Como mesero, quiero una función calcular_propina(total_cuenta) 
que reciba el valor total de la cuenta y calcule la propina del 10%.
Si el total es mayor de $100.000, aplicar el 15%.
El programa debe mostrar el total final a pagar."""

# def calcular_propina(total_cuenta):
#     if total_cuenta > 100000:
#         porc_propina = 0.15
#         total_cuenta = total_cuenta + (porc_propina * total_cuenta)
#         print("Total a pagar: ",total_cuenta)

#     else:
#         porc_propina =  0.10
#         total_cuenta = total_cuenta + (porc_propina * total_cuenta)
#         print("Total a pagar: ",total_cuenta) 

# total= int(input("Total cuenta: "))

# calcular_propina(total)

"""2. Gimnasio “Level Up” – Control de repeticiones.
Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las repeticiones del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”."""

# def repeticiones(n):
#     for i in range(1, n+1):
#         if i %2 == 0:
#             print(f"Repetición: {i}, ¡Excelente forma!")

#         else: 
#             print(f"Repetición: {i}, ¡Mantén el ritmo!")

# cantidad = int(input("Ingresa el valor de repeticiones a realizar: "))

# repeticiones(cantidad)

"""3. Tienda “LoopShop” – Descuentos acumulados
Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
Si el precio supera 50.000, aplicar 10% de descuento.
Al final, mostrar la suma total de las compras con descuento."""

# def aplicar_descuentos():
#     valor_compra = 1
#     grantotal = 0
#     while valor_compra != 0:
#         valor_compra = int(input("Ingrese precio: "))
#         sindesc = 0
        
             
#         if valor_compra > 50000:
#             condesc = 0
#             total = valor_compra - (valor_compra * 0.10)
#             print("Valor a pagar por esta venta: ",total)
#             condesc += total
#             grantotal += condesc
#         else:
#              sindesc += sindesc
#              grantotal += sindesc
          
#     else:
#             print("Total a pagar con descuento: ",condesc)
#             print("Total a pagar sin descuento: ",sindesc)
#             print("Total a pagar en general: ", grantotal)

# aplicar_descuentos()

"""4. Banco “PythonBank” – Evaluador de crédito
Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:

    Apruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.
    Si no cumple, mostrar “Crédito rechazado”.
    Usar condicionales dentro de la función."""

# def evaluar_credito(ingresos, edad):
#     if ingresos > 2000000:
#         if edad >= 25 and edad <= 60:
#             print("¡Crédito aprobado!")
#         else: 
#             print("Crédito rechazado por edad!")
#     else:
#         print("¡Crédito rechazado!")


# ingresos = int(input("Ingrese valor correspondiente a sus ingresos mensuales: "))
# edad = int(input("Ingrese su edad: "))

# evaluar_credito(ingresos, edad)

"""5. Escuela “Aprende Más” – Promedio de notas
Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
Debe repetirse para varios estudiantes usando un while."""

# def promedio_notas(a, b, c):
#     promedio = (a+b+c)/3
#     if promedio >= 3:
#         print(f"{promedio}: Estudiante aprobado.")
#     else: 
#         print(f"{promedio}: Estudiante Reprobado.")           
   

# numero_Estudiantes = int(input("Ingrese el total de estudiantes: "))
# i=1

# while i <= numero_Estudiantes:
#     nota_Uno = float(input("Ingrese primer nota: "))
#     nota_Dos = float(input("Ingrese segunda nota: "))
#     nota_Tres = float(input("Ingrese tercer nota: "))
#     promedio_notas(nota_Uno, nota_Dos, nota_Tres)
#     i+=1
# else: 
#     print("Terminamos")

"""6. Estación “LoopBus” – Simulador de pasajeros
Como conductor, quiero una función simular_viaje(pasajeros) que recorra con un for cada pasajero y muestre “Pasajero X a bordo”.
Si llega a 10 pasajeros, mostrar “Bus lleno” y detener el bucle."""

# def simular_viaje(pasajeros):
#     for i in range(1, pasajeros):
#         if i <10:
#             print(f"Pasajero {i} a bordo.")          
#         else:
#             print(f"Pasajero {i}, Bus lleno.")
#             break


# numero_pasajeros = int(input("Ingrese el total de pasajeros: "))
# simular_viaje(numero_pasajeros)

"""7. Panadería “Don Pancho” – Control de producción diaria
Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.
Si el lote es divisible por 3, mostrar “Verificación de calidad”.
Al final, mostrar “Producción terminada”."""

# def hornear_pan(lotes):
#     for lote in range(1, lotes): 
#         if lote %3 == 0:
#             print(f"Lote número: {lote} ---> Verificación de calidad.")
#         else:
#             print(f"Lote número: {lote} ---> Se esta horneando.")
#     print("Produción terminada.")
            

# cantidad_lotes = int(input("Ingrese la cantidad de lotes: "))
# hornear_pan(cantidad_lotes)

"""8. Cine “MovieLoop” – Calculadora de entradas
Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
Aplicar precio:

    Menores de 12 → $5.000
    De 12 a 59 → $8.000
    Mayores de 60 → $4.000
    Usar un while y condiciones.
"""

# def calcular_entradas():
#     while True:
#         edad = int(input("Ingresar edad: "))
#         if edad == 0:
#             break
#         elif edad >= 60:
#             print("Valor a pagar: $4.000")
            
#         elif edad >12 and edad <=59:
#             print("Valor a pagar: $8.000")
            
#         else:
#             print("Valor a pagar: $5.000")

# calcular_entradas()

"""9. Tienda “EnergyStore” – Simulador de puntos
Como cliente, quiero una función calcular_puntos(compras) que use un for para recorrer la cantidad de compras (ingresada por el usuario).
Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.
Al final, mostrar los puntos totales."""

# def calcular_puntos(compras):  
#     p = 0  
#     for i in range(1, compras+1):
#         if i %3 == 0:
#             pl = 10
#             print(f"{i} Usted ganó {pl} puntos.")
#             p += 10   
#         else:
#             pl = 5
#             print(f"{i} Usted ganó {pl} puntos.") 
#             p += 5
#     return p, "Puntos en total."
            
# cantidad_compra = int(input("Ingrese la cantidad de compra: "))
# print(calcular_puntos(cantidad_compra))

"""10. Academia “CodeStart” – Tabla de multiplicar personalizada
Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
Si el resultado es mayor de 50, mostrar también “Resultado alto”."""

# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         result = i * numero
#         if result > 50:
#             print(f"{numero} X {i}: {result} --> Resultado alto.")
#         else:
#             print(f"{numero} X {i}: {result}")


# Tabla_numero = int(input("Ingrese el número de la tabla que desea conocer: "))
# tabla_multiplicar(Tabla_numero)

"""11. Aerolínea “FlyLoop” – Cálculo de millas acumuladas
Como viajero frecuente, quiero una función calcular_millas(viajes) que reciba el número de viajes realizados y sume millas según la distancia:

Viaje corto (< 1000 km): 500 millas
Medio (1000–3000 km): 1000 millas
Largo (> 3000 km): 2000 millas
Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado."""

"""12. Hospital “Salud Total” – Evaluador de signos vitales
Como médico, quiero una función evaluar_paciente() que reciba frecuencia cardiaca y temperatura corporal.
Si ambos valores están fuera del rango normal (FC > 100 o Temp > 38), mostrar “Paciente en observación”.
Repetir el proceso con varios pacientes en un bucle while."""

"""13. Tienda Online “ShopMaster” – Carrito de compras con validaciones
Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:

Si el precio es negativo, mostrar error y pedir otro valor.
Si el precio es mayor a 100.000, aplicar un 20% de descuento.
Usar while y if dentro de la función hasta ingresar 0 para finalizar."""

"""14. Academia “DevLoop” – Calculadora de factoriales
Como estudiante de programación, quiero una función calcular_factorial(numero) que use un bucle for para calcular el factorial del número.
Si el número ingresado es negativo, mostrar “Número inválido”.
De lo contrario, mostrar el resultado."""

"""15. Empresa “TechManager” – Simulador de rendimiento laboral
Como jefe de equipo, quiero una función evaluar_empleado(nombre, horas) que:

Use un bucle for para simular las horas trabajadas (de 1 hasta horas).
Si la hora es mayor de 8, contar como hora extra.
Al final, calcular el total de horas normales y extras.
Mostrar un resumen del empleado."""