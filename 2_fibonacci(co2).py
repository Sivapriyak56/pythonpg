# 2.generate fibonacci series of n terms
n=int(input("enter a number" ))
a=0
b=1
sum=0
count=1
print("fibonacci series: ")
while count<=n:
  print(sum)
  count+=1
  a=b
  b=sum
  sum=a+b