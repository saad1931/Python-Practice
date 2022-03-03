print("Faulty Calculator")
print("--------------------------")
print("Enter + for Addition")
print("Enter - for Subtraction")
print("Enter * for Multiplication")
print("Enter / for Division")

op=input("Enter choice here:")
print()
n1=int(input("Enter First number:"))
n2=int(input("Enter Second number:"))

if op=="+":
    if (n1==56 and n2==9):
        print("Answer of",n1,"+",n2,"is: 77")
    else:
        add=n1+n2
        print("Answer of",n1,"+",n2,"is:",add)
elif op=="-":
    sub = n1 - n2
    print("Answer of", n1, "-", n2, "is:", sub)
elif op == "*":
    if (n1 == 45 and n2 == 3):
        print("Answer of", n1, "*", n2, "is: 555")
    else:
        mul = n1 * n2
        print("Answer of", n1, "*", n2, "is:", mul)
elif op == "/":
    if (n1 == 56 and n2 == 6):
        print("Answer of", n1, "/", n2, "is: 4")
    else:
        div = n1 / n2
        print("Answer of", n1, "/", n2, "is:", div)
else:
    print("You entered wrong operator!")

