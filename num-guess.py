from random import randint

secret_number = randint(1, 10) # You can choose whatever the range is.
guess_count = 0
guess_limit = 4                # Set the limit as you prefer! (CAUTION: Don't set the limit below 3)
while guess_count<guess_limit:
    player_guess = int(input("Guess a number between 1 and 10: "))
    if player_guess == secret_number:
        print("Congratulation. You won!")
        break
    if player_guess != secret_number:
        print("Oops. Wrong one!")
    if guess_count == guess_limit-3:
        print(f"HINT: Sum of the secret number and 10 is {secret_number+10}. The product of them is {secret_number*10}")
    if guess_count == guess_limit-1:
        print("Game over! You lost!")
    guess_count += 1
