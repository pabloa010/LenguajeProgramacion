edad = float(input("ingrese la edad de la persona:"))

def seleccion(edad):
    if edad >= 18:
        print("es mayor de edad")
    else:
        print("la persona no es mayor de edad")

seleccion(edad)
