n=33
guess=0
while(guess<10):
    guess=guess+1
    inp=int(input("Enter a number:"))

    if inp==n:
        print("WellDone Your Answer is correct!")
        print("You took",guess,"chances to get this answer.")
        break
    elif inp>n:
        print("Sorry you entered greater number than desired result")
        print("Number of guesses left:",(10-guess))
    elif inp < n:
        print("Sorry you entered lesser number than desired result")
        print("Number of guesses left:", (10-guess))
    if guess==10:
        print("Game Over!")