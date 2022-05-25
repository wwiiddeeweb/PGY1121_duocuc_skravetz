# PRUEBA CENTRO MÉDICO DUOC
# POR SEBASTIÁN LEIVA ARIAS

# flag inicializador
initFlag = True

# registros

registros = ""


# init loop
while initFlag:
  # menú de opciones
  print("-"*30)
  print("Centro Médico DUOC")
  print("-"*30)
  print("1.	Registrar Paciente")
  print("2.	Atención Paciente")
  print("3.	Consultar Datos Paciente")
  print("4.	Salir")
  print("-"*30)

  # try-except inside init loop
  try:
    # option selection input
    opSelect = int(input("Ingrese opción a ejecutar: "))
    
    # validar rango de opciones
    while opSelect < 1 or opSelect > 4:
      print("Opción Incorrecta! Intente Nuevamente")
      opSelect = int(input("Ingrese opción a ejecutar: "))
      
    # registro paciente
    
    if opSelect == 1:
      print("*" * 30)
      print("Registro de Nuevo Paciente")
      print("*" * 30)
      rutPaciente = int(input("Ingrese RUT del paciente (sin puntos ni dígito verificador): "))
      while rutPaciente < 5000000 or rutPaciente > 99999999:
        print("Error: RUT Inválido")
        rutPaciente = int(input("Ingrese RUT del paciente (sin puntos ni dígito verificador): "))
      
      nombrePaciente = input("Ingrese Nombre y Apellido del paciente: ")
      direccionPaciente = input("Ingrese Dirección del Domicilio del paciente: ")
      
      edadPaciente = int(input("Ingrese la Edad del paciente: "))
      while edadPaciente < 0 or edadPaciente > 110:
        print("Error: Edad Fuera de Rango")
        edadPaciente = int(input("Ingrese la Edad del paciente: "))
      
      sexoPaciente = input("Ingrese Sexo del paciente: (F) Femenino ó (M) Masculino: ").lower()
      while not (sexoPaciente == "f" or sexoPaciente == "m"):
        print("Error: Sexo Inválido")
        sexoPaciente = input("Ingrese Sexo del paciente -> (F) Femenino ó (M) Masculino: ").lower()
      
      prevPaciente = input("Ingrese Previsión del paciente -> (ISAPRE) ó (FONASA): ").lower()
      while not (prevPaciente == "isapre" or prevPaciente == "fonasa"):
        print("Error: Previsión inválida")
        prevPaciente = input("Ingrese Previsión del paciente -> (ISAPRE) ó (FONASA): ").lower()
      
      emailPaciente = input("Ingrese Correo Electrónico del paciente -> ejemplo@email.com: ").lower()
      while not "@" in emailPaciente:
        print("Error: Formato de correo electrónico inválido")
        emailPaciente = input("Ingrese Correo Electrónico del paciente -> ejemplo@email.com: ")
      
      print(" ")
      print("*" * 30)
      print(f"Paciente de nombre {nombrePaciente} con RUT {rutPaciente} ingresado correctamente!")
      print("*" * 30)
      print(" ")

      
    # nueva atención paciente
    if opSelect == 2:
      rutAtencion = int(input("Ingresr RUT del paciente para realizar atención: "))
      while rutAtencion < 5000000 or rutAtencion > 99999999:
        print("Error: RUT Inválido")
        rutAtencion = int(input("Ingresr RUT del paciente para realizar atención: "))
      
      if (rutAtencion == rutPaciente):
        print(f"Paciente encontrado -> Nombre: {nombrePaciente} | RUT: {rutPaciente}")
        fecha = input("Ingrese la fecha de la atención: ")
        obs = input("Ingrese las observaciones de la visita: ")
        newRegistro = ("-" * 30) + "\n" + "Fecha Atención:\t" + fecha + "\n" + "Observación:\t" + obs + "\n" + ("-" * 30) + "\n"
        registros += newRegistro
        print("-" * 30)
        print("¡Registro realizado con éxito!")
        print("-" * 30)
        
      else:
        print("Paciente no existe en nuestros registros")
    
    # consultar datos del paciente
    if opSelect == 3:
      rutConsultar = int(input("Ingrese el RUT del paciente a consultar (sin puntos ni dígito verificador): "))
      while rutConsultar < 5000000 or rutConsultar > 99999999:
        print("Error: RUT Inválido")
        rutConsultar = int(input("Ingrese el RUT del paciente a consultar (sin puntos ni dígito verificador): "))
      
      if rutConsultar == rutPaciente: 
        print("-"*30)
        print("Datos del paciente\n")
        print("Rut del Paciente:\t", rutPaciente)
        print("Nombre del Paciente:\t",nombrePaciente)
        print("Dirección del Paciente:\t", direccionPaciente)
        print("Edad del Paciente:\t", edadPaciente)
        print("Sexo del Paciente:\t", sexoPaciente)
        print("Previsión del Paciente:\t", prevPaciente)
        print("E-Mail del Paciente:\t", emailPaciente)
        print("Registros del paciente:\n", registros)
        print("-"*30)
      else:
        print("Paciente no existe en nuestros registros")
    
    # exit
    if opSelect == 4:
      print("adios!")
      initFlag = False
      break
    
  # except inside init loop
  except:
    print("")
    print("*" * 30)
    print("¡Dato no válido! Intente nuevamente")
    print("*" * 30)
    print("")
    pass
  

