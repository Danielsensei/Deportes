class Jugador():
    def __init__(self,nombre,edad,DNI,altura,equipo,deporte):
        self.__nombre=nombre
        self.__edad=edad
        self.__DNI=DNI
        self.__altura=altura
        self.__equipo=equipo
        self.__deporte=deporte
    def set_nombre (self,nombre):
        self.__nombre=nombre
    def get_nombre (self):
        return self.__nombre
    def set_edad (self,edad):
        self.__edad=edad
    def get_edad (self):
        return self.__edad
    def set_DNI (self,DNI):
        self.__DNI=DNI
    def get_DNI (self):
        return self.__DNI
    def set_altura (self,altura):
        self.__altura=altura
    def get_altura (self):
        return self.__altura
    def set_equipo (self,equipo):
        self.__equipo=equipo
    def get_equipo (self):
        return self.__equipo
    def set_equipo (self,deporte):
        self.__deporte=deporte
    def get_equipo (self):
        return self.__deporte
    
class Futbol(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,deporte,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
        super().__init__(nombre,edad,DNI,altura,equipo,deporte)
    def set_futbol(self,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
    def get_futbol(self):
        return self.__posicionfutbol
class Baloncesto(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,deporte,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
        super().__init__(nombre,edad,DNI,altura,equipo,deporte)
    def set_baloncesto(self,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
    def get_baloncesto(self):
        return self.__posicionbaloncesto
class Voleibol(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,deporte,clase):
        self.__clase=clase
        super().__init__(nombre,edad,DNI,altura,equipo,deporte)
    def set_voleibol(self,clase):
        self.__clase=clase
    def get_voleibol(self):
        return self.__clase
class Taekwondo(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,deporte,cinturon):
        self.__cinturon=cinturon
        super().__init__(nombre,edad,DNI,altura,equipo,deporte)
    def set_taekwondo(self,cinturon):
        self.__cinturon=cinturon
    def get_taekwondo(self):
        return self.__cinturon
'''def main():
    personas={}
    z="si"
    while z.lower()=="si":
        nombre=input("Introduce el nombre del jugador:")
        edad=input("Introduce la edad del jugador:")
        DNI=input("Introduce el DNI del jugador:")
        altura=input("Introduce la altura del jugador:")
        equipo=input("Introduce el equipo al que pertenece:")
        a=input("¿A que tipo de deporte pertenece:futbol, baloncesto, voleibol o taekwondo?")
        if a.lower()=="futbol":
            posicionfutbol=input("Introduce la posicion que ocupa el jugador dentro del campo:")
            jugador=Futbol(nombre,edad,DNI,altura,equipo,posicionfutbol)
            jugador.set_futbol(posicionfutbol)
        elif a.lower()=="baloncesto":
            posicionbaloncesto=input("Introduce la posicion que ocupa el jugador dentro de la cancha:")
            jugador=Baloncesto(nombre,edad,DNI,altura,equipo,posicionbaloncesto)
            jugador.set_baloncesto(posicionbaloncesto)
        elif a.lower()=="voleibol":
            clase=input("Introduce la clase del jugador:")
            jugador=Voleibol(nombre,edad,DNI,altura,equipo,clase)
            jugador.set_voleibol(clase)
        elif a.lower()=="taekwondo":
            cinturon=input("Introduce el cinturon del jugador:")
            jugador=Taekwondo(nombre,edad,DNI,altura,equipo,cinturon)
            jugador.set_taekwondo(cinturon)
        else:
            break
        z=input("¿Quires introducir a otro jugador?")'''
    
def mostrar():
    for jugador in personas:
        print(jugador.get_nombre())
        print(jugador.get_edad())
        print(jugador.get_DNI())
        print(jugador.get_altura())
        print(jugador.get_equipo())
        print(jugador.get_deporte())
        if jugador.get_a()=="futbol":
            print(jugador.get_posicionfutbol())
        elif jugador.get_a()=="baloncesto":
            print(jugador.get_posicionbaloncesto())
        elif jugador.get_a()=="voleibol":
            print(jugador.get_clase())
        elif jugador.get_a()=="taekwondo":
            print(jugador.get_cinturon())
def esMayorDeEdad():
    if edad>=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
        

if __name__=="__main__":
    z="si"
    while z.lower()=="si":
        nombre=input("Introduce el nombre del jugador:")
        edad=int(input("Introduce la edad del jugador:"))
        DNI=input("Introduce el DNI del jugador:")
        altura=input("Introduce la altura del jugador:")
        equipo=input("Introduce el equipo al que pertenece:")
        deporte=input("¿A que tipo de deporte pertenece:futbol, baloncesto, voleibol o taekwondo?")
        if deporte.lower()=="futbol":
            posicionfutbol=input("Introduce la posicion que ocupa el jugador dentro del campo:")
            jugadores=Futbol(nombre,edad,DNI,altura,equipo,deporte,posicionfutbol)
            jugador.set_futbol(posicionfutbol)
        elif deporte.lower()=="baloncesto":
            posicionbaloncesto=input("Introduce la posicion que ocupa el jugador dentro de la cancha:")
            jugadores=Baloncesto(nombre,edad,DNI,altura,equipo,deporte,posicionbaloncesto)
            jugador.set_baloncesto(posicionbaloncesto)
        elif deporte.lower()=="voleibol":
            clase=input("Introduce la clase del jugador:")
            jugador=Voleibol(nombre,edad,DNI,altura,equipo,deporte,clase)
            jugador.set_voleibol(clase)
        elif deporte.lower()=="taekwondo":
            cinturon=input("Introduce el cinturon del jugador:")
            jugador=Taekwondo(nombre,edad,DNI,altura,equipo,deporte,cinturon)
            jugador.set_taekwondo(cinturon)
        else:
            break
        z=input("¿Quires introducir a otro jugador?")
