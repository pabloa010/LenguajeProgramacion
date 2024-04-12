import sqlite3

class Huesped:
    def __init__(self, nombre, apellido, habitacion, fecha):
        self.nombre = nombre
        self.apellido = apellido
        self.habitacion = habitacion
        self.fecha = fecha

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Habitación: {self.habitacion}, Fecha: {self.fecha}"


class Alpha_hotel:
    def __init__(self, Alph_hotel):
        self.Alph_hotel = Alph_hotel
        self.connection = sqlite3.connect(self.Alph_hotel)
        self.cursor = self.connection.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS visitas
                            (nombre TEXT, apellido TEXT, habitacion TEXT, fecha TEXT)''')
        self.connection.commit()

    def agregar_visita(self, huesped):
        self.cursor.execute("INSERT INTO visitas VALUES (?, ?, ?, ?)", (huesped.nombre, huesped.apellido, huesped.habitacion, huesped.fecha))
        self.connection.commit()
        print("Visita añadida correctamente.")

    def mostrar_visitas(self):
        self.cursor.execute("SELECT * FROM visitas")
        visitas = self.cursor.fetchall()
        if visitas:
            print("Lista de visitas:")
            for visita in visitas:
                print(f"Nombre: {visita[0]}, Apellido: {visita[1]}, Habitación: {visita[2]}, Fecha: {visita[3]}")
        else:
            print("No hay visitas registradas.")

    def buscar_visita(self, nombre, apellido):
        self.cursor.execute("SELECT * FROM visitas WHERE nombre=? OR apellido=?", (nombre, apellido))
        visita = self.cursor.fetchone()
        if visita:
            print(f"Nombre: {visita[0]}, Apellido: {visita[1]}, Habitación: {visita[2]}, Fecha: {visita[3]}")
        else:
            print("Visita no encontrada.")

    def actualizar_visita(self, nombre_apellido, nueva_habitacion, nueva_fecha):
        self.cursor.execute("UPDATE visitas SET habitacion=?, fecha=? WHERE nombre=? OR apellido=?", (nueva_habitacion, nueva_fecha, nombre_apellido, nombre_apellido))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Visita actualizada correctamente.")
        else:
            print("Visita no encontrada.")

    def eliminar_visita(self, nombre, apellido):
        self.cursor.execute("DELETE FROM visitas WHERE nombre=? AND apellido=?", (nombre, apellido))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Visita eliminada correctamente de los registros.")
        else:
            print("Visita no encontrada en los registros.")

    def __del__(self):
        self.connection.close()