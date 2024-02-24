class Contacto:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y mi número de contacto es {self.phone_number}")

contacto1 = Contacto("Mathius Zamora", 88882222)
contacto2 = Contacto("Pablo Aburto", 78781111)
contacto1.greet()