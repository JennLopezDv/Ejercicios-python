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

def aplicar_descuentos():
    valor_compra = 1
    grantotal = 0
    while valor_compra != 0:
        valor_compra = int(input("Ingrese precio: "))
        sindesc = 0
        
             
        if valor_compra > 50000:
            condesc = 0
            total = valor_compra - (valor_compra * 0.10)
            print("Valor a pagar por esta venta: ",total)
            condesc += total
            grantotal += condesc
        else:
             sindesc += sindesc
             grantotal += sindesc
          
    else:
            print("Total a pagar con descuento: ",condesc)
            print("Total a pagar sin descuento: ",sindesc)
            print("Total a pagar en general: ", grantotal)



aplicar_descuentos()
