# generar las primeras 10 tablas de multiplicar, cada una de 1 a 10

x = range (1, 11, 1)
for i in x:
  print("tabla del: ", i)
  for j in x:
    print(i*j)
    
