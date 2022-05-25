# ejs guía 2.2.2.

## cineduoc


if estudiante != 1 or != 2:
  print("valores incorrectos, intente nuevamente")
  estudiante = input("Pertenece a DUOC? (1) Sí, (2) No")
else:
  if estudiante == 1:
    estudiante = true
  elif estudiante == 2:
    estudiante = false
    
print(f"estudiante es: {estudiante}")