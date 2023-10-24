% Definición de reglas
is_open('ACK', '(Acknowloadge Flag). Se utiliza para acusar recibo de un segmento TCP').
is_open('SYN', '(Synchronize flag) usado para iniciar un 3 way Handshake y sincronizar números de secuencia en el otro host. El número de secuencia debe establecerse aleatoriamente durante el establecimiento de la conexión TCP').

check_flag(Flag, Result) :- is_open(Flag, Result)
