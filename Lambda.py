# Lambda or Anonymous

def minusfunc(a,b):
    """
function for minus 2 values
    """
    return a-b

# print(minusfunc.__doc__)

minuslambda=lambda x,y:x-y

n1=int(input("Enter Value 1:"))
n2=int(input("Enter Value 2:"))

print("Answer using Function:",minusfunc(n1,n2))
print("Answer using Lambda/Anonymous:",minuslambda(n1,n2))

print("------------------------------------------------------")
print("Lambda example for sorting list of list:")
a=[[5,6],[24,3],[3,5]]
a.sort(key=lambda x:x[0])
print(a)