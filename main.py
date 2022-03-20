from statistics import mode


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]

        if color in colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        permitidos = ["electrico", "gasolina"]
        
        if tipo in permitidos:
            self.tipo = tipo

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        total = 0

        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                total += 1
        
        return total

    def verificarIntegridad(self):
        pirateria = "Las piezas no son originales"
        original = "Auto original"
        
        if self.motor.registro != self.registro:
            return pirateria
        
        for asiento in self.asientos:
            if asiento.registro != self.registro:
                return pirateria

        return original