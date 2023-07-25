import random
PLAY = input("Would you like to play?")
while PLAY == "y":
    rangex = input("What range of numbers do you want?")
    guesses=0
    number = random.randint(1,eval(rangex))
    guess = input("What is your guess?")
    if eval(guess) < number:
        print("Too low!")
    if eval(guess) > number:
        print("Too high!")
    guesses = guesses+1
    while not eval(guess) == number:
        guess = input("What is your guess?")
        if eval(guess) < number:
            print("Too low!")
        if eval(guess) > number:
            print("Too high!")
        guesses = guesses+1
    print("Good job!")
    print("It took you",guesses,"guesses")
    PLAY = input("Would you like to play again?")
print("Thanks for playing!")

