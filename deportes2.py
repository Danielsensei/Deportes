class Jugador():
    def __init__(self,nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte):
        self.__nombrejugador=nombrejugador
        self.__edad=edad
        self.__DNI=DNI
        self.__altura=altura
        self.__equipo=equipo
        self.__puntosdeliga=puntosdeliga
        self.__deporte=deporte
    def set_nombrejugador (self,nombrejugador):
        self.__nombrejugador=nombrejugador
    def get_nombrejugador (self):
        return self.__nombrejugador
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
    def set_deporte (self,deporte):
        self.__deporte=deporte
    def get_deporte (self):
        return self.__deporte
class Futbol(Jugador):
    def __init__(self,nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,posicionfutbol):
        self.__posicionfutbol=posicionfutbol
        super().__init__(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte)
<<<<<<< HEAD
    def set_posicionfutbol(self,posicionfutbol):
=======
    def set_futbol(self,posicionfutbol):
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        self.__posicionfutbol=posicionfutbol
    def get_posicionfutbol(self):
        return self.__posicionfutbol
class Baloncesto(Jugador):
    def __init__(self,nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
        super().__init__(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte)
<<<<<<< HEAD
    def set_posicionbaloncesto(self,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
    def get_posicionbaloncesto(self):
=======
    def set_baloncesto(self,posicionbaloncesto):
        self.__posicionbaloncesto=posicionbaloncesto
    def get_baloncesto(self):
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        return self.__posicionbaloncesto
class Voleibol(Jugador):
    def __init__(self,nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,clase):
        self.__clase=clase
        super().__init__(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte)
<<<<<<< HEAD
    def set_clase(self,clase):
        self.__clase=clase
    def get_clase(self):
=======
    def set_voleibol(self,clase):
        self.__clase=clase
    def get_voleibol(self):
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        return self.__clase
class Taekwondo(Jugador):
    def __init__(self,nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,cinturon):
        self.__cinturon=cinturon
        super().__init__(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte)
<<<<<<< HEAD
    def set_cinturon(self,cinturon):
        self.__cinturon=cinturon
    def get_cinturon(self):
=======
    def set_taekwondo(self,cinturon):
        self.__cinturon=cinturon
    def get_taekwondo(self):
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        return self.__cinturon

def mostrar():
    nombrejugador=input("¿Cual es el jugador que quieres que se te muestre?")
<<<<<<< HEAD
    for i in range(0,len(personas)):
        if personas[i].get_nombrejugador()==nombrejugador:
            print("El nombre de jugador es ",personas[i].get_nombrejugador())
            print("La edad del jugador es ",personas[i].get_edad())
            print("El DNI del jugador es ",personas[i].get_DNI())
            print("La altura del jugador es",personas[i].get_altura())
            print("El equipo al que pertenece el jugador es ",personas[i].get_equipo())
            print("Los puntos de liga del jugador son ",personas[i].get_puntosdeliga())
            print("El deporte del jugador es ",personas[i].get_deporte())
            if personas[i].get_deporte()=="futbol":
                print("Su posicion en el equipo es ",personas[i].get_posicionfutbol())
            elif personas[i].get_deporte()=="baloncesto":
                print("Su posicion en el equipo es ",personas[i].get_posicionbaloncesto())
            elif personas[i].get_deporte()=="voleibol":
                print("La clase del jugador es ",personas[i].get_clase())
            elif personas[i].get_deporte()=="taekwondo":
                print("El cinturon del jugador es ", personas[i].get_cinturon())
            break
        else:
            print("Este jugador no se encuentra entre las personas que has introducido")
            break

def esMayorDeEdad():
    nombrejugador=input("Introduzca el nombre del jugador que desea saber si es mayor de edad:")
    for i in range(0,len(personas)):
        if personas[i].get_nombrejugador()==nombrejugador:
            if personas[i].get_edad()>=18:
                print ("El jugador o jugadora es mayor de edad")
            else:
                print ("El jugador o jugadora es menor de edad")

def darDeBaja():
    nombrejugador=input("Introduzca el nombre del jugador al que quiera dar de baja:")
    for i in range(0,len(personas)):
        if personas[i].get_nombrejugador()==nombrejugador:
            print(personas[i].get_nombrejugador())
            personas.remove(personas[i])
            print("Este jugador ha sido eliminado")
            break
        else:
            print("Este jugador no esta entre las personas que has introducido")

def cambiarValorDeJugador():
    nombrejugador=input("Introduce el nombre del jugador al que quieres modificar una de sus caracteristicas:")
    for i in range(0,len(personas)):
        if personas[i].get_nombrejugador()==nombrejugador:
            x=input("Introduce el valor que quieras cambiar:nombre, edad, DNI, altura, equipo, puntos de liga o (posicion de futbol, posicion baloncesto, clase de jugador de voleibol o cinturon):")
            if x=="jugador":
                nombrejugador=input("Introduce el nombre del jugador:")
                personas[i].set_nombrejugador(nombrejugador)
            if x=="edad":
                edad=input("Introduce la edad del jugador:")
                personas[i].set_edad(edad)
            if x=="DNI":
                DNI=input("Introduce el DNI del jugador:")
                personas[i].set_DNI(DNI)
            if x=="altura":
                altura=input("Introduce la altura del jugador:")
                personas[i].set_altura(altura)
            if x=="equipo":
                equipo=input("Introduce el equipo al que pertenece el jugador:")
                personas[i].set_equipo(equipo)
            if x=="puntos de liga":
                puntosdeliga=input("Introduce los puntos de liga del jugador:")
                personas[i].set_puntosdeliga(puntosdeliga)
            if personas[i].get_deporte()=="futbol":
                if x=="posicion de futbol" or "posición de futbol":
                    posicionfutbol=input("Introduce la posicion del jugador:")
                    personas[i].set_posicionfutbol(posicionfutbol)
            if personas[i].get_deporte()=="baloncesto":
                if x=="posicion de baloncesto" or "posición de baloncesto":
                    posicionbaloncesto=input("Introduce la posicion del jugador:")
                    personas[i].set_posicionbaloncesto(posicionbaloncesto)
            if personas[i].get_deporte()=="voleibol":
                if x=="clase de jugador de voleibol":
                    clase=input("Introduce la clase del jugador:")
                    personas[i].set_clase(clase)
            if personas[i].get_deporte()=="taekwondo":
                if x=="cinturon" or "cinturón":
                    cinturon=input("Introduce el cinturon que tiene el jugador:")
                    personas[i].set_cinturon(cinturon)

def puntosDeLiga():
    nombrejugador=input("Introduzca el nombre del jugador que desea saber sus puntos de liga:")
    for i in range(0,len(personas)):
        if personas[i].get_nombrejugador()==nombrejugador:
            print("Los puntos de liga que tiene el jugador son ",personas[i].get_puntosdeliga())
=======
    for nombrejugador in personas:
        print(nombrejugador.get_nombrejugador())
        print(nombrejugador.get_edad())
        print(nombrejugador.get_DNI())
        print(nombrejugador.get_altura())
        print(nombrejugador.get_equipo())
        if nombrejugador.get_posicionfutbol()=="futbol":
            print(nombrejugador.get_posicionfutbol())
        elif nombrejugador.get_posicionbaloncesto()=="baloncesto":
            print(nombrejugador.get_posicionbaloncesto())
        elif nombrejugador.get_clase()=="voleibol":
            print(nombrejugador.get_clase())
        elif nombrejugador.get_cinturon()=="taekwondo":
            print(nombrejugador.get_cinturon())

def esMayorDeEdad():
    nombrejugador=input("Introduzca el nombre del jugador que desea saber si es mayor de edad")
    for nombrejugador in personas:
        if edad>=18:
            print ("El jugador o jugadora es mayor de edad")
        else:
            print ("El jugador o jugadora es menor de edad")

def darDeBaja():
    jugadoreliminado=input("Introduzca el nombre del jugador al que quiera dar de alta")
    for nombrejugador in personas:
        if nombrejugador==jugadoreliminado:
            personas.remove(nombrejugador)
            break
        else:
            print("Este jugador no esta entre las personas que has introducido")
            break
        

def puntosDeLiga():
    nombrejugador=input("Introduzca el nombre del jugador que desea saber sus puntos de liga:")
    for nombrejugador in personas:
        print("LOs puntos de liga que tiene el jugador son ",puntosdeliga)
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845


def darDeAlta():
    z="si"
    while z.lower()=="si":
<<<<<<< HEAD
=======
        nombrejugador=[]
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        nombrejugador=input("Introduce el nombre del jugador:")
        edad=int(input("Introduce la edad del jugador:"))
        DNI=input("Introduce el DNI del jugador:")
        altura=input("Introduce la altura del jugador:")
        equipo=input("Introduce el equipo al que pertenece:")
        puntosdeliga=input("Introduce la cantidad de puntos que tiene el jugador:")
        deporte=input("¿A que tipo de deporte pertenece:futbol, baloncesto, voleibol o taekwondo?")
        if deporte.lower()=="futbol":
            posicionfutbol=input("Introduce la posicion que ocupa el jugador dentro del campo:")
            nombrejugador=Futbol(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,posicionfutbol)
<<<<<<< HEAD
            nombrejugador.set_posicionfutbol(posicionfutbol)
        elif deporte.lower()=="baloncesto":
            posicionbaloncesto=input("Introduce la posicion que ocupa el jugador dentro de la cancha:")
            nombrejugador=Baloncesto(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,posicionbaloncesto)
            nombrejugador.set_posicionbaloncesto(posicionbaloncesto)
        elif deporte.lower()=="voleibol":
            clase=input("Introduce la clase del jugador:")
            nombrejugador=Voleibol(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,clase)
            nombrejugador.set_clase(clase)
        elif deporte.lower()=="taekwondo":
            cinturon=input("Introduce el cinturon del jugador:")
            nombrejugador=Taekwondo(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,cinturon)
            nombrejugador.set_cinturon(cinturon)
        personas.append(nombrejugador)
        break

if __name__=="__main__":       
    personas=[]
=======
            nombrejugador.set_futbol(posicionfutbol)
        elif deporte.lower()=="baloncesto":
            posicionbaloncesto=input("Introduce la posicion que ocupa el jugador dentro de la cancha:")
            nombrejugador=Baloncesto(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,posicionbaloncesto)
            nombrejugador.set_baloncesto(posicionbaloncesto)
        elif deporte.lower()=="voleibol":
            clase=input("Introduce la clase del jugador:")
            nombrejugador=Voleibol(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,clase)
            nombrejugador.set_voleibol(clase)
        elif deporte.lower()=="taekwondo":
            cinturon=input("Introduce el cinturon del jugador:")
            nombrejugador=Taekwondo(nombrejugador,edad,DNI,altura,equipo,puntosdeliga,deporte,cinturon)
            nombrejugador.set_taekwondo(cinturon)
        nombrejugador.append(personas)

if __name__=="__main__":
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
    print("Si quieres dar de alta jugador, pulse 1")
    print("Si quieres que te muestre las caracteristicas de un jugador, pulse 2")
    print("Si quieres saber si el jugador es mayor de edad, pulse 3")
    print("Si quieres dar de baja a un jugador, pulse 4")
    print("Si quieres ver los puntos de liga de un jugador, pulse 5")
<<<<<<< HEAD
    print("Si quieres cambiar el valor de algun dato de un jugador, pulse 6")
    x=input("Introduce: ")
    while x=="1" or x=="2" or x=="3" or x=="4" or x=="5" or x=="6":
=======
    x=input("Introduce: ")
    while x=="1" or x=="2" or x=="3" or x=="4" or x=="5":
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        if x=="1":
            darDeAlta()
        elif x=="2":
            mostrar()
        elif x=="3":
            esMayorDeEdad()
        elif x=="4":
            darDeBaja()
        elif x=="5":
            puntosDeLiga()
<<<<<<< HEAD
        elif x=="6":
            cambiarValorDeJugador()
        
=======
        personas={}
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        print("Si quieres dar de alta jugador, pulse 1")
        print("Si quieres que te muestre las caracteristicas de un jugador, pulse 2")
        print("Si quieres saber si el jugador es mayor de edad, pulse 3")
        print("Si quieres dar de baja a un jugador, pulse 4")
        print("Si quieres ver los puntos de liga de un jugador, pulse 5")
<<<<<<< HEAD
        print("Si quieres cambiar el valor de algun dato de un jugador, pulse 6")
=======
>>>>>>> 05cb59048e02f8e6e7652d8ece5f680b4b55a845
        x=input("Introduce: ")
