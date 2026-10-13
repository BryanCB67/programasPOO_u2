class Book:  # Se declara la clase Book.
    def __init__(self, title, num_pages):  # Constructor para recibir título y número de páginas.
        self.title = title  # Asigna el título al objeto
        self.num_pages = num_pages  # Asigna el número de páginas al objeto

    def __str__(self):  # Método mágico __str__ para definir cómo se representa el objeto en forma de texto legible
        return f"Book: {self.title}, Pages: {self.num_pages}"  # Retorna el formato de texto requerido

    def __len__(self):  # Método mágico __len__ para personalizar el comportamiento de la función nativa len()
        return self.num_pages  # Retorna el número de páginas como la longitud del libro


my_book = Book("upen", 350)  # Creación de un objeto Book.
print(my_book)  # Al imprimir el objeto directamente, Python ejecuta automáticamente el método __str__
print(f"Total de páginas usando len(): {len(my_book)}")  # La función len() invoca automáticamente al método __len__ definido en la clase