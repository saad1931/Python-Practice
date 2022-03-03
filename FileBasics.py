# # File I/O Basics
# """
# "r"- Open file for reading -default
# "w"- Open file for writing
# "x"- Create file if not exists
# "a"- Add more content to file
# "t"- Text mode -default
# "b"- Binary mode
# "+"- Read and Write both
# """


#For opening
# f=open("file","rt")
# content=f.read()
# print(content)
# f.close()
#
# m=open("file","rt")
# # c= m.readline()
# c=m.readlines()
# print(c)
# m.close()
#
# l=open("file","rt")
#
# for line in l:
#     print(line)
# l.close()




#For writing
# fi=open("f1","w")
# fi.write("This is new file")
# fi.close()


#For appending
# fi=open("f1","a")
# fi.write("\nThis is second line")
# fi.close()


#For writing and reading
# f1=open("f1","r+")
# # f1.write("\nThis is third line")
# # f1.write("\nThis is fourth line")
# a=f1.write("\nThis is fifth line")
# # print(f1.read())
# print(a)
# f1.close()


# # tell & seek
# with open("f1")as f1:
#     print(f1.tell())#tell where is the file pointer
#     print(f1.readline())
#     f1.seek(3)#start reading from the given number
#     print(f1.readline())
#     print(f1.tell())