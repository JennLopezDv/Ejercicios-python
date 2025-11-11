"""11. Banco “PythonBank” – Simulación de ahorro mensual
Como cliente, quiero usar un for que sume mi ahorro mensual durante 6 meses.
Si en algún mes el total supera $1,000,000, mostrar “¡Meta alcanzada!”.
Al final, mostrar el total acumulado."""

# ahorro = 0


# for i in range(1, 7):
#     ahorroCliente = int(input(f"Mes {i} Ingrese valor: "))
#     if ahorroCliente > 1000000:
#         print("Meta mensual alcanzada")
#     ahorro += ahorroCliente

# print("Su total ahorrado es de: $",ahorro)

"""///////////////////////"""
# def sumar(a,b):
#     resultado = a+b
#     return resultado

# print(sumar(2,4))

# print(sumar(5,6))
"""///////////////////////"""

"""12. Gimnasio “Level Up” – Control de repeticiones.
Como deportista, quiero ingresar un número de repeticiones y usar un for para imprimir “Repetición X completada”.
Si X es divisible por 3, mostrar además “¡Excelente ritmo!”."""

# numeroRepeticiones = int(input("Ingrese el número de repeticiones a realizar: "))

# for i in range(1, numeroRepeticiones+1):
#     if i %3 == 0:
#         print(f"Repetición {i} completada ¡Excelente ritmo!")
#     else:
#         print(f"Repetición {i} completada.")

"""13. Parqueadero “AutoLoop” – Control de vehículos.
Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
Si entra un número par, mostrar “Vehículo par registrado”.
Si el total llega a 20, mostrar “Capacidad completa”."""

# contarVehiculo = 1

# while contarVehiculo <= 20:       
#     if contarVehiculo %2 == 0:
#         print(f"Vehículo {contarVehiculo}, par registrado.")
#     else: 
#         print(f"Vehículo {contarVehiculo} ingresado.")
#     contarVehiculo +=1

# else: 
#     print("Capacidad completa")

"""14. Tienda “Ahorra Más” – Caja registradora básica.
Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
Si la venta supera $100,000, mostrar “Venta destacada”.
Al final, mostrar el total vendido."""

# montoVenta = int(input("Ingrese monto: "))
# totalVenta = montoVenta

# while montoVenta != 0:
#     montoVenta = int(input("Ingrese otro monto: "))
#     if montoVenta > 100000:
#         print("Venta destacada")
#     totalVenta += montoVenta

# else: 
#     print(f"Total vendido: ${totalVenta}")

"""15. Academia “CodeStart” – Contador de ejercicios completados.
Como estudiante, quiero usar un for del 1 al número que indique.
Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
Si no, solo mostrar “Ejercicio X completado”."""

contadorEjercicios = int(input("Ingrese el número de ejercicios: "))

for i in range(1, contadorEjercicios):
    if contadorEjercicios %5 == 0:
        print(f"Ejercicio {contadorEjercicios}, ¡Gran avance!")
else: 
    print(f"Ejercicio {contadorEjercicios} completado.")

