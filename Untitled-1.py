class Casa:
    def __init__(self, ventanas, puertas, techo, metros_cuadrados, color):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.metros_cuadrados = metros_cuadrados
        self.color = color 

    def describir(self):
        return (f"Casa con {self.ventanas} ventanas, {self.puertas} puertas, "
                f"techo de tipo '{self.techo}', {self.metros_cuadrados} m², y de color {self.color}.")


class ViviendaFamiliar(Casa):
    def __init__(self, ventanas, puertas, techo, metros_cuadrados, color, num_habitaciones):
        super().__init__(ventanas, puertas, techo, metros_cuadrados, color)
        self.num_habitaciones = num_habitaciones

    def describir(self):
        base = super().describir()
        return base + f" Tiene {self.num_habitaciones} habitaciones."


class Apartamento(Casa):
    def __init__(self, ventanas, puertas, techo, metros_cuadrados, color, piso):
        super().__init__(ventanas, puertas, techo, metros_cuadrados, color)
        self.piso = piso

    def describir(self):
        base = super().describir()
        return base + f" Está ubicado en el piso {self.piso}."


class Bungalo(Casa):
    def __init__(self, ventanas, puertas, techo, metros_cuadrados, color, jardin):
        super().__init__(ventanas, puertas, techo, metros_cuadrados, color)
        self.jardin = jardin  # True o False

    def describir(self):
        base = super().describir()
        jardin_info = "con jardín." if self.jardin else "sin jardín."
        return base + f" Es un búngalo {jardin_info}"


class Penthouse(Casa):
    def __init__(self, ventanas, puertas, techo, metros_cuadrados, color, num_baños):
        super().__init__(ventanas, puertas, techo, metros_cuadrados, color)
        self.num_baños = num_baños

    def describir(self):
        base = super().describir()
        return base + f" Este penthouse tiene {self.num_baños} baños"

casa_familiar = ViviendaFamiliar(6, 2, "teja", 120, "verde", 4)
apartamento = Apartamento(4, 1, "plano", 80, "azul claro", 5)
bungalo = Bungalo(5, 2, "dos aguas", 100, "blanco", True)
penthouse = Penthouse(10, 4, "madera", 500, "grisáceo", 4)


print(casa_familiar.describir())
print(apartamento.describir())
print(bungalo.describir())
print(penthouse.describir())

