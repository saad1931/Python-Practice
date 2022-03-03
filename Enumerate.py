list1=["not","Data","not","AI","not","Machine learning"]

i=1
c=1
for items in list1:
    if i%2==0:
        print(f"Question: What is in your opinion is the future field in computer science? {items}")
    i=i+1

for index,item in enumerate (list1):
    if index%2!=0:
        print(f"Question: What is in your opinion is the future field in computer science? {item}")

if __name__ == '__main__':

    import Time123
    Time123.actualtime("Time:")