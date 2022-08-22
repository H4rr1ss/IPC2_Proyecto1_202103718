from tkinter import W
from colorama import Fore
from clases import Paciente
from lista_simple import ListaSimpleEnlazada
import xml.etree.ElementTree as ET

def opciones_menu():
    print(Fore.CYAN + "\n     ----------------MENÚ-----------------")
    print(Fore.CYAN + "     |       1. Cargar archivo XML       |")
    print(Fore.CYAN + "     |       2. Mostrar pacientes        |")
    print(Fore.CYAN + "     |       3. Eligir un paciente       |")
    print(Fore.CYAN + "     |       4. Salir                    |")
    print(Fore.CYAN + "     -------------------------------------")

def menu():
    opcion = ""
    listaPacientes = ListaSimpleEnlazada()

    while opcion != "4":
        opciones_menu()
        opcion = input(Fore.CYAN + "\nSeleccione una opción del menú: ")

        if opcion == "1":# Cargar archivo xml
            nombrearchivo = input(Fore.YELLOW + "\nIngrese el nombre del archivo: ")
            ruta = "./" + nombrearchivo
            listaPacientes = cargar_pacientes(ruta)
            print(Fore.GREEN + "   -----------------------------------")
            print(Fore.GREEN + "   | Se cargó el archivo con éxito!! |")
            print(Fore.GREEN + "   -----------------------------------\n")
            print(Fore.LIGHTWHITE_EX + "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        elif opcion == "2":# Mostrar pacientes
            print(Fore.YELLOW + "\n     |-----Pacientes:-----|\n")
            listaPacientes.print()
            print(Fore.LIGHTWHITE_EX + "\n\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        elif opcion == "3":# Elegir un paciente
            pass
        
def cargar_pacientes(ruta):
        # Lista pacientes
        lista_pacientesXML = ListaSimpleEnlazada()
        
        # Atributos paciente
        nombre = ""
        edad = 0
        periodos = 0
        dimension = 0
        # matriz =  ACA VA LA MATRIZ

        while lista_pacientesXML.raiz != None:
            tree = ET.parse(ruta)
            pacientes = tree.getroot()#pacientes

            for pacienteXML in pacientes: # pacienteXML es la etiqueta <Pacientes>
                if pacienteXML.tag == "paciente":

                    for datosXML in pacienteXML: # Entro a la etiqueta <datospersonales>

                        if datosXML.tag == "datospersonales":
                            for dato in datosXML:
                                if dato.tag == "nombre":
                                    nombre = dato.text
                                elif dato.tag == "edad":
                                    edad = int(dato.text)

                        elif datosXML.tag == "periodos": # Entro a la etiqueta <periodos>
                            periodos = int(datosXML.text)

                        elif datosXML.tag == "m":
                            dimension = int(datosXML.text)

                paciente = Paciente(nombre, edad, periodos, dimension) # Creo objeto Paciente con sus atributos
                lista_pacientesXML.append(paciente)
            
            return lista_pacientesXML # Retorna la lista de pacientes

menu()