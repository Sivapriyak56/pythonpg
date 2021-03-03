# list comprehension
# a)positive numbers from given list
list = [-2, 3, -4, 5, 6, -7]
newlist = [x for x in list if x > 0]
print(newlist)

#b)square of n numbers
l1=[2,3,4,5,6]
sqlist=[x**2 for x in l1]
print(sqlist)

#b)square of n numbers
list=[]
n=int(input("enter a number "))
for x in range(n):
  x=int(input("enter a number "))
  list.append(x)
sqlist=[x**2 for x in list]
print(sqlist)

#c)vowels in word
wd="ohmygod"
v="aeiou"
list=[]
list=[x for x in wd if x in v]
print(list)

#d)ordinal value
w="journey"
list=[]
list=[ord(x) for x in w]
print(list)