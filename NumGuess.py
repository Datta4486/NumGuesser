import random as rand
print("Welcome to my probably first game without using any tutorials. It's really simple - A number is randomly generated between 1 - 100 and you must guess it. Guess first try and you get a reward.")
print("Would you like to play a game? \nIf so, type Yes and if not press No")
endgame = 0
tries = 0
finish = 0
choice = str(input())
# Input to play or nah
if choice == "Yes" or choice == "YES":
    while endgame != 1:
        print("The game has started, guess the number between 1-100")
        finish = 0
        tries = 0
        # Number Choosing
        answer = rand.randrange(1,101,1)
        # while function to do a loop
        while finish != 1:
            print(answer)
            # User answer
            useranswer = int(input("Enter ur guess:"))
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
                replay = str(input())
                if replay == "NO" or replay == "NO":
                    endgame = finish = 1
                    print("Thanks for playing!")
                elif replay == "YES" or replay == "Yes":
                    finish = 1
elif choice == "No" or choice == "NO":
    print("Why even bother running this program?")




