Proceso foodanddance
	Definir asistente,precio,precio1menu,precio2menu,total,buffet Como Entero;
	buffet <- 500000;
	Definir resp Como Caracter;
	Escribir 'escriba la cantidad de asistentes necesarios:';
	Leer asistente;
	Si asistente<=50 Entonces
		precio1menu <- 1000000;
		precio2menu <- 1500000;
		Escribir 'cantidad de opciones del menu (uno o dos): ';
		Leer resp;
		Si resp='uno' Entonces
			Escribir 'desea agregar buffet de postres (si/no):';
			Leer resp;
			Si resp='si' Entonces
				total <- precio1menu+buffet;
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio1menu,' Una opcion de menú';
				Escribir ' buffet de postres: $',buffet;
				Escribir ' total: ','$',total;
			SiNo
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio1menu,' Una opcion de menú';
				Escribir ' buffet de postres: Sin buffet';
				Escribir ' total: ','$',precio1menul;
			FinSi
		SiNo
			Escribir 'desea agregar buffet de postres (si/no):';
			Leer resp;
			Si resp='si' Entonces
				total <- precio2menu+buffet;
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio2menu,' Una opcion de menú';
				Escribir ' buffet de postres: $',buffet;
				Escribir ' total: ','$',total;
			SiNo
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio2menu,' Una opcion de menú';
				Escribir ' buffet de postres: Sin buffet';
				Escribir ' total: ','$',precio2menu;
			FinSi
		FinSi
	FinSi
	Si asistente>=51 Y asistente<=100 Entonces
		precio1menu <- 1800000;
		precio2menu <- 2300000;
		Escribir 'cantidad de opciones del menu (uno o dos): ';
		Leer resp;
		Si resp='uno' Entonces
			Escribir 'desea agregar buffet de postres (si/no):';
			Leer resp;
			Si resp='si' Entonces
				total <- precio1menu+buffet;
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio1menu,' Una opcion de menú';
				Escribir ' buffet de postres: $',buffet;
				Escribir ' total: ','$',total;
			SiNo
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio1menu,' Una opcion de menú';
				Escribir ' buffet de postres: Sin buffet';
				Escribir ' total: ','$',precio1menul;
			FinSi
		SiNo
			Escribir 'desea agregar buffet de postres (si/no):';
			Leer resp;
			Si resp='si' Entonces
				total <- precio2menu+buffet;
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio2menu,' Una opcion de menú';
				Escribir ' buffet de postres: $',buffet;
				Escribir ' total: ','$',total;
			SiNo
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio2menu,' Una opcion de menú';
				Escribir ' buffet de postres: Sin buffet';
				Escribir ' total: ','$',precio2menu;
			FinSi
		FinSi
	FinSi
	Si asistente>=101 Y asistente<=200 Entonces
		precio1menu <- 3500000;
		precio2menu <- 4000000;
		Escribir 'cantidad de opciones del menu (uno o dos): ';
		Leer resp;
		Si resp='uno' Entonces
			Escribir 'desea agregar buffet de postres (si/no):';
			Leer resp;
			Si resp='si' Entonces
				total <- precio1menu+buffet;
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio1menu,' Una opcion de menú';
				Escribir ' buffet de postres: $',buffet;
				Escribir ' total: ','$',total;
			SiNo
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio1menu,' Una opcion de menú';
				Escribir ' buffet de postres: Sin buffet';
				Escribir ' total: ','$',precio1menul;
			FinSi
		SiNo
			Escribir 'desea agregar buffet de postres (si/no):';
			Leer resp;
			Si resp='si' Entonces
				total <- precio2menu+buffet;
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio2menu,' Una opcion de menú';
				Escribir ' buffet de postres: $',buffet;
				Escribir ' total: ','$',total;
			SiNo
				Escribir '      eventos ','Food and Dance';
				Escribir ' hasta ',asistente,' personas',' $',precio2menu,' Una opcion de menú';
				Escribir ' buffet de postres: Sin buffet';
				Escribir ' total: ','$',precio2menu;
			FinSi
		FinSi
	FinSi
FinProceso
