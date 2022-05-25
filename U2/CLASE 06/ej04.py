# ticketera compra boletos estadio
## menores 4000 ( > 7  y < 12)
## adulto 7000 (12 - 65)
## a.mayor 3000 (> 65 años)

## debe determinar el total a pagar por un grupo de personas que lleguen juntas considerando sus edades

## debe entregar el total de personas q ingresan al estadio y el total de ventas del día
## validar q las cantidades no sean fuera del rango 

# init
init = 1

# counters
contMenores = 0
contAdultos = 0
contAmayores = 0


# tickets
valorTicket = 0
totalTickets = 0

# main loop
while init == 1:
  try:
    print("TICKETERA ESTADIO")
    print("-----------------")
   
    print("Seleccione acción a ejecutar: ")
    print("(1). Ingresar Compra")
    print("(2). Salir")
    opcion = int(input())
    
    if (opcion >= 1 and opcion <= 2):
      if(opcion == 1):
        print("Valores de ticket: ")
        print("(1). Menores: $4000")
        print("(2). Adultos: $7000")
        print("(3). Adultos Mayores: $3000")
        print("-----------------")
        compra = int(input("Ingrese opción: "))
        if (compra >= 1 and compra <= 3):
              if(compra == 1):
                valorTicket = 4000
                contMenores = contMenores + 1
                totalTickets = totalTickets + valorTicket
                print("Se ha vendido un ticket de: Menor")

              if(compra == 2):
                valorTicket = 7000q
                contAdultos = contAdultos + 1
                totalTickets = totalTickets + valorTicket
                print("Se ha vendido un ticket de: Adulto")
          
              if(compra == 3):
                valorTicket = 3000
                contAmayores = contAmayores + 1
                totalTickets = totalTickets + valorTicket
                print("Se ha vendido un ticket de: Adulto Mayor")

        else:
              print("opción errónea")  
      if(opcion == 2):
        print("REPORTE DEL DÍA: ")
        print("Menores: ", contMenores)
        print("Adultos: ", contAdultos)
        print("Adultos Mayores:  ", contAmayores)
        print("Total personas registradas: ", contMenores+contAdultos+contAmayores)
        print("Total ventas: ", totalTickets)
        init = 0

  except:
    print("valor erróneo, intente nuevamente:")
  



