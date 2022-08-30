from colorama import Fore
from clases import Celula, Paciente, Patron
from lista_patrones import ListaPatron
from lista_celula import ListaCelula
from lista_simple import Lista_Paciente
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
                patrones = ListaPatron()

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

        # AGARRO LOS DATOS DEL PACIENTE SELECCIONADO
        nombre, edad, periodos, dimension, celulas, patron = listaP.returnPaciente(int(entrada))

        # COPIA DE MATRIZ PACIENTE CON CONTAGIADAS ASIGNADAS A SU POSICIÓN
        listaC = convertirListaCelula(dimension, patron)# Agregarle el patron de contagiadas
        
        # GRAFICAR LA MATRIZ COPIA
        #listaC.graficarLista(nombre, edad, dimension) # patrones lo estoy ingresando como lista
        


        #listaC.mostrarCelulas()
        print("\n -.-.-.-..-.-.--..-.-.-.-")
        #for n in range(periodos) --Va a hacer el rango que le coloqué yo
        nuevoPatron = ListaPatron()
        patronFinal = listaC.comportamientoCelulas(nuevoPatron, dimension)
        #patronReglaUno = listaC.reglaUno(nuevoPatron, dimension)#Retorna las infectadas 
        #listaC.reglaDos(nuevoPatron)

        listaC1 = convertirListaCelula(dimension, patronFinal)# Agregarle el patron de contagiadas
        
        # GRAFICAR LA MATRIZ COPIA
        listaC1.graficarLista(nombre, edad, dimension)



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

menu()