#9.create a string from a given string where first and last characters exchanged

s=input("enter a string")
str=""
a=s[0]
b=s[-1]
d=s[1:-1]
for i in d:
    str=str+i
print(b+str+a)






