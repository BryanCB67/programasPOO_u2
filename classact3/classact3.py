class Employee: # Se crea una clase general (padre) Employee para agrupar los atributos comunes como el nombre, evitando repetir código.
    def __init__(self, name): # Constructor de la clase base que recibe el nombre del empleado.
        self.name = name # Guarda el nombre en un atributo general para cualquier tipo de empleado usando self.

class FullTimeEmployee(Employee): # Se crea la clase hija FullTimeEmployee que hereda de Employee usando paréntesis.
    def __init__(self, name, salary): # Constructor que recibe el nombre y el salario.
        super().__init__(name) # super() invoca al constructor de la clase padre (Employee) para reutilizar la asignación del nombre.
        self.salary = salary # Atributo específico para el salario fijo de tiempo completo.

    def payment(self): # Método para calcular el pago de este empleado.
        return self.salary # Retorna el salario fijo mensual.

class HourlyEmployee(Employee): # Se crea la otra clase hija HourlyEmployee que también hereda de Employee.
    def __init__(self, name, hours, payment_per_hour): # Constructor que recibe el nombre, las horas y la tarifa por hora.
        super().__init__(name) # Reutiliza el atributo name heredado de la clase Employee mediante super().
        self.hours = hours # Guarda el número de horas trabajadas en un atributo individual.
        self.payment_per_hour = payment_per_hour # Guarda cuánto se paga por cada hora en un atributo individual.

    def payment(self): # Método para calcular el pago de este empleado por horas.
        return self.hours * self.payment_per_hour # Multiplica las horas por la tarifa y retorna el resultado de su pago.

def calculate_payment(worker): # Función externa que aplica polimorfismo recibiendo cualquier objeto worker y llamando a su método payment().
    return worker.payment() # Ejecuta el método payment respectivo del objeto que se le pase (sea FullTime o Hourly).

# Creación de los objetos utilizando las clases corregidas y estructuradas con herencia
employee1 = FullTimeEmployee("Bryan", 8000) # Se crea un objeto FullTimeEmployee pasando nombre y salario.
employee2 = HourlyEmployee("Pinto", 40, 100) # Se crea un objeto HourlyEmployee pasando nombre, horas y tarifa.

# Impresión de los resultados en consola usando el punto y los paréntesis
print("Pago de", employee1.name, ":", calculate_payment(employee1)) # Llama a la función y muestra el pago del empleado a tiempo completo.
print("Pago de", employee2.name, ":", calculate_payment(employee2)) # Llama a la función y muestra el pago del empleado por horas.