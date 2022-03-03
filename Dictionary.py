# Dictionary is key value pairs


d1={"Saad":"10155","Ashaj":10097,"kamran":9999}
print(d1["Saad"])
print(d1["Ashaj"])
d1["Ali"]=2345
print(d1)
del d1["Ali"]
d1["Akbar"]={"good":"best","Topper":1}
print(d1["Akbar"])
print(d1["Akbar"]["Topper"])
d2=d1.copy()
del d2["Akbar"]
print(d1.get("Saad"))
d1.update({"Anas":2})
print(d1.keys())
print(d1.items())
print(d1)
print(d2)

# Exercise

"""
Create a dictionary which have 4 words and there meaning and take input from user a word and print it's meaning
"""
print("Exercise 1")
Words_Meaning = {
                 "Mutable":"Can be changed",
                 "Immutable":"Cannot be Changed",
                 "List":"[]",
                 "Tuple":"()",
                 "Dictionary":"{}"
                }

print("Please enter a word for printing it's meaning: ")
word=input()
print("Meaning of",word,"is:",Words_Meaning[word])
#print(Words_Meaning[word])