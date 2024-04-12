from classes import Huesped, Alpha_hotel
import sys

def main():
    hotel = Alpha_hotel("Alpha_hotel")
    while True:
        print("\nBienvenido al sistema de gestión de reservas Hotel Alpha")
        print("\n1. Agregar visita")
        print("2. Mostrar visitas")
        print("3. Buscar visita")
        print("4. Actualizar visita")
        print("5. Eliminar visita")
        print("6. Salir")

        opcion = input("Por favor, seleccione una opción a realizar: ")

        if opcion == '1':
            nombre = input("Por favor, ingrese el nombre del cliente: ")
            apellido = input("Por favor, ingrese el apellido del cliente: ")
            habitacion = input("Por favor, ingrese el número de habitación: ")
            fecha = input("Por favor, ingrese la fecha de la visita en formato (dd/mm/aaaa): ")
            huesped = Huesped(nombre, apellido, habitacion, fecha)
            hotel.agregar_visita(huesped)

        elif opcion == '2':
            hotel.mostrar_visitas()

        elif opcion == '3':
            nombre_apellido = input("Por favor, ingrese el nombre o apellido del cliente a buscar: ")
            hotel.buscar_visita(nombre_apellido, nombre_apellido)

        elif opcion == '4':
            nombre_apellido = input("Por favor, ingrese el nombre o apellido del cliente cuya visita desea actualizar: ")
            nueva_habitacion = input("Por favor, ingrese la nueva habitación: ")
            nueva_fecha = input("Por favor, ingrese la nueva fecha de la visita en formato (dd/mm/aaaa): ")
            hotel.actualizar_visita(nombre_apellido, nueva_habitacion, nueva_fecha)

        elif opcion == '5':
            nombre_apellido = input("Por favor, ingrese el nombre o apellido del cliente cuya visita desea eliminar: ")
            try:
                nombre, apellido = nombre_apellido.split(maxsplit=1)
            except ValueError:
            # Si solo se proporciona un nombre o un apellido, asignamos el valor a 'nombre' y 'apellido' permanece como una cadena vacía
                nombre = nombre_apellido
                apellido = ""
            print(f"La reserva a eliminar está a nombre de {nombre} {apellido}")
            hotel.eliminar_visita(nombre, apellido)

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, revise y seleccione una opción válida nuevamente.")
import sys


main()
