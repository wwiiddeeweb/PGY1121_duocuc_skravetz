
x = range(1,11,1)
y = ""

contVocales = 0;
contConsonantes = 0;
for i in x:
  y = input(f"ingrese carácter {i}: ")
  while y == "":
    y = str(input("carácter erróneo! ingrese carácter: "))
  if y in "aeiou":
    contVocales += 1
  else:
    contConsonantes += 1

print("cantidad de vocales: ", contVocales)
print("cantidad de consonantes: ", contConsonantes)