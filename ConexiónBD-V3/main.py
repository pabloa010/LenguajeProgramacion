import os
import sys
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
    nueva_ciudad = c.City(id_ciudad, nuevo_nombre, 1)
    print(nueva_ciudad)
    daoCity = dao.DaoCity(conex)
    daoCity.update(nueva_ciudad)

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

def insertar_job():
    nombre = input("Nombre del trabajo: ")
    job = c.Job(nombre, 1)
    daoJob = dao.DaoJob(conex)
    daoJob.insert(job)

def mostrar_jobs():
    daoJob = dao.DaoJob(conex)
    jobs = daoJob.get_all()
    for job in jobs:
        print(job)

def editar_job():
    id_job = int(input("Por favor, ingrese el ID del trabajo que desea editar: "))
    nuevo_nombre = input("Por favor, ingrese el nuevo nombre que se asignará al trabajo: ")
    nuevo_job = c.Job(nuevo_nombre, 1)
    nuevo_job.id = id_job
    daoJob = dao.DaoJob(conex)
    daoJob.update(nuevo_job)

def eliminar_job():
    id_job = int(input("Por favor, ingrese el ID del trabajo que desea eliminar: "))
    daoJob = dao.DaoJob(conex)
    daoJob.delete(id_job)

def buscar_job():
    nombre_job = input("Por favor, ingrese el nombre del trabajo que desea buscar: ")
    daoJob = dao.DaoJob(conex)
    jobs = daoJob.search(nombre_job)
    for job in jobs:
        print(job)

def insertar_empleado():
    nombre = input("Ingresa nombre del empleado: ")
    ciudad_nombre = input("Nombre de la ciudad del empleado: ")
    job_nombre = input("Puesto de trabajo del empleado: ")
    salario = float(input("Salario del empleado: "))
    status = input("Ingresa el estatus del empleado, ya sea activo o inactivo: ")
    ciudad = c.City(ciudad_nombre, 1)
    job = c.Job(job_nombre, 1)
    empleado = c.Employee(nombre, ciudad, job, salario, status, 1)
    daoEmployee = dao.DaoEmployee(conex)
    daoEmployee.insert(empleado)

def mostrar_empleados():
    daoEmployee = dao.DaoEmployee(conex)
    empleados = daoEmployee.get_all()
    for empleado in empleados:
        print(empleado)

def editar_empleado():
    id_empleado = int(input("Por favor, ingrese el ID del empleado que desea editar: "))
    nombre = input("Nuevo nombre del empleado: ")
    ciudad_nombre = input("Nuevo nombre de la ciudad del empleado: ")
    job_nombre = input("Nuevo nombre del puesto de trabajo del empleado: ")
    salario = float(input("Nuevo salario del empleado: "))
    ciudad = c.City(ciudad_nombre, 1)
    job = c.Job(job_nombre, 1)
    empleado = c.Employee(nombre, ciudad, job, salario, 1)
    empleado.id = id_empleado
    daoEmployee = dao.DaoEmployee(conex)
    daoEmployee.update(empleado)

def eliminar_empleado():
    id_empleado = int(input("Por favor, ingrese el ID del empleado que desea eliminar: "))
    daoEmployee = dao.DaoEmployee(conex)
    daoEmployee.delete(id_empleado)

def buscar_empleado():
    nombre_empleado = input("Por favor, ingrese el nombre del empleado que desea buscar: ")
    daoEmployee = dao.DaoEmployee(conex)
    empleados = daoEmployee.search(nombre_empleado)
    for empleado in empleados:
        print(empleado)

def salir():
    print("Hasta pronto. ")
    sys.exit()

def menu():
    print("1. Insertar Ciudad")
    print("2. Mostrar Ciudades")
    print("3. Editar Ciudad")
    print("4. Eliminar Ciudad")
    print("5. Buscar Ciudad")
    print("6. Insertar Trabajo")
    print("7. Mostrar Trabajos")
    print("8. Editar Trabajo")
    print("9. Eliminar Trabajo")
    print("10. Buscar Trabajo")
    print("11. Insertar Empleado")
    print("12. Mostrar Empleados")
    print("13. Editar Empleado")
    print("14. Eliminar Empleado")
    print("15. Buscar Empleado")
    print("16. Salir del menú")

def main():
    op = 0
    while(op != 16):
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
        elif op == 6:
            insertar_job()
            os.system("pause")
        elif op == 7:
            mostrar_jobs()
            os.system("pause")
        elif op == 8:
            editar_job()
            os.system("pause")
        elif op == 9:
            eliminar_job()
            os.system("pause")
        elif op == 10:
            buscar_job()
            os.system("pause")
        elif op == 11:
            insertar_empleado()
            os.system("pause")
        elif op == 12:
            mostrar_empleados()
            os.system("pause")
        elif op == 13:
            editar_empleado()
            os.system("pause")
        elif op == 14:
            eliminar_empleado()
            os.system("pause")
        elif op == 15:
            buscar_empleado()
            os.system("pause")
        elif op == 16:
            salir()
        else:
            print("Por favor, verifica el número ingresado e intenta nuevamente ")
import sys

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