''' En un delivery se venden 4 tipos de pan: 
Amasado $1.500 
Molde $1.000 
Baguette $2.000 
Integral $3.000 

Determine el total a pagar por un cliente que puede llevar varios tipos de pan. 
Considere que si el total de la venta es superior a $5000 el envío es gratis, 
sino se cobra el 10% adicional. 
 '''
amasado = 1500
molde = 1000
baguette = 2000
integral = 3000
opcion = 1

while opcion == 1:
  print("PANADERÍA")
  print(f"Lista de precios\n Amasado(1): $ {amasado}\n Molde(2) $ {molde}\n Baguette(3): $ {baguette} \n Integral(4) $ {integral}")

  nroPanes = 0
  i = 1
  total = 0
  nroPanes = int(input("Cuántos panes desea comprar?"))

  if nroPanes > 0:
    while i <= nroPanes:
      opcion = int(input(f"Ingrese opción de pan {i}: "))
      i = i+1
      if opcion == 1:
        total = total + amasado 
      elif opcion == 2:
        total = total + molde
      elif opcion == 3:
        total = total + baguette
      elif opcion == 4:
        total = total + integral
      else:
        print("opción no válida")

  if total > 5000:
    print("\n")
    print("-------------------------------")
    print("total a pagar:", total)
    print("envío: $0")
  else:
    total = total + (total*0.10)
    print("\n")
    print("-------------------------------")
    print("envío: $",(total*0.10))
    print("total a pagar:", total)
    
    print("\n-------------------------------")
    opcion = int(input("desea realizar otra compra? (1) sí, (2) no "))

