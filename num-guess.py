from random import randint

max = 10    # You can choose whatever the range is.
min = 1
secret_number = randint(min, max)
guess_count = 0
guess_limit = 4                # Set the limit as you prefer! (CAUTION: Don't set the limit below 3)
while guess_count<guess_limit:
    player_guess = int(input(f"Guess a number between {min} and {max}: "))
    if player_guess == secret_number:
        print("Congratulation. You won!")
        break
    if player_guess != secret_number:
        print("Oops. Wrong one!")
    if guess_count == guess_limit-3:
        print(f"HINT: Sum of the secret number and {max} is {secret_number+max}. The product of them is {secret_number*max}")
    if guess_count == guess_limit-1:
        print("Game over! You lost!")
    guess_count += 1
