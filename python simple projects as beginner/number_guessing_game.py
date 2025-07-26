import random

number = random.randint(1,100)
guess = None
attemps = 0

while guess != number:
    guess = int(input("Guess the number between (1 to 100): "))
    attemps += 1

    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
print(f" Correct! You guessed it in {attemps} attempts.")