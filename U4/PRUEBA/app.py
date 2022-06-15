# PRUEBA PARCIAL 3. PGY1121. DUOCUC. PROF HERNÁN SAAVEDRA
# PRUEBA POR SEBASTIÁN LEIVA ARIAS. 

import numpy as np
import functions as fn

'''
●	Grabar. Corresponde a guardar ciertos datos de una persona, entre ellos: NIF, nombre y edad.
Debe verificar que el NIF sea correcto, que el nombre tenga mínimo 8 caracteres y que la edad sea mayor igual a 0. 

●	Buscar: Corresponde buscar a una persona por su NIF y mostrar toda su información almacenada. 
Además, debe mostrar si la persona pertenece o no a la Unión Europea. 

●	Imprimir certificados: Esta opción permite imprimir los certificados de nacimiento, estado conyugal, pertenencia a la Unión Europea. Estos deben ser previamente ingresados con valores aleatorios desde el teclado. Al imprimir el certificado, debe mostrar el nombre del certificado, el NIF respectivo y nombre de la persona con sus datos. 

●	Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere, además, su nombre y apellido y la versión del programa.
'''

initFlag = True
userData = ""

while initFlag:
  try:
    #
    print("""
          REGISTRO DE CIUDADANOS DE LA U.E. EN ESPAÑA | ANDALUCÍA
          -------------------------------------------------------
          Opciones del sistema:
          (1) Grabar Registro
          (2) Buscar Registro
          (3) Imprimir Certificado
          (4) Salir del Programa
          """)
    opSelect = int(input("Ingrese el número de la opción deseada: "))
    
    if opSelect == 1:
      try:
        userNif = input("Ingrese su número de NIF: (formato 12345678-ABC) ")
        validatedNif = fn.validateNif(userNif)
        userName = input("Ingrese su nombre completo: ")
        validatedName = fn.validateName(userName)
        userAge = int(input("Ingrese su edad -en números-: "))
        validatedAge = fn.validateAge(userAge)

        fn.newUser(validatedNif, validatedName, validatedAge)
        
      except:
        print("error ingresando datos")
        continue
    elif opSelect == 2:
      try:
        userNif = input("Ingrese NIF del usuario a buscar: ")
        fn.getUser(userNif)
      except:
        print("Error en los datos ingresados, intente nuevamente")
      
    elif opSelect == 3:
      print("""
            
            
            IMPRIMIR CERTIFICADOS:
            -----------------------
            (1) Certificado de Nacimiento
            (2) Estado Conyugal
            (3) Pertenencia a la UE
            
            """)
      try:
        opCert = int(input("Ingrese la opción que desea imprimir: "))
        if opCert == 1:
          print("""
                
                CERTIFICADO DE NACIMIENTO
                --------------------------
                
                Lugar de nacimiento: Andalucía
                
                
                
                """)
        elif opCert == 2:
          print("""
                
                CERTIFICADO DE ESTADO CONYUGAL
                -------------------------------
                
                Lugar de nacimiento: Andalucía
                
                
                
                """)
        elif opCert == 3:
          print("""
                
                CERTIFICADO DE PERTENENCIA A LA UNIÓN EUROPEA
                ----------------------------------------------
                
                Lugar de nacimiento: Andalucía
                
                
                
                """)
        else:
          print("Opción no existe, intente nuevamente")
          continue
      except:
        print("Dato de entrada erróneo.")
      
    elif opSelect == 4:
      print("""
            
            ¡Hasta Pronto! Que tenga un buen día
            
            Programa creado por Sebastián Leiva Arias
            en Duoc UC. 2022.
            
            Versión 1.0.0 (alpha)
            
            """)
      initFlag = False
      break
    else:
      print("La opción Ingresada es incorrecta, intente nuevamente")
      continue
    
  except:
    print("Ha ocurrido un error")
    continue