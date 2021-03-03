#11.find biggest amoung 3 elelments.
a=int(input("enter  number a "))
b=int(input("enter  number b "))
c=int(input("enter  number c "))
if a>b:
  if a>c:
    print("a is greater")
  else:
    print("c is greater")
elif b>c:
  print("b is greater")
else:
  print("c is greater") 