import random

print("Howdy, what's your name?")
name = input("Type in your name: ")

print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

number = random.randint(1, 100)
guess = ""

while True:
    guess = int(input("Your guess?"))
    if guess == number:
        guessnumber = guessnumber + 1
        print(f"Well done, {name}! You found my number in {guessnumber} tries!")
        break
    elif guess > number:
        guessnumber = guessnumber + 1
        print("Your guess is too high, try again.")
    else:
        guessnumber = guessnumber + 1
        print("Your guess is too low, try again.")

