emailPaciente = input("Ingrese Correo Electrónico del paciente -> ejemplo@email.com: ")

while not "@" in emailPaciente:
  print("no tiene arroba")
  emailPaciente = input("Ingrese Correo Electrónico del paciente -> ejemplo@email.com: ")
  
print("tiene arroba")

