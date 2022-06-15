import numpy as np

arrUno = np.ones(3, dtype=object)

print(arrUno)

for i in range(len(arrUno)):
  arrUno[i] = np.random.randint(1,100)
  
print(arrUno)