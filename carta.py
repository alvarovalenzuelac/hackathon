class Carta():
    def __init__(self,nombre,costo,imagen,jugador="sin_jugador") -> None:
        self.nombre = nombre
        self.costo = costo
        self.imagen = imagen
        self.jugador = jugador

class Unidad(Carta):
    def __init__(self, nombre, costo,imagen,jugador,resistencia,poder) -> None:
        super().__init__(nombre, costo,imagen,jugador)
        self.resistencia = resistencia
        self.poder = poder

    def atacar(self,objetivo):
        if not isinstance(objetivo,Unidad):
            print("el objetivo, no es una unidad")
            return self
        print(f"{self.nombre} ataca a {objetivo.nombre}")
        objetivo.resistencia -= self.poder
        if objetivo.resistencia < 0:
            objetivo.resistencia = 0
        return self
    
    def print_atributos(self):
        print(f"Nombre: {self.nombre}, Costo: {self.costo}, Poder: {self.poder}, Resistencia: {self.resistencia}")
        return self


class Efecto(Carta):
    def __init__(self, nombre, costo,imagen,jugador,texto,atributo,magnitud) -> None:
        super().__init__(nombre, costo,imagen,jugador)
        self.texto = texto
        self.atributo = atributo
        self.magnitud = magnitud
    
    def jugar(self,objetivo):
        if not isinstance(objetivo,Unidad):
            print("el objetivo no es una unidad")
            return self
        if self.atributo == "resistencia":
            objetivo.resistencia += self.magnitud
            print(f"{self.nombre} surge efecto en {objetivo.nombre}")
            if objetivo.resistencia < 0:
                objetivo.resistencia = 0
            
        if self.atributo == "poder":
            objetivo.poder += self.magnitud


#ninja_cinturon_rojo = Unidad("Ninja Cinturón Rojo",3,4,3)
#ninja_cinturon_negro = Unidad("Ninja Cinturón Negro",4,4,5)

#algoritmo_duro = Efecto("Algoritmo Duro",2,"aumentar la resistencia del objetivo en 3","resistencia",3)
#promesa_no_manejada = Efecto("Promesa no Manejada",1,"reducir la resistencia del objetivo en 2","resistencia",-2)
#programacion_en_pareja = Efecto("Programación en pareja",3,"aumentar el poder del objetivo en 2","poder",2)

#ninja_cinturon_negro.atacar(ninja_cinturon_negro)

"""promesa_no_manejada.jugar(ninja_cinturon_rojo)
#ninja_cinturon_rojo.print_atributos()
ninja_cinturon_rojo.print_atributos()
ninja_cinturon_negro.print_atributos()
ninja_cinturon_negro.atacar(ninja_cinturon_rojo)
ninja_cinturon_rojo.print_atributos()
ninja_cinturon_negro.print_atributos()"""