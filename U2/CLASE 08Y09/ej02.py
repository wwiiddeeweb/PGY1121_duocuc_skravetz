# escribir un programa en el que se pregunte al usuario por su nombre completo y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase, utilice ciclos. (ej, juan perez gonzález, la letra "a" aparece 2 veces

nombre = input("Ingrese su nombre completo: ")
while nombre.isdigit() == True:
  print("Nombre inválido")
  nombre = input("Ingrese su nombre completo: ")
else:
  letraBuscar = input("Ingrese la letra a buscar: ")
  contLetra = 0

  for letra in nombre:
    if(letra == letraBuscar):
      contLetra += 1
    else:
      contLetra

  print("La letra '", letraBuscar, "' está presente: ", contLetra, " veces." )
