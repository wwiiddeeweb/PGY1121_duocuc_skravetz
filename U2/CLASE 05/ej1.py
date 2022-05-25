
x = range(1,6,1)
y = 0
contadorMayorCero = 0
contadorMenorCero = 0
contaddorIgualCero = 0

for i in x:
  y = int(input("ingrese número: "))
  if y > 0:
    contadorMayorCero = contadorMayorCero +1
  elif y < 0:
    contadorMenorCero = contadorMenorCero +1
  else:
    contaddorIgualCero = contaddorIgualCero +1

print("mayores a cero: ", contadorMayorCero)
print("menores a cero: ", contadorMenorCero)
print("iguales a cero: ", contaddorIgualCero)