def validarRut (rut):
  if(rut > 555 and rut < 999):
    return True
  else:
    return False
    
def bienvenidaUsuario (validacionRut):
  if validacionRut:
    print("bienvenido usuario! ")
  else: 
    print("adiós usuario!")
    

rutUsuario = int(input("ingrese su rut: "))

bienvenidaUsuario(validarRut(rutUsuario))





