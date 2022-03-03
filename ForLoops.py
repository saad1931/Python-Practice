list1=[["Saad",22],["Ali",21],["Sabeen",23],["Sara",20]]

for name,age in list1:
    print(name,"is",age,"years old.")



Dict1={"Saad":10155,"Ashaj":10097}
print(Dict1["Saad"])

for stu,id in Dict1.items():
    print(stu,"has Id",id)

#quiz
list2=[1,6,7,8,2]
for num in list2:
    if(num>6):
        print(num)