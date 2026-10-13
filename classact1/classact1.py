class Employee:  # Se declara la clase base Employee con la primera letra en mayúscula y dos puntos obligatorios.
    def __init__(self, name, salary):  # Constructor que recibe los parámetros name y salary; utiliza self para referenciar al objeto actual.
        self.name = name  # Guarda el parámetro name de forma permanente en el atributo del objeto actual.
        self.salary = salary  # Guarda el parámetro salary de forma permanente en el atributo del objeto actual.

    def show_info(self):  # Método de instancia que requiere self para mostrar los datos del empleado.
        print(f"Name: {self.name}, Salary: {self.salary}")  # Imprime la información usando una f-string.

class Manager(Employee):  # Se declara la clase derivada Manager que hereda de Employee pasando la clase padre entre paréntesis.
    def __init__(self, name, salary, department):  # Constructor del Manager que recibe los atributos propios y los heredados.
        super().__init__(name, salary)  # super() se usa para invocar el constructor de la clase padre (Employee) y reutilizar la inicialización de name y salary.
        self.department = department  # Agrega y guarda el atributo exclusivo de la clase Manager.

    def show_info(self):  # Sobrescritura (override le permite a la clase hija modificar, adaptar o ampliar el comportamiento de un método heredado para que funcione de manera distinta o más específica) del método show_info para modificar su comportamiento en la clase hija.
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")  # Imprime la información extendida incluyendo el departamento.


emp = Employee("Carlos", 3000)  # Creación de un objeto de la clase base Employee.
mgr = Manager("Ana", 5000, "IT")  # Creación de un objeto de la clase derivada Manager.
emp.show_info()  # Llama al método show_info del empleado.
mgr.show_info()  # Llama al método show_info sobrescrito del gerente.