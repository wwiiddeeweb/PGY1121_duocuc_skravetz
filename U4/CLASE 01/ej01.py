import numpy as np

arreglo = np.array([1,3,4,5,45,62])

# mostrar número de dimensiones
print(arreglo.ndim)

# mostrar largo del arreglo
print(len(arreglo))

# en qué eje están? (x,y,z)
print(arreglo.shape)

# selecciona una porción del arreglo. siempre muestra desde x hasta el y-1 -> [x:y] 
print(arreglo[1:4])

# elementos entre el intervalo del arreglo
# se puede definir un número de _saltos_ sobre los cuales recorrer el array
## pd: valor negativo parte el array al revés
print(arreglo[::-2])

# ej: avanzar desde el index(2) hasta el final, de 1 en 1 valor
print(arreglo[2::1])

