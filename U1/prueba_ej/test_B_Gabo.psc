Proceso food_and_dance
	//Definiciones
	Definir resp1, cant, menu, postre, total Como Entero;
	Definir text1, text2 Como Caracter;
	Escribir "Bienvenido a Food and Dance";
	Repetir
		//Inicializaciones
		total<-0;
		//Ingreso datos 
		Escribir "¿Para qué cantidad de personas es el evento? (límite 200 personas)";
		Leer cant;
		Escribir "¿Qué opción de menú desea? Con una opción (1) o con dos opciones (2)";
		Leer menu;
		Escribir "¿Desea postre? Sí (1) No (0)";
		Leer postre;
		//Proceso 
		Si cant<=50 Entonces
			si menu==1 Entonces
				total<-total+1000000;
				text1<-"Hasta 50 personas: $1.000.000 (Una opción de menú)";
			SiNo
				total<-total+1500000;
				text1<-"Hasta 50 personas: $1.500.000 (Dos opciones de menú)";
			FinSi
		FinSi
		Si cant>50 y cant<=100 Entonces
			Si menu==1 Entonces
				total<-total+1800000;
				text1<-"Hasta 100 personas: $1.800.000 (Una opción de menú)";
			SiNo
				total<-total+2300000;
				text1<-"Hasta 100 personas: $2.300.000 (Dos opciones de menú)";
			FinSi
		FinSi
		Si cant>100 y cant<=200 Entonces
			Si menu==1 Entonces
				total<-total+3500000;
				text1<-"Hasta 200 personas: $3.500.000 (Una opción de menú)";
			SiNo
				total<-total+4000000;
				text1<-"Hasta 200 personas: $4.000.000 (Dos opciones de menú)";
			FinSi
		FinSi
		Si postre==1 Entonces
			total<-total+500000;
			text2<-"Buffet de postres: $500.000";
		SiNo
			text2<-" ";
		FinSi
		//Boleta
		Escribir "Eventos Food And Dance";
		Escribir text1;
		Escribir text2;
		Escribir "************************";
		Escribir "Total del presupuesto $", total;
		Escribir "Gracias por preferirnos.";
		Escribir "************************";
		Escribir "¿Desea otra cotización? Sí (1) No (0)";
		Leer resp1;
	Hasta Que resp1==0
FinProceso
