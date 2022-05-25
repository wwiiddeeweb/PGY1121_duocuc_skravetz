Proceso testB
	definir cantidad_asistentes, precio_total, ciclo1, precio_asistentes, precio_menus Como Entero;
	definir respuesta_1 , menus, postre_1, respuesta, postre, respuesta_2, respuesta2 Como Caracter;
	ciclo1 = 0; precio_total = 0;
	escribir "Bienvenid@ a Food and Dance, desea reservar un evento: Si/No?";
	leer respuesta_1;
	respuesta = Minusculas(respuesta_1);
	mientras ciclo1 = 0 y respuesta = "si" o respuesta == "s" o respuesta == "1" Hacer
		escribir "Cuantos asistentes desea?: ";
		leer cantidad_asistentes;
		Si cantidad_asistentes > 200 o cantidad_asistentes < 1 entonces
			escribir "Error en la cantidad de asistentes, el maximo es de 200 y el minimo es de 1, lo sentimos";
			ciclo1 = 1;
		Sino
			escribir "Desea 1 o 2 menus?: ";
			leer menus;
			mientras menus <> "1" y menus <> "2" Hacer
				escribir "Por favor escoja entre 1 o 2 menus";
				leer menus;
			FinMientras
			Si cantidad_asistentes <= 50 y menus = "1" entonces 
				precio_menus = 1000000;
			FinSi
			Si cantidad_asistentes <= 50 y menus = "2" entonces 
				precio_menus = 1500000;
			FinSi
			Si cantidad_asistentes >= 50 y cantidad_asistentes <= 100  y menus = "1" entonces 
				precio_menus = 1800000;
			FinSi
			Si cantidad_asistentes >= 50 y cantidad_asistentes <= 100 y menus = "2" entonces 
				precio_menus = 2300000;
			FinSi
			Si cantidad_asistentes > 100 y cantidad_asistentes <=  200 y menus = "1" entonces 
				precio_menus = 3500000;
			FinSi
			Si cantidad_asistentes > 100 y cantidad_asistentes <=  200 y menus = "2" entonces 
				precio_menus = 4000000;
			FinSi
			escribir "Desea un buffet de postres?: Si/No";
			leer postre_1;
			postre = Minusculas(postre_1);
			si postre <> "si" y postre <> "s" y postre <> "1" Entonces
				escribir "Sin buffet de postres";
			FinSi
			esperar 2 segundo;
			Limpiar Pantalla;
			Si  menus ="1" Entonces
				precio_total = precio_menus;
				escribir ("                     Eventos Food and Dance");
				escribir ("");
				escribir "Hasta " , cantidad_asistentes, " Asistentes  "        ,  precio_menus, " Una Opcion de menu";
				Si postre == "si" o postre == "s" o postre == "1" Entonces
					escribir "Buffet de Postres $500.000";
					precio_total = precio_total + 500000;
				FinSi
				escribir "Total   $", precio_total;
				escribir "                                     Gracias por preferirnos";
			finSi
			Si  menus ="2" Entonces
				precio_total = precio_menus;
				escribir ("                     Eventos Food and Dance");
				escribir ("");
				escribir "Hasta " , cantidad_asistentes, " Asistentes  "        ,  precio_menus, " Dos Opciones de menu";
				Si postre == "si" o postre == "s" o postre == "1" Entonces
					escribir "Buffet de Postres $500.000";
					precio_total = precio_total + 500000;
				Finsi
				escribir "Total  $", precio_total;
				escribir "                                     Gracias por preferirnos";
			FinSi
		Finsi
		esperar 4 segundos;
		Limpiar Pantalla;
		escribir "Desea ingresar otra reserva? Si/No: ";
		leer respuesta_2;
		respuesta2 = Minusculas(respuesta_2);
		esperar 0.8 segundos;
		Limpiar Pantalla;
		Si respuesta2 = "si" o respuesta2 == "s" o respuesta2 == "1" entonces
			ciclo1 = 0;
			escribir "Bienvenid@ a Food and Dance";
		SiNo
			ciclo1 = 1;
		FinSi
	FinMientras
	escribir "Que tenga un buen dia";
FinProceso