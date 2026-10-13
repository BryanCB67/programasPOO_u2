class Engine:  # Se declara la clase Engine (Motor).
    def start(self):  # Método start para encender el motor.
        print("Engine started")  # Imprime el mensaje de inicio del motor

class Car:  # Se declara la clase Car (Composición: un carro tiene un motor).
    def __init__(self, engine):  # Constructor que recibe un objeto de tipo Engine como atributo
        self.engine = engine  # Guarda el objeto engine dentro de un atributo de la clase Car

    def start_car(self):  # Método para iniciar el carro
        self.engine.start()  # Llama al método start() utilizando el objeto motor guardado en la composición


my_engine = Engine()  # Creación de una instancia de Engine.
my_car = Car(my_engine)  # Creación de una instancia de Car pasándole el motor creado (composición).
my_car.start_car()  # Invocación del método start_car que a su vez enciende el motor