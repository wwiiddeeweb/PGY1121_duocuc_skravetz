''' 
1. Crear un arreglo unidimensional de tamaño 10, con elementos aleatorios de números enteros del 0 al 100, para ello deberá investigar la función que permita crear números aleatorios.

2. Crear una copia del arreglo y muestre:
Elemento mayor
Elemento menor
Suma de los elementos
Promedio de los elementos
Mostrar todos los elementos

'''

import random as rnd
import numpy as np
import math

arr = np.array([], dtype=int)
for i in range(10):
  arr = np.append(arr, math.floor(rnd.randint(0,100)))

# mostrar arreglo generado
print("array: ", arr)

# valor mínimo
print("min: ", arr.min())

# valor máximo
print("max: ", arr.max())

# suma de los elementos
suma = arr.sum()
print("suma: ", suma)

# promedio de los elementos
prom = arr.mean()
print("promedio: ", prom)
