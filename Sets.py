s=set[1,3,5,7,9]
print(type(s))
print(s)



set_list=set[1,2,3,45,6]
print(type(set_list))
print(set_list)

l=[1,3,4,5,5]
set_list2=set[l]
print(type(set_list2))
print(set_list2)

s1=set()
s1.add(6)
s1.add(3)
s1.add(3) # set does not store unique values
print(max(s1))
print(min(s1))
print(len(s1))
s2=s1.union({3,47,6})
print(s1,s2)
s2=s1.intersection({6,7,8})
print(s1,s2)
s3=s1.intersection({2,3})
print(s3)