### JUEGO DE PIEDRA, PAPEL O TIJERAS 
### La computadora no tiene una opcion predeterminada

import random
options = ("piedra", "papel", "tijeras")

print("Bienvenid@ al juego! Nos alegra tenerte!")
computer_wins = 0
user_wins = 0
rounds = 1
while True:

  print("*" * 45)
  print("Round:", rounds)
  print("*" * 45)

  print("Computer wins =>", computer_wins)
  print("User wins =>", user_wins)
  computer_option = (random.choice(options))

  user_option = input("Elige ¿piedra, papel o tijeras?")
  user_option = user_option.lower()

  if not user_option in options:
    print("Esa opcion no es valida.")
    continue 

  rounds += 1
  print("User_option =>", user_option)
  print("Computer_option =>", computer_option)

  if user_option == computer_option:
      print("Empate!")
  if user_option == "piedra" and computer_option == "tijeras":
      print("Ganaste!")
      user_wins += 1
  if user_option == "papel" and computer_option == "tijeras":
     print("Perdiste!")
     computer_wins += 1
  if user_option == "piedra" and computer_option == "papel":
      print("Perdiste!")
      computer_wins += 1
  if user_option == "papel" and computer_option == "piedra":
    print("Ganaste!")
    user_wins += 1
  if user_option == "tijeras" and computer_option == "piedra":
      print("Perdiste!")
      computer_wins += 1
  if user_option == "tijeras" and computer_option == "papel":
    print("Ganaste!")
    user_wins += 1

  if computer_wins == 3:
    print("Has sido vencido")
    break
  if user_wins == 3:
    print("Absoluto ganador!!!")
    break



### JUEGO DE PIEDRA, PAPEL O TIJERAS 
### La computadora no tiene una opcion predeterminada
