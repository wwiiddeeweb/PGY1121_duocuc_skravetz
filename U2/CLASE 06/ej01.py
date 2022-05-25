# ejercicio menú

sw = 1

while sw == 1:
  print("1. opción 1")
  print("2. opción 2")
  print("3. opción 3")
  
  try:
    opcion = int(input("ingrese opción: "))
    if (opcion > 0 and opcion < 4):
      if opcion == 1:
        print("ha seleccionado la opción 1!")
        print("adiós :)")
        sw = 0      
      if opcion == 2:
        print("ha seleccionado la opción 2!")
        print("adiós :)")
        sw = 0
      if opcion == 3:
        print("ha seleccionado la opción 3!")
        print("adiós :)")
        sw = 0
    else:
      print("número fuera de rango")
      sw = 0
  except:
    print("opción errónea, adiós!")
