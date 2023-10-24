from pyswip import Prolog

# Inicializa el motor Prolog
prolog = Prolog()

# Carga el archivo Prolog (test.pl) en el motor
prolog.consult('custom_scan.pl')

# Realiza una consulta Prolog
#flag = 'SYN'  # Puedes cambiar a 'SYN' u otra bandera según tus necesidades
#print(type(flag))
flag=input("Ingresa la flag")
query = f"check_flag('{flag}', X)"
result = list(prolog.query(query))

# Imprime el resultado
for item in result:
    print(item['X'])

