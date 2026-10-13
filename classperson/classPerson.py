class Person: # Se declara la clase Person con la primera letra en mayúscula y dos puntos obligatorios para estructurar el modelo de personas.
    def __init__(self, name, age, city): # Constructor de la clase que recibe los parámetros name, age y city; utiliza self para hacer referencia al objeto individual que se está creando.
        self.name = name # Guarda el parámetro name de forma permanente en el atributo del objeto actual usando self y el operador  [=].
        self.age = age # Guarda el parámetro age de forma permanente en el atributo del objeto actual usando self y el operador de  [=].
        self.city = city # Guarda el parámetro city de forma permanente en el atributo del objeto actual usando self y el operador de [=].

    def greet(self): # Método de la clase llamado greet; el parámetro self es indispensable para acceder a los datos específicos de la persona que lo invoque.
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.") # Utiliza una f-string con llaves {} para insertar dinámicamente los valores guardados en el objeto[cite: 8].e: 8].

# Creación de tres objetos de la clase Person con valores diferentes
p1 = Person("Ana", 25, "Mexico") # Se instancia el primer objeto con datos específicose
p2 = Person("Carlos", 30, "Colombia") # Se instancia el segundo objeto con datos específicos
p3 = Person("Sofia", 22, "Argentina") # Se instancia el tercer objeto con datos específicos

# Invocación del método greet() para cada objeto creado utilizando el punto y los paréntesis
p1.greet() # Llama al método greet para p1
p2.greet() # Llama al método greet para p2
p3.greet() # Llama al método greet para p3