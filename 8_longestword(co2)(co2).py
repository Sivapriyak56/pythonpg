a=[]
n=int(input("enter a number "))
print("enter strings")
for x in range(n):
  x=(input(" "))
  a.append(x)

print(a)
s=[]
for i in a:
    s.append(len(i))
print(s)
d=s[0]
l=0
for x in s:
    if x>=d:
        if l<=x:
            l=x
print(l)


