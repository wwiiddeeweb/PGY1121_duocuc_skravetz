# programa q consulte la edad de la persona e indique si es mayor de edad

edadPersona = int(input("Ingrese su edad: "))

if edadPersona > 18:
  print("la persona es mayor de edad")
elif edadPersona == 18:
  print("la persona tiene justo 18 años")
else:
  print("la persona es menor de edad")