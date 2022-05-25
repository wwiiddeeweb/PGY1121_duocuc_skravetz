# cree 2 listas, en las cuales se guardarán 3 nombres y 3 apellidos (1 lista para nombres y una lista para apellidos), el sistema deberá mostrar de forma ordenada los nombres y apellidos.

listaNombres = []
listaApellidos = []

for i in range(3):
  name = input("ingrese nombre: ")
  listaNombres.append(name)
  last_name = input("ingrese apellido: ")
  listaApellidos.append(last_name)


for i in range(len(listaNombres)):
  print(listaNombres[i], listaApellidos[i])
