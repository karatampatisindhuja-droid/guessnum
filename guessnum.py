import random

# Generate a random number between 1 and 200
secret_number = random.randint(1, 200)

print("🎯 Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 200.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the correct number!")
        break