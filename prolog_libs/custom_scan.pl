% Definición de reglas
is_open('ACK', '(Acknowloadge Flag). Se utiliza para acusar recibo de un segmento TCP').
is_open('SYN', '(Synchronize flag) usado para iniciar un 3 way Handshake y sincronizar numeros de secuencia en el otro host. El numero de secuencia debe establecerse aleatoriamente durante el establecimiento de la conexion TCP.').
is_open('URG', '(Urgent Flag) La urgent flag indica que los datos entrantes son urgentes y que un segmento TCP con el indicador URG establecido se procesa inmediatamente sin tener que esperar segmentos TCP enviados previamente').
is_open('PSH', '(Push Flag) Solicita a TCP que pase los datos a la aplicacion de inmediato').
is_open('RST', '(Reset Flag) Se utiliza para establecer la conexion, un firewall podria enviarlo para interrumpir una conexion').
is_open('FIN','El remitente no tiene mas datos que enviar').

check_flag(Flag, Result) :- is_open(Flag, Result).
