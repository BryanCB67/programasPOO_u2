class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def show_info(self):
        print(f"Marca: {self.brand}, Modelo: {self.model}, Color: {self.color}")

# Creación de los dos objetos
car1 = Car("Toyota", "Corolla", "Blanco")
car2 = Car("Ford", "Mustang", "Rojo")

# Llamada al método
car1.show_info()
car2.show_info()