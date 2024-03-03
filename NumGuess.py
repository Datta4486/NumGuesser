import random as rand
print("Welcome to my probably first game without using any tutorials. It's really simple - A number is randomly generated between 1 - 100 and you must guess it. Guess first try and you get a reward.")
print("Would you like to play a game? \nIf so, type Yes and if not press No")
endgame = 0
tries = 0
finish = 0
# Typo Checking
while True:
    # Input to play or nah
    choice = str(input().lower())
    if choice in ["yes","no"]:
        break
    else:
        print("Invalid Choice, type either Yes or No.")
# Actual Game
if choice.lower() == "yes":
    while endgame != 1:
        print("The game has started, guess the number between 1-100")
        finish = 0
        tries = 0
        # Number Choosing
        answer = rand.randrange(1,101,1)
        # while function to do a loop
        while finish != 1:
            while True:
                try: 
                    useranswer = int(input("Enter ur guess:"))
                    break
                except ValueError:
                    print("Invalid input. Make sure that it is an integer.")
            #If answer is false
            if useranswer != answer:
                if useranswer > answer:
                    print("Wrong Guess, the number is lower than ur given number")
                    tries+=1
                else:
                    print("Wrong Guess, the number is higher than ur given number ")
                    tries+=1
            else:
                if tries == 0:
                    print("Wow, first try! \n Well your reward is that you can get a 500 rupee Amazon GC. Just ask my mother.")
                else:
                    print("Guessed correct. It took you",tries+1,"tries to guess it")
                print("Would you like to play again? Type Yes or NO")
                while True:
                    replay = str(input().lower())
                    if replay in ["yes","no"]:
                        break
                    else:
                        print("Invalid input. Type either yes or no")
                if replay.lower() == "no":
                    endgame = finish = 1
                    print("Thanks for playing!")
                elif replay.lower() == "yes":
                    finish = 1
elif choice.lower() == "no":
    print("Why even bother running this program?")




