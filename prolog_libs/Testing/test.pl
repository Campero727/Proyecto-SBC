% Definición de reglas
is_open('ACK', 'ACK flag is open').
is_open('SYN', 'SYNCORNIZATION is open').

check_flag(Flag, Result) :- is_open(Flag, Result).
