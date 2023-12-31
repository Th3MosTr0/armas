class guns:
    
    def __init__(self,nombre,rareza,capacidad_balas,alcanze,daño):
        self.nombre = nombre
        self.rareza = rareza
        self.capacidad_balas = capacidad_balas
        self.alcanze = alcanze
        self.daño = daño

class francotirador (guns):

    def __init__(self, nombre, rareza, capacidad_balas, alcanze,daño):
        super().__init__(nombre, rareza, capacidad_balas, alcanze,daño)

    def mostrar_informacion(self):
        print("Nombre: Tokarev SVT-40")
        print("Rareza: legendaria")
        print("capacidad de balas: 6")
        print("alcanze: 800metros")
        print ("daño: 120")

class fusil_de_asalto (guns):

    def __init__(self, nombre, rareza, capacidad_balas, alcanze, daño):
        super().__init__(nombre, rareza, capacidad_balas, alcanze, daño)

    def mostrar_informacion(self):
        print("Nombre: AK-47")
        print("Rareza: épica")
        print("capacidad de balas: 30")
        print("alcanze: 400metros")
        print ("daño: 40")

class lanzacohetes (guns):

    def __init__(self, nombre, rareza, capacidad_balas, alcanze, daño):
        super().__init__(nombre, rareza, capacidad_balas, alcanze, daño )

    def mostrar_informacion(self):
        print("Nombre: RPG-7")
        print("Rareza: muy rara")
        print("capacidad de balas: 1")
        print("alcanze: 500metros")
        print ("daño: 150")

class escopeta(guns):

    def __init__(self, nombre, rareza, capacidad_balas, alcanze, daño ):
        super().__init__(nombre, rareza, capacidad_balas, alcanze, daño )

    def mostrar_informacion(self):
        print("Nombre: Winchester 21")
        print("Rareza: rara")
        print("capacidad de balas: 10")
        print("alcanze: 50metros")
        print ("daño: 100")


class pistola (guns):

    def __init__(self, nombre, rareza, capacidad_balas, alcanze, daño):
        super().__init__(nombre, rareza, capacidad_balas, alcanze, daño)

    def mostrar_informacion(self):
        print("Nombre: mp30")
        print("Rareza: común")
        print("capacidad de balas: 8")
        print("alcanze: 100metros")
        print ("daño: 20")
