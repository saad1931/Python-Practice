print("String formatting method 1:")
d1="My name is Saad and i am a CS student studying in PAF-KIET university and i am here to learn Python"
d2="My ID is 10155 and %s"%d1
print(d2)
print()
print("String formatting method 2:")
d3="Saad"
d4=10155
d5="My name is %s %s"%(d3,d4)
print(d5)
print()
print("String formatting method 3:")
d6="This is {1} {0}"
d7=d6.format(d3,d4)
print(d7)
print()
print("String formatting method 3 using F string:")
d8=f"This is {d3} {d4} {7*7}"
print(d8)