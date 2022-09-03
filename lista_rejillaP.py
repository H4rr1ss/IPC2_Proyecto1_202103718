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
            print(str(listaPatron.returnInfectadas()))#accediendo a los metodos de esa lista
            print(actual.getPatronRejilla())

            actual = actual.siguiente

    def enfermedad(self, listaActual, periodo):
        actual = self.primero
        nodoListaActual = listaActual.returnInfectada()

        while actual is not None:
            listaPatron = actual.getPatronRejilla()
            
        # Voy a recorrer mis patrones con células contagiadas
        # y comparar con la listaActual hasta percibir una similitud en alguna listaPatron


        # CONTARÁ CON 3 OPCIONES-----EN EL RANGO DE LOS PERIODOS ESTABLECIDOS-----

        #ANALIZO EL PATRON INICIAL
            # 1. Que el patron se repita después de N periodos      -> CASO GRAVE
            # 2. Que el patron se repita en el primero periodo N=1  -> MORIRÁ

        #ANALIZO OTRO PATRON QUE NO SEA EL INICIAL
            # 3. algún patron diferente al 1ro. se repita después de N periodos     -> CASO GRAVE
            # 4. algún patron diferente al 1ro. se repita en el primero periodo N=1 -> MORIRÁ

        #SI NO CUMPLE LOS ANTERIORES HARÁ LO SIGUIENTE:
            # 5. que no se repita ni una vez el patron en los periodos establecidos -> CASO LEVE


            #ANALIZARÉ PATRON INICIAL   <---2CASOS--->
            contador = 0

            while (nodoListaActual is not None):#va almacenar varias celulas
                actualX = int(nodoListaActual.getPosX())
                actualY = int(nodoListaActual.getPosY())

                nodoListaPatron = listaPatron.returnInfectada()#Reinicio las posiciones
                for i in range(listaActual.size):
                    
                    patronX = int(nodoListaPatron.getPosX())
                    patronY = int(nodoListaPatron.getPosY())

                    if patronX == actualX and patronY == actualY:
                        contador += 1


                    nodoListaPatron = nodoListaPatron.siguiente

                nodoListaActual = nodoListaActual.siguiente
                

            if contador < listaActual.size:
                print("No es el mismo patron")
                break
            else:
                print("es identico el patron")


            actual = actual.siguiente#paso a la siguiente lista que tengo almacenada








#<celda f="0" c="5"/>
#<celda f="1" c="5"/>
#<celda f="2" c="5"/>
#<celda f="4" c="1"/>
#<celda f="4" c="2"/>
#<celda f="4" c="3"/>
#<celda f="4" c="6"/>
#<celda f="4" c="7"/>
#<celda f="4" c="8"/>
#<celda f="6" c="4"/>
#<celda f="7" c="4"/>
#<celda f="8" c="4"/>
 



#<celda f="0" c="0"/>
#<celda f="0" c="1"/>
#<celda f="0" c="8"/>
#<celda f="0" c="9"/>
#<celda f="1" c="0"/>
#<celda f="1" c="1"/>
#<celda f="1" c="8"/>
#<celda f="1" c="9"/>
#<celda f="4" c="1"/>
#<celda f="4" c="2"/>
#<celda f="4" c="7"/>
#<celda f="4" c="8"/>
#<celda f="5" c="1"/>
#<celda f="5" c="2"/>
#<celda f="5" c="7"/>
#<celda f="5" c="8"/>
#<celda f="8" c="0"/>
#<celda f="8" c="1"/>
#<celda f="8" c="8"/>
#<celda f="8" c="9"/>
#<celda f="9" c="0"/>
#<celda f="9" c="1"/>
#<celda f="9" c="8"/>
#<celda f="9" c="9"/>