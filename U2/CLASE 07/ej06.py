# cree una lista para almacenar nombres, el proceso se realiza preguntando si desea seguir ingresando, si la respuesta es no , se detiene el proceso. luego, elimine el nombre con la menor cantidad de carácteres.

opcion = "si"
listaNombres = []
listaLargoNombres = []


opcion = input("desea ingresar nombres?: si ó no ")
while opcion == "si":
  name = input("ingrese un nombre: ")
  listaNombres.append(name)
  opcion = input("desea ingresar nombres?: si ó no ")


for i in listaNombres:
  length = len(i)
  listaLargoNombres.append(length)


smallerValue = min(listaLargoNombres)
smallerValueIndex = listaLargoNombres.index(smallerValue)

print(listaNombres)

listaNombres.pop(int(smallerValueIndex))
print(listaNombres)