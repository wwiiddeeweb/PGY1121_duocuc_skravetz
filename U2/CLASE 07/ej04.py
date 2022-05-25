# escriba 3 nombres y luego muestre el q tenga la mayor cantidad de carácteres

listaNombres = []
listaLargos = [] 

for i in range(3):
  name = input("Ingrese un nombre: ")
  listaNombres.append(name)

for i in listaNombres:
  length = len(i)
  listaLargos.append(length)
  
largerValue = listaLargos.index(max(listaLargos))
lenghtLargerValue = max(listaLargos)

print("El nombre más largo es: ", listaNombres[largerValue], " | (", lenghtLargerValue, " carácteres)" )