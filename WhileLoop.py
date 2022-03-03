count=1
while(count<11):
    print(count,end=" ")
    count=count+1

list1=[10,56,33]
i=0

while(True):

    print("\nEnter Player Name or Write exit :")
    player = input()
    if player=="Exit":
        break
    i=i+1
    for item in list1:

        if player == "Babar":
            print("Jesrsey number of",player,"is",list1[0])
            break
        elif player == "Shaheen":
            print("Jesrsey number of",player,"is",list1[1])
            break
        elif player == "Rizwan":
            print("Jesrsey number of",player,"is",list1[2])
            break
        else:
            print("No Player with this Name exists!")
            break

