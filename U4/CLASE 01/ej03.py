# arreglos bidimensionales
''' 
1. Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
con elementos aleatorios de números enteros del 0 al 100. 
'''

import numpy as np
from numpy import random as rd

matrix = np.zeros((3,3))


for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    matrix[i][j] = rd.randint(0,100)

print(matrix)

# promedio

print("promedio: ", matrix.mean())

# sumar elementos
print("suma: ", matrix.sum())

# elemento mayor
print("mayor: ", matrix.max())

# elemento menor
print("menor: ", matrix.min())

# sólo elementos de la diagonal

