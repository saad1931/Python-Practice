str="big data data"
print(len(str))
print(str[0:13])
print(str[0:13:2])
print(str[1:8:2])

print(str[::-1])# reversing string
print(str[-2])
print(str[-4:-3])
print(str[10:11])
print(str[4:5])
"""
1st colon represents starting range and will be printed
2nd colon represents ending range and will not  be printed
3rd colon represents slicing like how many digits we can skip
"""

# functions of string
print(str.find("data"))
print(str.replace("data","DATA"))
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.count(("a")))

word="Saad is student "
print(word[1:4])
print(word[-8:-1])
print(word[8:15])
print(word.find("is"))