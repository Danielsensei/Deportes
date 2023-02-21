class Jugador():
    def __init__(self,nombre,edad,DNI,altura,equipo):
        self.__nombre=nombre
        self.__edad=edad
        self.__DNI=DNI
        self.__altura=altura
        self.__equipo=equipo
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
class Futbol(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
        super().__init__(nombre,edad,DNI,altura,equipo)
    def set_futbol(self,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
    def get_futbol(self):
        return self.__posicionfutbol
class Baloncesto(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
        super().__init__(nombre,edad,DNI,altura,equipo)
    def set_baloncesto(self,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
    def get_baloncesto(self):
        return self.__posicionbaloncesto
class Voleibol(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,clase):
        self.__clase=clase
        super().__init__(nombre,edad,DNI,altura,equipo)
    def set_voleibol(self,clase):
        self.__clase=clase
    def get_voleibol(self):
        return self.__clase
class Taekwondo(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,cinturon):
        self.__cinturon=cinturon
        super().__init__(nombre,edad,DNI,altura,equipo)
    def set_taekwondo(self,cinturon):
        self.__cinturon=cinturon
    def get_taekwondo(self):
        return self.__cinturon
def main():
    jugadores={}
    z="si"
    while z.lower()=="si":
        jugador=()
        nombre=input("Introduce el nombre del jugador:")
        edad=input("Introduce la edad del jugador:")
        DNI=input("Introduce el DNI del jugador:")
        altura=input("Introduce la altura del jugador:")
        equipo=input("Introduce el equipo al que pertenece:")
        a=input("¿A que tipo de deporte pertenece:futbol, baloncesto, voleibol o taekwondo?")
        print(a)
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
        z=input("¿Quires introducir a otro jugador?")
    for x in range(0,len(jugadores)):
        print(jugadores[x].get_nombre())
        print(jugadores[x].get_edad())
        print(jugadores[x].get_DNI())
        print(jugadores[x].get_altura())
        print(jugadores[x].get_equipo())
        if jugadores[x].get_posicionfutbol()=="futbol":
            print(jugadores[x].get_posicionfutbol())
        elif jugadores[x].get_posicionbaloncesto()=="baloncesto":
            print(jugadores[x].get_posicionbaloncesto())
        elif jugadores[x].get_clase()=="voleibol":
            print(jugadores[x].get_clase())
        elif jugadores[x].get_cinturon()=="taekwondo":
            print(jugadores[x].get_cinturon())
if __name__=="__main__":
    main()