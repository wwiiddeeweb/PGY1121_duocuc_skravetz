Proceso teatroMoro
	
	// definir variables
	Definir tipoEntrada, valorEntrada, tipoTarifa, instruccion, total Como Entero;
	Definir msgEntrada, msgTarifa Como Caracter;

	Repetir
		Escribir "Sistema de venta de tickets de Teatro Moro";
		Escribir "------------------------------------------";
		Escribir "Indique el tipo de entrada: (1) Platea, (2) Tribuna ó (3) Galería";
		Leer tipoEntrada;
		Mientras tipoEntrada < 1 O tipoEntrada > 3 Hacer
			Escribir "Valor incorrecto, intente nuevamente.";
			Escribir "Indique el tipo de entrada: (1) Platea, (2) Tribuna ó (3) Galería";
			Leer tipoEntrada;
		FinMientras
		
		Escribir "Indique la tarifa: (1) Público General ó (2) Estudiante";
		Leer tipoTarifa;
		Mientras  tipoTarifa < 1 O tipoTarifa > 2 Hacer
			
			Escribir "Valor incorrecto, intente nuevamente.";
			Escribir "Indique la tarifa: (1) Público General ó (2) Estudiante";
			Leer tipoTarifa;
		FinMientras
		
		// mensajes tipo entrada
		Si tipoEntrada = 1 Entonces
			msgEntrada = "Platea";
		SiNo
			si tipoEntrada = 2 Entonces
				msgEntrada = "Tribuna";
			SiNo
				Si tipoEntrada = 3 Entonces
					msgEntrada = "Galería";
				FinSi
			FinSi
		FinSi
		
		// mensajes tipo tarifa
		Si tipoTarifa = 1 Entonces
			msgTarifa = "Público General";
		SiNo
			msgTarifa = "Estudiante";
		FinSi
		
		
		
		// totales
		// 1) Platea, (2) Tribuna ó (3) Galeria
		// (1) Público General ó (2) Estudiante
		
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
		Escribir "------------------------------------------";
		Escribir "				TEATRO MORO 				  ";
		Escribir "------------------------------------------";
		Escribir "Tipo de entrada: ", msgEntrada;
		Escribir "Tarifa: ", msgTarifa;
		Escribir "Total a pagar: $", total;
		Escribir "------------------------------------------";
		Escribir "Gracias por su compra, disfrute la función!";
		Escribir "------------------------------------------";
		
		
		
		// siguiente instruccion a seguir 		
		Escribir "¿Desea comprar otro ticket? (1) Sí, (2) No";
		Leer instruccion;
		
		Limpiar Pantalla;
		
	Hasta Que instruccion = 2;

FinProceso
