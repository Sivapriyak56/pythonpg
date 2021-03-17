a=input("enter a string :")
x=a[-3:]
if x=="ing":
    v=a.replace(x,"ly")
else:
    v=a.replace(x,"ing")
print(v)