import random
number = random.randint(0, 10)
guess = int(None)
attempts = 3

def AttemptsWarns(attempts):
    if attempts == 2:
        print ("\nTwo attempts left!")

    elif attempts == 1:
        print("\nLast attempt!!")



print ("Guess a number between 0 and 10, you have 3 attempts")

#print (number)

while guess != number and attempts != 0:
    guess = int(input("\nEnter your guess here: "))

    if guess < number:
        print("Your guess is too low")
        attempts -= 1
        AttemptsWarns(attempts)

    elif guess > number:
        print("Your guess is too high")
        attempts -= 1
        AttemptsWarns(attempts)

    elif guess == number:
        print ("\nYou got it!")
        break

if guess != number and attempts == 0:
    print (f'''\nYou have failed
    The number was {number}''')