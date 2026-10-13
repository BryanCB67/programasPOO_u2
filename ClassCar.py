class Car: # se realiza la clase car para tener el model y agregar sus atributos muy importante si no se coloca los dos puntos no se puede crear la clase importante tambien agregar la primera letra mayuscula en el nombre de la clase
    def __init__(self, brand, model, color): # esta linea es el constructor de la clase, se utiliza para realizar los atributos de la clase, se utiliza el self para hacer referencia a los atributos de la clase y se colocan los atributos que se van a utilizar en la clase
        self.brand = brand #en esta linea se hace la referencia a el objeto inidividual con el self, brand Es la "etiqueta" o cajita oficial donde se va a almacenar el dato de manera permanente dentro del carro para que no se olvide.
        self.model = model #en esta linea se hace la referencia a el objeto inidividual con el self, model Es la "etiqueta" o cajita oficial donde se va a almacenar el dato de manera permanente dentro del carro para que no se olvide.
        self.color = color #en esta linea se hace la referencia a el objeto inidividual con el self, color Es la "etiqueta" o cajita oficial donde se va a almacenar el dato de manera permanente dentro del carro para que no se olvide.
        #el operador "=" Su trabajo es tomar el valor que está a su derecha y guardarlo dentro de la cajita o atributo que está a su izquierda
    def show_info(self): # aqui en esta linea def Es la palabra clave que le indica a Python que se esta comenzando a crear una función o método, el showinfo es el metodo de mostrar informacion el self Le avisa al método Trabaja con los datos del carro específico que te está invocando en este momento
        print(f"Marca: {self.brand}, Modelo: {self.model}, Color: {self.color}") #aqui la f de f-string permite insertar variables directamente dentro de un texto usando llaves {} de forma rápida y limpia en las llaves va a imprimir lo que se guardo en el atributo por ejemplo como toyota, carolla
# muy importante revisar bien la sintaxis de la clase y los metodos como los : al momento de crear la clase

car1 = Car("Toyota", "Corolla", "Blanco") #creacion de objetos en este caso car1 
car2 = Car("Ford", "Mustang", "Rojo") #en este caso car2 


car1.show_info() #en estas dos lineas se esta llamando al metodo show info para mostrar la informacion de los objetos creados en car1 y car2
car2.show_info() #se utiliza el punto para acceder a los metodos y atributos de la clase y los parentesis para invocar al metodo show info