class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {} , {} ruedas".format(self.color, self.ruedas)
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        Vehiculo.__init__(self, color, ruedas)  #self.color = color
                                                #self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} Km/h, {} cc".format( self.velocidad, self.cilindraje)

c=Coche("azul", 4 ,150, 1200)
print(c)

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color {} , {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    def __str__(self):
        return super().__str__() + ", {} Km/h, {} cc".format( self.velocidad, self.cilindraje)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        super().__init__(color, ruedas, velocidad, cilindraje)
        self.carga = carga
    def __str__(self):
        return super().__str__() + ", {} Kg de carga".format( self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", {}".format( self.tipo)

class Motocicleta (Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    def __str__(self):
        return super().__str__() + ", {} Km/h, {} cc".format( self.velocidad, self.cilindraje)
vehiculo=[
    Coche("Azul" , 4, 150, 1200),
    Camioneta ("Blanco", 4, 100, 1300 , 1500),
    Bicicleta ("Verde", 2, "Urbano"),
    Motocicleta ("Negro", 2, "Deportiva", 180, 900)
]

#def Catalogar(lista):
#    for v in lista:
#        print("{} {}".format(type(v).__name__, v ))
#Catalogar(vehiculo)

def Catalogar(lista, ruedas = None):
    if ruedas != None:
        contador = 0
        for v in vehiculo:
            if v.ruedas == ruedas:
                contador += 1
        print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))
    for v in lista:
        if ruedas == None:
            print("{} {}".format(type(v).__name__, v ))
        else:
            if v.ruedas == ruedas:
                print("{} {}".format(type(v).__name__, v ))

Catalogar(vehiculo, 1)
