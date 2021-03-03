# 8.get a string from an input string where all occurences of first character replaced with "$",except first character

# a=input("enter a string")
# l=[]
# l2=[]
# str=""
# for x in a:
#   l.append(x)
# s=l[0]
# l2.append(s)
# for i in l[1:]:
#   if s==i:
#     l2.append("$")
#   else:
#     l2.append(i)
# print(l2)
# for z in l2:
#   str=str+z
# print(str)




a=input("enter a string")
str1=""
s=a[0]
b=a[1:]
for i in b:
  if s==i:
    str1=b.replace(i,"$")
print(s+str1)
