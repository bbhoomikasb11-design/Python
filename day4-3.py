secret_number = 7

guess = int(input("Guess the number: "))

if guess == secret_number:
    print("Congratulations! You guessed correctly.")

elif guess < secret_number:
    print("Too Low!")

else:
    print("Too High!")