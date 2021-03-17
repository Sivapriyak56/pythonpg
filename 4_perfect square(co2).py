n1 = int(input("enter a limit"))
n2 = int(input("enter a limit"))
a=[]
for i in range(n1,n2):
    if (i**(.5)==int(i**(.5))):
        if i%2==0:
            a.append(i)
print(a)



