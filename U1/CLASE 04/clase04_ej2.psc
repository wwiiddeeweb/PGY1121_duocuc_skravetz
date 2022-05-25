
	
Proceso clase04_ej2
	
	Definir capacidad_bus Como Entero;
	capacidad_bus <- 35;
	
	Definir instruccion Como Caracter;
	Leer instruccion;
	
		
	Si capacidad_bus = 35 Y instruccion = "venta" Entonces
		capacidad_bus <- capacidad_bus -1;
		Escribir "Ticket Vendido";
		Escribir "Tickets Restantes: ", capacidad_bus;

	SiNo
		Si capacidad_bus = 34 Y instruccion = "venta" Entonces
			capacidad_bus <- capacidad_bus -1;
			Escribir "Ticket Vendido";
			Escribir "Tickets Restantes: ", capacidad_bus;
		SiNo
			Si capacidad_bus = 33 Y instruccion = "venta" Entonces
				capacidad_bus <- capacidad_bus -1;
				Escribir "Ticket Vendido";
				Escribir "Tickets Restantes: ", capacidad_bus;
		Si instruccion = "consulta" Entonces
			Escribir capacidad_bus;

		FinSi
	FinSi
FinSi
FinSi

	

	
	
FinProceso
