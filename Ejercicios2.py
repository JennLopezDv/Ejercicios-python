#1. Pide al usuario un número y muestra si es positivo, negativo o cero.
# numero = int(input("Ingresa un número: "))

# if numero < 0:
#     print(numero, "Es negativo.")

# elif numero == 0:
#     print(numero, "Es Cero.")

# else:
#     print(numero, "Es positivo.")

#2. Mostrar si es número par o impár.
# ingreseNumero = int(input("Ingrese número: "))

# if ingreseNumero %2 == 0:
#     if ingreseNumero ==0:
#         print(ingreseNumero, "Es cero.")
#     elif ingreseNumero < 0:
#         print(ingreseNumero, "Es par negativo.")
#     else:
#         print(ingreseNumero, "Es par positivo.")

# else:
#     if ingreseNumero <0:
#         print(ingreseNumero, "Es negativo impar.")
#     else:
#         print(ingreseNumero, "Es positivo impar.")


#3. Cuál es el mayor de tres números.
# a = int(input("Ingrese el primer número: "))
# b = int(input("Ingrese el segundo número: "))
# c = int(input("Ingrese el tercer número: "))

# if a >= b and a >= c:
#     print(a, "Es mayor.")

# elif b >= a and b >= c:
#     print(b, "Es mayor.")

# else:
#     print(c, "Es mayor.")


#4. Contador del 1 al 10.
#numero = int(input("Hasta que número deseas contar: "))

#Forma de solución.
# i = 1
# while i <= numero:
#    print(i)
#    i += 1

#Forma 2 de solución.
#for i in range(1, numero +1):
#   print(i)


#5. Sumar hasta que el usuario ingrese 0.
# numero = int(input("Ingrese número: "))
# suma = 0

# while numero != 0:
#     suma += numero
#     numero = int(input("Ingrese otro número: "))

# print("El total es: ", suma)

#6. Adivina el número
# secreto = 100
# numero = int(input("¿Cuál número es?: "))

# while numero != secreto:
#     if numero < secreto:
#         print("Demasiado bajo.")

#     elif numero > secreto:
#         print("Demasiado alto.")
#     numero = int(input("Intenta de nuevo: "))

# print("¡¡A D I V I N A S T E!!")



    