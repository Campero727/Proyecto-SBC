import subprocess
import sys

def validar_scope(dir):
	command="nmap -sL "+dir
	result = subprocess.run([command], shell=True, capture_output=True, text=True)
	print(result.stdout)
	resolucion_DNS = input("Quieres que aplique resolucion DNS inversa al objetivo (S/N)")
	if resolucion_DNS=="S":
		print("Aplicare resolucion DNS")
	else:
		print("No aplicare resolucion DNS")


def setScope(scope):
	validar_scope(scope)
