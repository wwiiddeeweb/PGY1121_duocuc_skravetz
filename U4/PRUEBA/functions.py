# FUNCIONES DE LA APLICACIÓN
# PRUEBA PARCIAL 3. RAMO PGY1121 POR SEBASTIÁN LEIVA ARIAS
import numpy as np

arrUser = np.array(["","",""], dtype=object)

def validateNif(nif):
  while len(nif) < 12 and nif[8] != "-":
    print("ERROR. Número de nif no válido, no es ciudadano de la UE")
    return nif
  else:
    return nif

def validateName(name):
  while len(name) < 8:
    print("ERROR. Nombre debe tener al menos 8 caracteres, intente nuevamente")
    name = input("Ingrese su nombre completo: ")
  else:
    return name
  
def validateAge(age):
  while age < 0:
    print("ERROR. Debe tener 0 o más años para poder ser registrado.")
    age = int(input("Ingrese su edad -en números-: "))
  else:
    return age
  

def newUser(nif, name, age):
  userData = np.array([nif, name, age], dtype=object)
  arrUser[0] = nif
  arrUser[1] = name
  arrUser[2] = age
  print(f"""
        --------------------------------
             NUEVO REGISTRO CREADO!
        --------------------------------
        
        Usuario {userData[1]} de NIF {userData[0]} registrado exitosamente!
        
        
        """)
  return userData

def getUser(nif):
  print(arrUser)
  if nif == arrUser[0]:
    print(f"""
         
          --------------------
          Usuario encontrado!
          --------------------
          NIF: {arrUser[0]}
          Nombre: {arrUser[1]}
          Edad: {arrUser[2]}
          Es de la UE?: Sí
          
          """)
  else:
    print("""
          
          Lo sentimos, usuario no existe en el registro.
          
          """)
  

def printCertificate():
  print("print")

