class Accountant:  # Se declara la primera clase base Accountant.
    def generate_report(self):  # Método de instancia de Accountant.
        print("Generating financial report")  # Imprime el mensaje correspondiente al reporte financiero.

class Technician:  # Se declara la segunda clase base Technician.
    def repair_machine(self):  # Método de instancia de Technician.
        print("Repairing machine")  # Imprime el mensaje correspondiente a la reparación de máquinas.

class Boss(Accountant, Technician):  # Se declara la clase Boss que hereda simultáneamente de ambas clases base (Herencia Múltiple).
    pass  # Palabra clave pass que indica que la clase hereda todo lo anterior sin agregar código nuevo.


boss_obj = Boss()  # Creación de un objeto de la clase Boss.
boss_obj.generate_report()  # Invocación del método heredado de Accountant.
boss_obj.repair_machine()  # Invocación del método heredado de Technician.