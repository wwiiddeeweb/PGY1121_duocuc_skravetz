# ingresar 3 notas (entre 1 y 7) y calcular promedio. si la nota es igual o mayor a 4, indicar si está aprobado o en caso contrario estará reprobado

nota1 = int(input("ingrese nota #1: "))
nota2 = int(input("ingrese nota #2: "))
nota3 = int(input("ingrese nota #3: "))

prom = ((nota1+nota2+nota3)/3)

if prom >= 4:
  print(f"alumno aprobado! promedio: {prom:.2f}")
else:
  print(f"alumno reprobado, promedio: {prom:.2f}")