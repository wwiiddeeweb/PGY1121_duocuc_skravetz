Proceso teatroMoro
	
	Definir tipoEntrada, tipoTarifa, total, instruccion Como Entero;
	Definir msgEntrada, msgTarifa Como Caracter;
	
	
	// init
	Repetir 
		
		// welcome screen
		Escribir "---------------------------------------------------------------";
		Escribir "		                 Ticketera TEATRO MORO	                 ";
		Escribir "---------------------------------------------------------------";
		Escribir "		                    Lista de Precios	                 ";
		Escribir "---------------------------------------------------------------";
		Escribir "Platea:  Gral $15000 | Estudiantes: $9000 ";
		Escribir "Tribuna: Gral $9000 | Estudiantes: $5000  ";
		Escribir "Galería: Gral $5200 | Estudiantes: $3500  ";
		Escribir "---------------------------------------------------------------";
		Escribir "Ingrese tipo de entrada: (1) Platea, (2) Tribuna ó, (3) Galería";
		Leer tipoEntrada;
		Mientras tipoEntrada < 1 o tipoEntrada > 3 Hacer
			Escribir "Ha ingresado un valor incorrecto, intente nuevamente.";
			Escribir "Ingrese tipo de entrada: (1) Platea, (2) Tribuna ó, (3) Galería";
			Leer tipoEntrada;
		FinMientras
		Escribir "Seleccione tarifa: (1) Público General, (2) Estudiante";
		Leer tipoTarifa;
		Mientras tipoTarifa < 1 o tipoTarifa > 2 Hacer
			Escribir "Ha ingresado un valor incorrecto, intente nuevamente.";
			Escribir "Seleccione tarifa: (1) Público General, (2) Estudiante";
			Leer tipoTarifa;
		FinMientras
		
		
		// msgs
		Si tipoEntrada = 1 Entonces
			msgEntrada = "Platea";
		SiNo
			Si tipoEntrada = 2 Entonces
				msgEntrada = "Tribuna";
			SiNo
				msgEntrada = "Galería";
			FinSi
		FinSi
		
		Si tipoTarifa = 1 Entonces
			msgTarifa = "Público General";
		SiNo
			msgTarifa = "Estudiante";
		FinSi
		
		
		// calc ticket
		// (1) Platea, (2) Tribuna ó, (3) Galería
		// (1) pub gral, (2) estudiante
		
		Si tipoEntrada = 1 y tipoTarifa = 1 Entonces
			total = 15000;
		SiNo
			si tipoEntrada = 1 y tipoTarifa = 2 Entonces
				total = 9000;
			FinSi
		FinSi
		
		Si tipoEntrada = 2 y tipoTarifa = 1 Entonces
			total = 9000;
		SiNo
			si tipoEntrada = 2 y tipoTarifa = 2 Entonces
				total = 5000;
			FinSi
		FinSi
		
		Si tipoEntrada = 3 y tipoTarifa = 1 Entonces
			total = 5200;
		SiNo
			si tipoEntrada = 3 y tipoTarifa = 2 Entonces
				total = 3500;
			FinSi
		FinSi
		
		
		
		// print
		
		Limpiar Pantalla;
		
		Escribir "---------------------------------------------------------------";
		Escribir "		                 Ticketera TEATRO MORO	                 ";
		Escribir "---------------------------------------------------------------";
		Escribir "Tipo de entrada: ", msgEntrada;
		Escribir "Tarifa: ", msgTarifa;
		Escribir "Total a pagar: $", total;
		Escribir "---------------------------------------------------------------";
		Escribir "Gracias por su compra, disfrute la función! :)";
		Escribir "---------------------------------------------------------------";
		
		
		
		
		// next action
		Escribir "¿Desea comprar otro ticket? (1) Sí, (2) No";
		leer instruccion;
		
		Limpiar Pantalla;
		
		
		
	Hasta Que instruccion = 2;
	
	
	
	
	
FinProceso
