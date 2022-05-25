# indicar si un número es par o impar, gestionar excepción con try/except.

loop = 1
while loop == 1:
  try:
    x = int(input("ingrese un número: "))
    if ( x % 2 == 1):
      print("es impar")
      loop = 0
    else:
      print("es par")
      loop = 0
  except:
    print("valor erróneo, intente nuevamente")
    
    
