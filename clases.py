class Paciente:
    def __init__(self, nombre = None, edad = None, periodos = None, dimension = None, celulas = None, patrones = None):
        # Datos personales
        self.__nombre = nombre
        self.__edad = edad
        # Periodos
        self.__periodos = periodos
        # Dimensión
        self.__dimension = dimension
        # Rejillas
        self.__celulas = celulas
        self.__estado = ""
        self.__patrones = patrones
        # NODO
        self.siguiente = None

    # GETTES-----
    def getNombre(self):
        return self.__nombre

    def getEdad(self):
        return self.__edad

    def getPeriodo(self):
        return self.__periodos

    def getDimension(self):
        return self.__dimension

    def getEstado(self):
        return self.__estado

    # Retornar lista de celdas
    def getListaCelda(self):
        return self.__celulas

    def getListaPatron(self):
        return self.__patrones


#--------------------------------------------------------------------
class Celula:
    def __init__(self, estado, posX, posY):
        self.__estado = estado
        self.__posX = posX
        self.__posY = posY

        #NODO
        self.siguiente = None
        self.anterior = None
    
    # SETTERS
    def setEstado(self, estado):
        self.__estado = estado

    def setPosX(self, x):
        self.__posX = x

    def setPosY(self, y):
        self.__posY = y

    # GETTERS
    def getEstado(self):
        return self.__estado

    def getPosX(self):
        return self.__posX
    
    def getPosY(self):
        return self.__posY
    
class Patron:
    def __init__(self, posX, posY, estado):
        self.__estado = estado
        self.__posX = posX
        self.__posY = posY

        #NODO
        self.siguiente = None

    # GETTERS
    def getPosX(self):
        return self.__posX

    def getPosY(self):
        return self.__posY

    def getEstado(self):
        return self.__estado

    # SETTERS
    def setPosX(self, x):
        self.__posX = x
    
    def setPosY(self, y):
        self.__posY = y
    
    def setEstado(self, estado):
        self.__estado = estado