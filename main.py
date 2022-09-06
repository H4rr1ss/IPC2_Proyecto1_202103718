from unittest import result
from colorama import Fore
from clases import Celula, Paciente, Patron
from lista_patrones import ListaPatron
from lista_celula import ListaCelula
from lista_rejillaP import Lista_rejillaP
from lista_simple import Lista_Paciente
from lista_rejillaP import Lista_rejillaP
import xml.etree.ElementTree as ET

def cargar_pacientes(pacientes):
    lista_pacientesXML = Lista_Paciente() # Lista de pacientes

    # Atributos paciente
    nombre = ""
    edad = ""
    periodos = ""
    dimension = ""

    for pacienteXML in pacientes: # Recorre la etiqueta <pacientes>

        for datosXML in pacienteXML: # Recorre la etiqueta <datospersonales>
            if datosXML.tag == "datospersonales":
                  
                for dato in datosXML:
                    if dato.tag == "nombre":
                        nombre = dato.text
                    elif dato.tag == "edad":
                        edad = int(dato.text)

            elif datosXML.tag == "periodos": # Recorre la etiqueta <periodos>
                periodos = int(datosXML.text)

            elif datosXML.tag == "m": # Recorre la etiqueta <m>
                dimension = int(datosXML.text)

            elif datosXML.tag == "rejilla": # Recorre la etiqueta <rejilla>
                celulas = ListaCelula()
                patrones = ListaPatron() # Almacena el patron inicial de la rejilla

                fila = 0
                columna = 0

                # MATRIZ DE DIMENSION MXM
                for fila in range(dimension):
                    for columna in range(dimension):
                        celulas.append(0, fila, columna) # Lleno mi matriz de O
                    fila += 1
                
                for celdaContagiada in pacienteXML.findall(".//rejilla/celda"): #Ingreso a las posiciones de las infectadas
                    contagiadaX = celdaContagiada.get("f")
                    contagiadaY = celdaContagiada.get("c")
                    patrones.append(contagiadaX, contagiadaY, 1)
    
        paciente = Paciente(nombre, edad, periodos, dimension, celulas, patrones) # Creo objeto Paciente con sus atributos
        lista_pacientesXML.append(paciente)
     
    return lista_pacientesXML # Retorna la lista de pacientes
        
def opciones_menu():
    print(Fore.CYAN + "\n     ----------------MENÚ-----------------")
    print(Fore.CYAN + "     |       1. Cargar archivo XML       |")
    print(Fore.CYAN + "     |       2. Mostrar pacientes        |")
    print(Fore.CYAN + "     |       3. Eligir un paciente       |")
    print(Fore.CYAN + "     |       4. Salir                    |")
    print(Fore.CYAN + "     -------------------------------------")

