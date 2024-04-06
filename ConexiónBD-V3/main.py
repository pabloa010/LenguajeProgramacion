import os
import daoConnection as dao
import clases as c

os.system('cls')
conex = dao.Connection("localhost", "root", "", "bdregisters")
conex.connect()

def insertar():
    nombre = input("Nombre de la ciudad: ")
    ciudad = c.City(nombre, 1)
    daoCity = dao.DaoCity(conex)
    daoCity.insert(ciudad)

def mostrar():
    daoCity = dao.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)

def editar():
    id_ciudad = int(input("Por favor, ingrese el ID de la ciudad que desea editar: "))
    nuevo_nombre = input("Por favor, ingrese el nuevo nombre que se asignará a la ciudad: ")
    ciudad = c.City(nuevo_nombre, 1, id_ciudad)
    daoCity = dao.DaoCity(conex)
    daoCity.update(ciudad)

def eliminar():
    id_ciudad = int(input("Por favor, ingrese el ID de la ciudad que desea eliminar: "))
    daoCity = dao.DaoCity(conex)
    daoCity.delete(id_ciudad)

def buscar():
    nombre_ciudad = input("Por favor, ingrese el nombre de la ciudad que desea buscar: ")
    daoCity = dao.DaoCity(conex)
    cities = daoCity.search(nombre_ciudad)
    for city in cities:
        print(city)

def menu():
    print("1. Insertar Ciudad")
    print("2. Mostrar Ciudades")
    print("3. Editar Ciudad")
    print("4. Eliminar Ciudad")
    print("5. Buscar Ciudad")
    print("6. Salir del menú")

def main():
    op = 0
    while(op != 6):
        menu()
        op = int(input("Opcion: "))
        if op == 1:
            insertar()
            os.system("pause")
        elif op == 2:
            mostrar()
            os.system("pause")
        elif op == 3:
            editar()
            os.system("pause")
        elif op == 4:
            eliminar()
            os.system("pause")
        elif op == 5:
            buscar()
            os.system("pause")

main()

"""    


#instanciar modelo
city1 = c.City("Managua", 1)
city2 = c.City("León", 1)
city3 = c.City("Granada", 1)
city4 = c.City("Masaya", 1)
city5 = c.City("Estelí", 1)
city6 = c.City("Jinotepe", 1)

#instanciar dao
daoCity = dao.DaoCity(conex)
#insertar
daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)

#consultar
cities = daoCity.get_all()
for city in cities:
    print(city)
"""