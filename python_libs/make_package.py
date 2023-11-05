#-*- coding: utf-8 -*-
from pyswip import Prolog
from os import system
import re

# Crear una instancia de Prolog
prolog = Prolog()

# Cargar el archivo de reglas de Prolog
#prolog.consult('./prolog_libs/custom_scan.pl')

ports_arr=[]

def consultar_puertos():
	prolog.consult('./prolog_libs/states.pl')
	for port in ports_arr:
		query = f"check_ports_states('{port}', X)"
		result_ports = list(prolog.query(query))
		print("\n")
		# Imprime el resultado
		for item in result_ports:
			print(item['X'])
	#make_package(flag)
	#run_scan(flag,target)


def advanced_scan(target):
	advanced_scan=input("[S] Continuar [N] Cancelar")
	if advanced_scan=="S":
		ports=input("Ingresa los puertos que desees investigar separados por comas Ej: 10,20: ")
		for port in ports.split(","):
			ports_arr.append(port)
		consultar_puertos()
		command="sudo nmap -p"+ports+" -sCV "+target
		system(command)
		port_list=ports.split(",")
		if "80" in port_list:
			fuzz_sub=input("Servidor Web detectado, Deseas que realize un Fuzzing de subdominios [S/N]: ")
			if fuzz_sub=="S":
				wordlist = input("Ingresa la wordlist a utilizar: ")
				command="wfuzz -c -w "+wordlist+" -u 'http://"+target+"' -H 'Host:FUZZ."+target+"' --hw 977 > temp_fuzz"
				system(command)
				system("cat temp_fuzz | grep 200 | grep -vE '977 W' | awk '{print $13}' > tmp_sub1")
				with open('tmp_sub1','r') as file:
					data=file.read()
				data = data[1:-1]
				data = data.replace('"', '')
				print("Subdominio encontrado: "+data)
				conf_peticion=input("Puedo realizar una peticion a la pagina [S/N]: ")
				command="wget http://"+data+"."+target+""
				sub=data
				system(command)
				print("\n\n Te muestro la pagina web inicial")
				system("cat index.html > req_res")
				with open('req_res','r') as file_req:
					data=file_req.read();
				print(data)
				regex = r"href=([^ ]+)"
				matches = re.findall(regex, data)
				match=matches[0];
				if match != "":
					print("\n Posible LFI:")
					print(matches[0])
					cadena=matches[0]
					val_lfi = cadena.find("=")
					subcadena = cadena[:val_lfi]
					print("Puedo realizar fuzzing de LFI sobre http://"+sub+"."+target+"/"+subcadena+"=FUZZ")
					test_lfi_ans=input("[S/N]")
					if test_lfi_ans=="S":
						with open ('lfi','r') as file_lfi:
							for line in file_lfi:
								print("\n\nFile: "+line)
								command="curl http://"+sub+"."+target+"/"+subcadena+"="+line
								system(command)
					else:
						print("")
				else:
					print("")
			else:
				exit()
	elif advanced_scan=="N":
		exit()

def run_scan(flag,target):
	#scan=subprocess.Popen(["/usr/bin/nmap ","-h"],stdout=subprocess.PIPE)
	#output=scan.communicate()[0]
	command="sudo nmap -p- --open --min-rate 5000 --scanflags "+flag+" "+target+" -vvv -oN allPorts"
	system(command)
	print("\nLos siguientes puertos fueron encontrados, los resultados de almacenaron en el archivo [allPorts], proceder con analisis detallado")
	system("cat allPorts | awk '{print $1}' | cut -d '/' -f1 | grep -vE '#|Nmap|Host|Not|PORT|Increasing|Scanned|Some|Read'")
	advanced_scan(target);
	#with  open('allPorts','r') as file:
	#	 print(file.read())
	#advanced_scan=input("[S] Continuar [N] Cancelar")
	#if advanced_scan=="S":
	#	ports=input("Ingresa los pueertos que desees investigar separados por comas Ej: 10,20: ")
	#	command="sudo nmap -p"+ports+" -sCV "+target
	#	system(command)
	#elif advanced_scan=="N":
	#	exit()

def info_flag(target):
	prolog.consult('./prolog_libs/custom_scan.pl')
	flag=input("Ingresa la flag a activar: ")
	query = f"check_flag('{flag}', X)"
	result = list(prolog.query(query))
	print("\n")
	# Imprime el resultado
	for item in result:
		print(item['X'])
	make_package(flag)
	run_scan(flag,target)

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


def default_package(target):
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

	command="sudo nmap -p- --open -sS --min-rate 5000 -n -Pn -vvv "+target+" -oN allPorts"
	system(command)
	print("\nLos siguientes puertos fueron encontrados, los resultados de almacenaron en el archivo [allPorts], proceder con analisis detallado")
	system("cat allPorts | awk '{print $1}' | cut -d '/' -f1 | grep -vE '#|Nmap|Host|Not|PORT|Increasing|Scanned|Some|Read'")
	advanced_scan(target);

def setFlags(scope):
	scope=scope
	opcion = input ("Realizare un escaneo con flags automaticas o personalizado [A]Automatico [C]Custom: ");
	if opcion=="A":
		default_package(scope);
	elif opcion=="C":
		info_flag(scope)

