% Definición de metodologias
metodologia(osstmm, telecomunicaciones).
metodologia(owasp, web).
metodologia(nist_caf, infraestructura_critica).

% Regla para buscar una metodologia
buscar_metodologia(Tecnologia, Metodologia) :-
    metodologia(Metodologia, Tecnologia).
