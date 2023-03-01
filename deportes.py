class Jugador():
    def __init__(self,nombre,edad,DNI,altura,equipo,puntosdeliga):
        self.__nombre=nombre
        self.__edad=edad
        self.__DNI=DNI
        self.__altura=altura
        self.__equipo=equipo
        self.__puntosdeliga=puntosdeliga
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
    def set_puntosdeliga (self,puntosdeliga):
        self.__puntosdeliga=puntosdeliga
    def get_puntosdeliga (self):
        return self.__puntosdeliga
class Futbol(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,puntosdeliga,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
        super().__init__(nombre,edad,DNI,altura,equipo,puntosdeliga)
    def set_futbol(self,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
    def get_futbol(self):
        return self.__posicionfutbol
class Baloncesto(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,puntosdeliga,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
        super().__init__(nombre,edad,DNI,altura,equipo,puntosdeliga)
    def set_baloncesto(self,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
    def get_baloncesto(self):
        return self.__posicionbaloncesto
class Voleibol(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,puntosdeliga,clase):
        self.__clase=clase
        super().__init__(nombre,edad,DNI,altura,equipo,puntosdeliga)
    def set_voleibol(self,clase):
        self.__clase=clase
    def get_voleibol(self):
        return self.__clase
class Taekwondo(Jugador):
    def __init__(self,nombre,edad,DNI,altura,equipo,puntosdeliga,cinturon):
        self.__cinturon=cinturon
        super().__init__(nombre,edad,DNI,altura,equipo,puntosdeliga)
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
        edad=int(input("Introduce la edad del jugador:"))
        DNI=input("Introduce el DNI del jugador:")
        altura=input("Introduce la altura del jugador:")
        equipo=input("Introduce el equipo al que pertenece:")
        puntosdeliga=input("Introduce la cantidad de puntos que tiene el jugador:")
        a=input("¿A que tipo de deporte pertenece:futbol, baloncesto, voleibol o taekwondo?")
        if a.lower()=="futbol":
            posicionfutbol=input("Introduce la posicion que ocupa el jugador dentro del campo:")
            jugador=Futbol(nombre,edad,DNI,altura,equipo,puntosdeliga,posicionfutbol)
            jugador.set_futbol(posicionfutbol)
        elif a.lower()=="baloncesto":
            posicionbaloncesto=input("Introduce la posicion que ocupa el jugador dentro de la cancha:")
            jugador=Baloncesto(nombre,edad,DNI,altura,equipo,puntosdeliga,posicionbaloncesto)
            jugador.set_baloncesto(posicionbaloncesto)
        elif a.lower()=="voleibol":
            clase=input("Introduce la clase del jugador:")
            jugador=Voleibol(nombre,edad,DNI,altura,equipo,puntosdeliga,clase)
            jugador.set_voleibol(clase)
        elif a.lower()=="taekwondo":
            cinturon=input("Introduce el cinturon del jugador:")
            jugador=Taekwondo(nombre,edad,DNI,altura,equipo,puntosdeliga,cinturon)
            jugador.set_taekwondo(cinturon)
        z=input("¿Quires introducir a otro jugador?")
def mostrar():
    jugadores={}
    jugador= input("Introduzca el nombre del jugador que quiere ver sus caracteristicas:")
    for jugador in range(0,len(jugadores)):
        print(jugador.get_nombre())
        print(jugador.get_edad())
        print(jugador.get_DNI())
        print(jugador.get_altura())
        print(jugador.get_equipo())
        print(jugador.get_puntosdeliga())
        if jugador.get_posicionfutbol()=="futbol":
            print(jugador.get_posicionfutbol())
        elif jugador.get_posicionbaloncesto()=="baloncesto":
            print(jugador.get_posicionbaloncesto())
        elif jugador.get_clase()=="voleibol":
            print(jugador.get_clase())
        elif jugador.get_cinturon()=="taekwondo":
            print(jugador.get_cinturon())
def esMayorDeEdad():
    jugadores={}
    main()
    jugador= input("Introduzca el nombre del jugador que quiere sabers i es mayor de edad:")
    for jugador in range(0,len(jugadores)):
        if edad>=18:
            print ("El jugador o jugadora es mayor de edad")
        else:
            print ("El jugador o jugadora es menor de edad")
if __name__=="__main__":
    jugadores={}
    z="si"
    while z.lower()=="si":
        jugador=()
        nombre=input("Introduce el nombre del jugador:")
        edad=int(input("Introduce la edad del jugador:"))
        DNI=input("Introduce el DNI del jugador:")
        altura=input("Introduce la altura del jugador:")
        equipo=input("Introduce el equipo al que pertenece:")
        puntosdeliga=input("Introduce la cantidad de puntos que tiene el jugador:")
        a=input("¿A que tipo de deporte pertenece:futbol, baloncesto, voleibol o taekwondo?")
        if a.lower()=="futbol":
            posicionfutbol=input("Introduce la posicion que ocupa el jugador dentro del campo:")
            jugador=Futbol(nombre,edad,DNI,altura,equipo,puntosdeliga,posicionfutbol)
            jugador.set_futbol(posicionfutbol)
        elif a.lower()=="baloncesto":
            posicionbaloncesto=input("Introduce la posicion que ocupa el jugador dentro de la cancha:")
            jugador=Baloncesto(nombre,edad,DNI,altura,equipo,puntosdeliga,posicionbaloncesto)
            jugador.set_baloncesto(posicionbaloncesto)
        elif a.lower()=="voleibol":
            clase=input("Introduce la clase del jugador:")
            jugador=Voleibol(nombre,edad,DNI,altura,equipo,puntosdeliga,clase)
            jugador.set_voleibol(clase)
        elif a.lower()=="taekwondo":
            cinturon=input("Introduce el cinturon del jugador:")
            jugador=Taekwondo(nombre,edad,DNI,altura,equipo,puntosdeliga,cinturon)
            jugador.set_taekwondo(cinturon)
        jugadores.append(jugador)
        z=input("¿Quires introducir a otro jugador?")
    mostrar()
    esMayorDeEdad()
