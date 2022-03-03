try:
    player=int(1)
    print("Enter ICC ODI player of the year 2021 FROM the choices below:\n 1-Babar    2-Smith      3-Williamson     4-Root")
    n1=int(input())
    if n1==player:
        print("Correct",player,"is right answer!")
    else:
        print("Incorrect answer, Correct answer is ",player)
except Exception as e:
    print(e)
print("------------------------------")
print("Thanks for your participation!")
