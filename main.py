from python_libs.get_metodologia import buscar_metodologia
from python_libs.setScope import setScope
from python_libs.make_package import setFlags

if __name__=="__main__":
	telecom = input("Auditare un sistema de telecomunicaciones (S/N) -->").strip()
	web  = input("Auditare un sistema web (S/N) -->").strip()
	infraestructura =  input("Auditare un sistema de infraestructura critica (S/N) -->").strip()
	metodologias_encontradas = buscar_metodologia(telecom,web,infraestructura)

	print("Ahora necesito que definas el alcance, asegurate de seleccionar solo una opcion")
	scope=input("Ingresa una IP, rango o subred que sera el objetivo: ")
	setScope(scope)
	setFlags(scope)
