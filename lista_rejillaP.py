from code import interact
from clases import PatronRejilla

class Lista_rejillaP:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def append(self, patron):
        nuevo = PatronRejilla(patron)

        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        elif self.primero.siguiente is None:
            self.primero.siguiente = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def returnListas(self):
        actual = self.primero

        while actual is not None:
            listaPatron = actual.getPatronRejilla()#tomando la lista del primer patron
            print(actual.getPatronRejilla())

            actual = actual.siguiente





        # CONTARÁ CON 3 OPCIONES-----EN EL RANGO DE LOS PERIODOS ESTABLECIDOS-----

        #ANALIZO EL PATRON INICIAL
            # 1. Que el patron se repita después de N periodos      -> CASO GRAVE                   (SI)
            # 2. Que el patron se repita en el primero periodo N=1  -> MORIRÁ                       (SI)

        #ANALIZO OTRO PATRON QUE NO SEA EL INICIAL
            # 3. algún patron diferente al 1ro. se repita después de N periodos     -> CASO GRAVE   ()
            # 4. algún patron diferente al 1ro. se repita en el primero periodo N=1 -> MORIRÁ       ()

        #SI NO CUMPLE LOS ANTERIORES HARÁ LO SIGUIENTE:
            # 5. que no se repita ni una vez el patron en los periodos establecidos -> CASO LEVE    ()


    def casoA(self, listaActual):
        actual = self.primero
        nodoListaActual = listaActual.returnInfectada()
        verificacion = None
        periodo = 0

        while actual is not None:#almacena diferentes patrones
            periodo += 1
            contador = 0
            listaPatron = actual.getPatronRejilla()

            while (nodoListaActual is not None):#va almacenar varias celulas
                actualX = int(nodoListaActual.getPosX())
                actualY = int(nodoListaActual.getPosY())

                nodoListaPatron = listaPatron.returnInfectada()#Reinicio las posiciones
                for i in range(listaPatron.size):

                    patronX = int(nodoListaPatron.getPosX())
                    patronY = int(nodoListaPatron.getPosY())

                    if patronX == actualX and patronY == actualY:
                        contador += 1 # contador = 14

                        if contador == listaActual.size and periodo == 1:
                            verificacion = True
                        elif contador == listaActual.size:
                            verificacion = False
                    nodoListaPatron = nodoListaPatron.siguiente

                nodoListaActual = nodoListaActual.siguiente
                
            #se analiza el N = 1 de patronInicial
            if verificacion == True:#significa que si es igual el patron
                return 1#Si no es True es porque va a seguir analizando los demas patrones

            if verificacion == False:
                return 2
            actual = actual.siguiente#paso a la siguiente lista que tengo almacenada

    def casoB(self):
        base = self.primero

        while base is not None:
            periodo = 0
            verificacion = None
            listaActual = base.getPatronRejilla()
            actual = base.siguiente

            if actual is None:
                break
            else:
                #EN LA SEGUNDA ITERACION ME TIRA EXCEPT
                self.__derivadaB(listaActual, actual, periodo, verificacion)

            base = base.siguiente



    def __derivadaB(self, listaActual, actual, periodo, verificacion):
        while actual is not None:
            contador = 0
            periodo += 1
            listaPatron = actual.getPatronRejilla()

            nodoListaActual = listaActual.returnInfectada()
            while (nodoListaActual is not None):#va almacenar varias celulas
                actualX = int(nodoListaActual.getPosX())
                actualY = int(nodoListaActual.getPosY())

                nodoListaPatron = listaPatron.returnInfectada()#Reinicio las posiciones
                for i in range(listaPatron.size):

                    patronX = int(nodoListaPatron.getPosX())
                    patronY = int(nodoListaPatron.getPosY())

                    if patronX == actualX and patronY == actualY:
                        contador += 1 # contador = 14

                        if contador == listaActual.size and periodo == 1:
                            verificacion = True
                        elif contador == listaActual.size:
                            verificacion = False
                    nodoListaPatron = nodoListaPatron.siguiente

                nodoListaActual = nodoListaActual.siguiente

            if verificacion == True:#significa que si es igual el patron
                return 1#Si no es True es porque va a seguir analizando los demas patrones

            if verificacion == False:
                return 2

            actual = actual.siguiente