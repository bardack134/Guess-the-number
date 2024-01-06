# Importamos el logo desde el módulo externo (Logo.py)
from Logo import *

# Importamos la función randint del módulo random para generar un número aleatorio
from random import randint

# Imprimimos el logo al inicio del juego
print(logo)
print()

# Mensaje de bienvenida al juego
print("WELCOME TO THE NUMBER GUESSING GAME")
print()
print("I am thinking of a number between 1 and 100")

# VARIABLES GLOBALES
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Generamos un número aleatorio entre 1 y 100
answer = randint(1, 100)

# Función para verificar la respuesta del jugador
def check_answer(guess, answer, turns):
    """Compara la respuesta con la suposición. Devuelve el número de intentos restantes."""
    if guess > answer:
        print(too_high)  # Si la suposición es demasiado alta
        print()      
        return turns - 1
    elif guess < answer:
        print(too_low)  # Si la suposición es demasiado baja
        print()
        return turns - 1
    else:
        print(you_got_it)  # Si la suposición es correcta
        print() 
        print(f"You got it! The correct answer was {answer}")

# Función para establecer la dificultad del juego (número de intentos)
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # Si el nivel es fácil, devuelve los intentos para nivel fácil; de lo contrario, devuelve los intentos para nivel difícil
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Función principal del juego
def game():
    turns = set_difficulty()  # Establece la dificultad del juego
    print()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses, you lose.")
            return

        

# Llamamos a la función del juego
game()
