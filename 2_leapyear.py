# 2.display the future leap year from a current year to final year entered by user.
current=int(input("enter the current year: "))
final=int(input("enter final year: "))
print("leap years are")
for x in range(current,final+1):
  if x%4==0:
    if x%100!=0:
      print(x)
