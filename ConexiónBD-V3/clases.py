class City:
    def __init__(self, name, id, status=1):
        self.name = name
        self.status = status
        self.id = id

    def __str__(self):
        return f"{self.name}, {self.status}, {self.id}"
    
class Job:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
    
class Employee:
    def __init__(self, id, nombre, ciudad, job, salary, status):
        self.nombre = nombre
        self.ciudad = ciudad
        self.job = job
        self.salary = salary
        self.status = status
        self.id = id
    
    def __str__(self):
        return self.nombre
    
    def get_full_name(self):
        return self.nombre
    
    def get_city(self):
        return self.ciudad.name
    
    def get_job(self):
        return self.job.name
    
    def get_salary(self):
        return self.salary
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    
