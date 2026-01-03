import random

print("========================================")
print("Hi! Welcome to the Number Guessing Game")
print("========================================")

low= int(input("Enter The Lower Bond: "))
high= int(input("Enter The Higher Bond: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's Starts!")

num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input('Enter Your Guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break
    elif guess > num:
        print('To High. Try a lower Number.')
    elif guess < num:
        print('To Low. Try a higher Number.')
    else:
        print(f'Sorry! The number was {num}. Better luck Next time. ')
