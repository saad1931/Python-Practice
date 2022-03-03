def Factorial_Iterative(n):
    """
    Function for finding Factorial using iterative method
    """
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac


def Factorial_Recursive(n):
    """
    Function for finding Factorial using recursive method
    """
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial_Recursive(n-1)


# Recursive - Calling itself
# assume we put n=5
# 5*Factorial_Recursive(4)
# 5*4*Factorial_Recursive(3)
# 5*4*3*Factorial_Recursive(2)
# 5*4*3*2*Factorial_Recursive(1)
# 5*4*3*2*1=120

def fibonacci_series(n):
    if n==1:
        return 0
    elif n==2:
        return  1
    else:
        return fibonacci_series(n-1)+fibonacci_series(n-2)



num=int(input("Enter number to find it's factorial:"))
print()
print("Factorial using iterative method of",num,"is:",Factorial_Iterative(num))
print("Factorial using recursive method of",num,"is:",Factorial_Recursive(num))
print("Fibonacci series using recursive method upto",num,"is:",fibonacci_series(num))