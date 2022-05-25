Proceso clase04
	
	Definir sueldo1 Como Entero;
	Definir sueldo2 Como Entero;
	Definir sueldo3 Como Entero;
	
	Escribir "Ingrese sueldo 1";
	Leer sueldo1;
	
	Escribir "Ingrese sueldo 2";
	Leer sueldo2;
	
	Escribir "Ingrese sueldo 3";
	Leer sueldo3;
	
	
	Si sueldo1 > sueldo2 Y sueldo1 > sueldo3 Entonces
		Escribir "Sueldo 1 es mayor que el resto";
	SiNo
		Si sueldo2 > sueldo1 Y sueldo2 > sueldo3 Entonces
			Escribir "Sueldo 2 es mayor que el resto";
		SiNo
			Si sueldo3 > sueldo1 Y sueldo3 > sueldo2 Entonces
				Escribir "Sueldo 3 es mayor que el resto";
			FinSi
		FinSi
	FinSi

	
	
FinProceso
