num=[1,2,3,4,5,6,7,8,9,10]
#Map

def square(n):
    return n*n

def cube(n):
    return n*n*n

sq=list(map(square,num))
print("List of squares of numbers 1-10 using function: ",sq)


sq2=list(map(lambda x:x*x,num))
print("List of squares of numbers 1-10 using lambda: ",sq2)

func=[square,cube]
for i in range(1,11):
    val=list(map(lambda x:x(i),func))
    print(val)

#Filter

def filtereven(n):
    if n%2==0:
        return n

def filterodd(n):
    if n%2 !=0:
        return n

print("List of Numbers:")
print(num)

evennum=list(filter(filtereven,num))
print("Even numbers from list are:",evennum)


oddnum=list(filter(filterodd,num))
print("Odd numbers from list are:",oddnum)

#Reduce

from functools import reduce
l1=[1,2,3,4,5]
l2=list(range(1,101))

plus=reduce(lambda x,y:x+y,l2)
print(plus)

red=reduce(lambda x,y:x+y,l1)
print(red)