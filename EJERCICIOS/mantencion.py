'''
valores: 
Cliente	Valor
Mant. Completa	$100.500
Mant. Simple	$89.000
C. de Aceite	$16.000

'''

# inicializadores
initFlag = True
totalServicio = 0

# precios
precioMantCompleta = 100500
precioMantSimple = 89000
precioCambAceite = 16000

# contadores
contMantCompleta = 0
contMantSimple = 0
contCambAceite = 0


try:
  # ciclo inicializador
  while (initFlag == True):
    try:
      print("-" * 25)
      print("INICIO: Mantención Automotriz")
      print("-" * 25)
      
      # pregunta cantidad de autos
      try:
        cantidadAutos = int(input("Ingrese cantidad de autos: "))
      except:
        print("error! ingrese un número")
        cantidadAutos = int(input("Ingrese cantidad de autos: "))

      # ciclo por cada auto
      for i in range(cantidadAutos):
        print("-" * 25)
        print("Seleccione servicio: ")
        print("-" * 25)
        print("1. Mant. Completa	$100.500 ")
        print("2. Mant. Simple	$89.000")
        print("3. C. de Aceite	$16.000")
        print("-" * 25)
        opSeleccionada = int(input("Ingrese qué servicio necesita: "))
        
        # condicional de opciones de servicio
        if (opSeleccionada == 1):
          contMantCompleta += 1
          totalServicio += precioMantCompleta
        elif (opSeleccionada == 2):
          contMantSimple += 1
          totalServicio += precioMantSimple
        elif (opSeleccionada == 3):
          contCambAceite += 1
          totalServicio += precioCambAceite
        else:
          print("opción no válida")
        
      initFlag = False
    except:
      print("Error! Regresando al menú...")

  # imprimir boleta
  print("-"*25)
  print("BOLETA DE MANTENCIÓN: ")
  print(f"1. Matención Completa: {contMantCompleta}")
  print(f"2. Matención Simple: {contMantSimple}")
  print(f"3. Cambio de Aceite: {contCambAceite}")
  print("-"*25)
  print(f"TOTAL: $ {totalServicio}")

except:
  print("ERROR! Datos inválidos")
  pass



