''' Ingrese por teclado 5 números enteros positivos, súmelos y muestre el resultado de la suma.

Ingrese por teclado un número entero positivo entre 103 y 987, luego genere un proceso que permita invertir el número, aplicando las 4 operaciones matemáticas básicas (suma, resta, multiplicación y división). Finalmente, muestre el resultado.
 '''
 
 
''' num = (input("ingrese número: "))
n1 = (num[0])
n2 = (num[1])
n3 = (num[2])
while int(num) >= 103 and int(num) <= 987:
    print(f"su número es: {num}")
    print(f"número invertido es:", n3+n2+n1)
    break '''
    

num = int(input("ingrese número: "))

while num < 103 or num > 987:
  num = int(input("ingrese número: "))
else:
  dig1 = num
  dig2 = (num-(num%10))/10
  dig3 = (dig2-(dig2%10))/10*1


  result = (((dig1%10)*10)+(dig2%10))*10+(dig3%10)
  print(f"el número invertido de {num} es {result}")
