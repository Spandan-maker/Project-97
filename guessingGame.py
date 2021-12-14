import random

number = random.randint(1,9)
chances = 0

while chances < 5:
    guess = int(input("Enter a number between 1 to 9: "))

    if guess > number:
        print("A bit less")
        #guess = int(input("Enter a number between 1 to 9: "))
        chances = chances + 1

    elif guess < number:
        print("A bit high")
        #guess = int(input("Enter a number between 1 to 9: "))
        chances = chances + 1

    elif guess == number: 
        print("You guessed it right!!!")
        break
    
    if chances == 5: 
        print("You LOST!!!, The number is " + str(number))