%definicion de reglas
is_open('21', 'Puerto FTP abierto').
is_open('22','Puerto SSH abierto').
is_open('23','Puerto telnet abierto').
is_open('53','Puerto DNS abierto').
is_open('80','Puerto HTTP abierto').
is_open('445','Puerto SMB abierto').
is_open('3306','Puerto Mysql abierto').


check_ports_states(Port, Result) :- is_open(Port, Result).

