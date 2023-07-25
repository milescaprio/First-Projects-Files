import random
computerguesses = random.randint(1,10)
play = input("play? y/n") #Ask if wanna play
while play == 'y': #Check if wanna play
    computerguesses = random.randint(1,10)
    guess = input("Try to guess the number between 1 and 10.")
    if computerguesses == eval(guess):
        print("youWIN!")
    else:
        print("you lose:(") #Check Number
    print("the number was")
    print(computerguesses) #hindsight
    play = input("play again? y/n")
    if play == 'n':
        print("good game(s)")
