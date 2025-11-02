import random

def number_guessing_game():
    guess = random.randint(1, 50)
    while True:
        num = int(input("guess no: "))
        if guess > num:
            print("is too low")
        elif guess < num:
            print("is too high")
        else:
            print("your guess is correct")
            break
number_guessing_game()