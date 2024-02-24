#Calculador de operaciones basicas por Mathius Zamora y Pablo Aburto
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

# Opciones a elegir
print("Muchas gracias por usar nuestro calculador, \n Por favor, escoje la operación a realizar:")
print("1- Sumar")
print("2- Restar")
print("3- Multiplicar")
print("4. Dividir")

opcion = input("Para iniciar, por favor ingresa el número de la operación a realizar: ")

number1 = float(input("Por favor, ingrese el primer número: "))
number2 = float(input("Por favor, ingrese el segundo número: "))

#Detalle de operaciones
if opcion == '1':
    print("La suma de", number1, "+", number2, "es =", add(number1, number2))

elif opcion == '2':
    print("La resta de", number1, "-", number2, "es =", subtract(number1, number2))

elif opcion == '3':
    print("La multiplicación de", number1, "*", number2, "es =", multiply(number1, number2))

elif opcion == '4':
    print("La división de", number1, "/", number2, "es =", divide(number1, number2))

else:
    print("Por favor verificar el número ingresado; operación no válida")