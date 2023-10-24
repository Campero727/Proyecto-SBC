from pyswip import Prolog

# Crear una instancia de Prolog
prolog = Prolog()

# Cargar el archivo de reglas de Prolog
prolog.consult('prolog_libs/metodologias.pl')

metodologias=[]
# Función para buscar una metodologia por tecnologia a auditar
def buscar_metodologia(telecom,web,infraestructura):
	tecnologias=[]
	if telecom=="S":
		tecnologias.append("telecomunicaciones")
	if web=="S":
		tecnologias.append("web")
	if infraestructura=="S":
		tecnologias.append("infraestructura_critica")
	for tecnologia in tecnologias:
		consulta = f"buscar_metodologia('{tecnologia}', Metodologia)"
		resultados = list(prolog.query(consulta))
		for r in resultados:
			metodologias.append(r['Metodologia'])
	print("En base a tus necesidades utilizare las siguientes metodologias")
	for metodologia in metodologias:
		print("[+]"+metodologia)
#print(metodologias)
