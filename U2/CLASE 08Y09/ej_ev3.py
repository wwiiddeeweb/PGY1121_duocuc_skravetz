## variables
flag = True
i = 0
contMCompleta = 0
contMSimple = 0
contCAceite = 0
sumaMCompleta = 0
sumaMSimple = 0
sumaCAceite = 0
valorMCompleta = 100500
valorMSimple = 89000
valorCAceite = 16000

## input
print("-"*30)
print("1. Mantención Completa: $", valorMCompleta)
print("2. Mantención Simple: $", valorMSimple)
print("3. Cambio Aceite: $", valorCAceite)
print("-"*30)
cantCli = int(input("Ingrese cantidad de clientes: "))

while flag:
  if cantCli > 0:
    flag = False
    try:
      while i < cantCli:
        i += 1
        print("Vehículo: ", (i))
        opServicio = int(input("Ingrese qué servicio desea: (1, 2 ó 3)"))
        if opServicio >= 1 and opServicio <= 3:
          if opServicio == 1:
            contMCompleta += 1
            sumaMCompleta += valorMCompleta
          elif opServicio == 2:
            contMSimple += 1
            sumaMSimple += valorMSimple
          elif opServicio == 3:
            contCAceite += 1
            sumaCAceite += valorCAceite    
          else:
            print("Opción fuera de rango:")
          
        # final output msg
        print("   Mantención   ")
        print("-"*20)
        if(contMCompleta > 0):
          print(contMCompleta, " | Mantención Completa: $", sumaMCompleta)
        if(contMSimple > 0):
          print(contMSimple, " | Mantención Completa: $", sumaMSimple)
        if(contCAceite > 0):
          print(contCAceite, " | Mantención Completa: $", sumaCAceite)
        print("Total a pagar: $", sumaMCompleta+sumaMSimple+sumaCAceite)
    
  except:
  

    


