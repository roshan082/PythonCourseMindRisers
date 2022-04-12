
import random

    

def randomNumber():
    guess_number = input("Enter a number : ")
    numbers = random.randint(1, 10)
    print(f"You Guessed : {guess_number}")
    print("Random Numbers : ", numbers)
    checkNumber(guess_number, numbers)
    input("Enter If you want to Play Again...")
    randomNumber()

def checkNumber(input_number, random_number):
    if int(input_number) == int(random_number):
        print("")
        print("Hurray!!! You Guessed the correct number..")
        print("")
    else:
        print("")
        print("Sorry!! Try Again")
        randomNumber()
print("")
randomNumber()

