class Paciente:
    def __init__(self, nombre = None, edad = None, periodos = None, dimension = None):
        # Datos personales
        self.__nombre = nombre
        self.__edad = edad
        # Periodos
        self.__periodos = periodos
        # Dimensión
        self.__dimension = dimension
        # Rejillas
        #self.rejilla = lista
        self.__estado = ""
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

#--------------------------------------------------------------------
class Celula:
    def __init__(self, estado, posX, posY):
        self.__estado = estado
        self.__posX = posX
        self.__posY = posY
    
    def setEntrada(self, estado):
        self.__estado = estado

    def setPosX(self, x):
        self.__posX = x

    def setPosY(self, y):
        self.__posY = y