

''' # start, end, step
try:
  x = int(input("ingrese nro: "))
  for num in range(1, x, 2):
    
except:
  pass
  print("errorsito") 
 '''
 


''' exito = True

for num in range(3):
  print("sucedió!")
  if exito:
    print("cualquier éxito!")
    break
else:
  print("se completó el for sin entrar al if")
    
 '''
 
 

evenCount = 0
 
for num in range(1,10):
  if num % 2 == 0:
    evenCount += 1
    print(num)

print("números pares: ", evenCount)