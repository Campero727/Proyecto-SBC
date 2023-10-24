#-*- coding: utf-8 -*-
from pyswip import Prolog

# Crear una instancia de Prolog
prolog = Prolog()

# Cargar el archivo de reglas de Prolog
prolog.consult('./prolog_libs/custom_scan.pl')

def info_flag():
	flag=input("Ingresa la flag a activar: ")
	query = f"check_flag('{flag}', X)"
	result = list(prolog.query(query))
	print("\n")
	# Imprime el resultado
	for item in result:
		print(item['X'])
	make_package(flag)

def make_package(flag):
	print("\n")
	print("El paquete TCP a enviar sera el siguiente\n");
	print("+-------------------------------+")
	print("| Source Port | Destination Port|")
	print("|        Sequence Number        |")
	print("|    Acknowloadement Number     |")
	print("|Data Ofset|Reserved|"+flag+"|Windows|")
	print("|   CheckSum   | Urgent Pointer |")
	print("|      Options      |   Padding |")
	print("|               data            |")
	print("+-------------------------------+")


def default_package():
	print("\n")
	print("El paquete TCP a enviar sera el siguiente");
	print("+-------------------------------+")
	print("| Source Port | Destination Port|")
	print("|        Sequence Number        |")
	print("|    Acknowloadement Number     |")
	print("|Data Ofset|Reserved|SYN|Windows|")
	print("|   CheckSum   | Urgent Pointer |")
	print("|      Options      |   Padding |")
	print("|               data            |")
	print("+-------------------------------+")

def setFlags():
	opcion = input ("Realizare un escaneo con flags automaticas o personalizado [A]Automatico [C]Custom: ");
	if opcion=="A":
		default_package();
	elif opcion=="C":
		info_flag()