# Menú general
def menu():
    opcion = ""
    ruta = ""

    while opcion != "4":
        opciones_menu()
        opcion = input(Fore.CYAN + "\nSeleccione una opción del menú: ")
        
        if opcion == "1":# Cargar archivo xml
            try:
                nombrearchivo = input(Fore.YELLOW + "\nIngrese el nombre del archivo: ")
                ruta = "./" + nombrearchivo
                tree = ET.parse(ruta)
                rutaPacientes = tree.getroot()#pacientes
                cargar_pacientes(rutaPacientes)
                print(Fore.GREEN + "   -----------------------------------")
                print(Fore.GREEN + "   | Se cargó el archivo con éxito!! |")
                print(Fore.GREEN + "   -----------------------------------\n")
                print(Fore.LIGHTWHITE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            except:
                print(Fore.RED + "   -----------------------------------")
                print(Fore.RED + "   |    ERROR: Datos no cargados     |")
                print(Fore.RED + "   -----------------------------------\n")
                print(Fore.LIGHTWHITE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        elif opcion == "2":# Mostrar pacientes
            try:
                tree = ET.parse(ruta)
                pacientes = tree.getroot()#pacientes
                listaPacientes = cargar_pacientes(pacientes)
                print(Fore.YELLOW + "\n      |-----Pacientes:-----|\n")
                listaPacientes.print()
                print(Fore.LIGHTWHITE_EX + "\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

            except:
                print(Fore.RED + "   -----------------------------------")
                print(Fore.RED + "   |    ERROR: Datos no cargados     |")
                print(Fore.RED + "   -----------------------------------\n")
                print(Fore.LIGHTWHITE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        elif opcion == "3":# Elegir un paciente para analizar
            try:
                tree = ET.parse(ruta)
                pacientes = tree.getroot()#pacientes
                listaPacientes = cargar_pacientes(pacientes)
                menu_seleccionarPaciente(listaPacientes)
            except:
                print(Fore.RED + "   -----------------------------------")
                print(Fore.RED + "   |    ERROR: Datos no cargados     |")
                print(Fore.RED + "   -----------------------------------\n")
                print(Fore.LIGHTWHITE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            
# Submenú de seleccionar paciente
def menu_seleccionarPaciente(listaP):# Lista de pacientes
    try:
        entrada = 0

        if entrada == 0:
            print(Fore.YELLOW + "\n  ----------------------------------------------------")#12
            print(Fore.LIGHTGREEN_EX + "           ----------------------------")#17
            print(Fore.LIGHTGREEN_EX + "           |  Seleccione un paciente  |")
            print(Fore.LIGHTGREEN_EX + "           ----------------------------\n")

        entrada = input("  Digite el paciente que desea seleccionar: ")
        print()
        #                ----- SE TOMAN LOS DATOS DEL PACIENTE SELECCIONADO -----

        #                                                           primera iteración
        # AGARRO LOS DATOS DEL PACIENTE SELECCIONADO
        nombre, edad, periodos, dimension, celulas, patron = listaP.returnPaciente(int(entrada))
        # COPIA DE MATRIZ PACIENTE CON CONTAGIADAS ASIGNADAS A SU POSICIÓN
        listaC = convertirListaCelula(dimension, patron)# Agregarle el patron de contagiadas
        # GRAFICAR LA MATRIZ COPIA
        listaC.graficarLista(nombre, edad, 0, dimension) # patrones lo estoy ingresando como lista
        
        #Almacenará las listas de los patrones
        almacenPatrones = Lista_rejillaP()
        #almacenPatrones.append(patron)
        #listaC.mostrarCelulas()
        for elemento in range(periodos):
            periodo = elemento + 1
            nuevoPatron = ListaPatron() # Almacena el patron al aplicar las reglas

            # ListaC es la lista base que se analizará
            patronFinal = listaC.comportamientoCelulas(nuevoPatron, dimension)

            # ListaC1 ahora es el nuevo patron con reglas
            listaC1 = convertirListaCelula(dimension, patronFinal)

            listaC1.graficarLista(nombre, edad, periodo, dimension)

            almacenPatrones.append(patronFinal)#Almaceno mi lista de patron en otra lista

            #almacenPatrones.returnListas()#TENGO UNA LISTA DE LAS LISTAS DE PATRONES
            # almacenPatrones = [ #patron1, #patron2, #patronN, .... ]
            listaC = listaC1
            listaC1 = None

        determinarEnfermedad(almacenPatrones, patron)
        print("--------------------------------------")
        almacenPatrones.returnListas()

        print(Fore.YELLOW + "\n  ----------------------------------------------------")#12
    except:
        print(Fore.RED + "   ------------------------------------")
        print(Fore.RED + "   |  ERROR: Eliga una opción válida  |")
        print(Fore.RED + "   ------------------------------------\n")
        print(Fore.LIGHTWHITE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

def convertirListaCelula(dimension, ListaCont):
    lista = ListaCelula()
    fila = 0
    columna = 0

    #ListaCont tiene una posX y poxY determinada para contagiar
    celulaInfectada = ListaCont.returnInfectada()
    
    for fila in range(dimension):
        for columna in range(dimension):
            lista.append(0, fila, columna)
        fila += 1

    lista.mostrarCelulas()
    celulaNormal = lista.returnCelula()

    while celulaInfectada is not None:
        appendInfected(celulaNormal, celulaInfectada.getPosX(), celulaInfectada.getPosY())
        celulaInfectada = celulaInfectada.siguiente
    return lista

def appendInfected(nodoCelula, x, y):
    while nodoCelula is not None:
        if(int(nodoCelula.getPosX()) == int(x)) and (int(nodoCelula.getPosY()) == int(y)):
            nodoCelula.setEstado(1)
        nodoCelula = nodoCelula.siguiente

def determinarEnfermedad(listaPatrones, patronInicial):
    #LUEGO DE HABER APLICADO LOS N PERIODOS, ANALIZO TODOS LOS PATRONES
    if patronInicial is not None:#analizo el patronInicial inicial
        resultado = listaPatrones.casoA(patronInicial)

        if resultado == 1:
            print("El paciente morirá")
            #break
        elif resultado == 2:
            print("El paciente tiene enfermedad grave")
            #break

    listaPatrones.returnListas()
    
    res = listaPatrones.casoB()

    if res == 1:
        print("El paciente morirá")
        #break
    elif res == 2:
        print("El paciente tiene enfermedad grave")
        #break

    if res == None and resultado == None:
        print("sufre una enfermedad leve")
    #if patronFinal is not None: #analizo otro diferente al inicial
        #listaPatrones.enfermedad(patronFinal, periodo)#Enfermedad grave o muerte

    #if resultado is None: #No retorno nada de las anteriores
        #print("Ya que no ocurrio ninguno de los 4 casos anteriores, significa que su enfermedad es leve")

menu()