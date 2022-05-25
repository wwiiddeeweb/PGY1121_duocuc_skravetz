# sistema de validación de user y pass de empleado para login

user1 = "pedro"
user1pass = "1234"
user2 = "angel"
user2pass = "a4s1"

userInput = input("ingrese nombre usuario: ")
passInput = input("ingrese contraseña: ")

if userInput == user1 and passInput == user1pass:
  print(f"bienvenido {user1}")
elif userInput == user2 and passInput == user2pass:
  print(f"bienvenido {user2}")
else:
  print("credenciales inválidas")