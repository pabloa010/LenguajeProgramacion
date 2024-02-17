class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        
# crear objeto persona
persona1 = Persona("Durán", 79)
persona1.saludar()

esposa = Persona("Gabriela",29)
esposa.saludar()



class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando el grado {self.grado}.")


estudiante1 = Estudiante("Gabriela", 29, "Maestría")
estudiante1.saludar()
estudiante1.estudiar()


