Proceso food_and_dance
	//Definiciones
	Definir resp1, cant, menu, postre, total Como Entero;
	Definir text1, text2 Como Caracter;
	Escribir "Bienvenido a Food and Dance";
	Repetir
		//Inicializaciones
		total<-0;
		//Ingreso datos 
		Escribir "�Para qu� cantidad de personas es el evento? (l�mite 200 personas)";
		Leer cant;
		Escribir "�Qu� opci�n de men� desea? Con una opci�n (1) o con dos opciones (2)";
		Leer menu;
		Escribir "�Desea postre? S� (1) No (0)";
		Leer postre;
		//Proceso 
		Si cant<=50 Entonces
			si menu==1 Entonces
				total<-total+1000000;
				text1<-"Hasta 50 personas: $1.000.000 (Una opci�n de men�)";
			SiNo
				total<-total+1500000;
				text1<-"Hasta 50 personas: $1.500.000 (Dos opciones de men�)";
			FinSi
		FinSi
		Si cant>50 y cant<=100 Entonces
			Si menu==1 Entonces
				total<-total+1800000;
				text1<-"Hasta 100 personas: $1.800.000 (Una opci�n de men�)";
			SiNo
				total<-total+2300000;
				text1<-"Hasta 100 personas: $2.300.000 (Dos opciones de men�)";
			FinSi
		FinSi
		Si cant>100 y cant<=200 Entonces
			Si menu==1 Entonces
				total<-total+3500000;
				text1<-"Hasta 200 personas: $3.500.000 (Una opci�n de men�)";
			SiNo
				total<-total+4000000;
				text1<-"Hasta 200 personas: $4.000.000 (Dos opciones de men�)";
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
		Escribir "�Desea otra cotizaci�n? S� (1) No (0)";
		Leer resp1;
	Hasta Que resp1==0
FinProceso
