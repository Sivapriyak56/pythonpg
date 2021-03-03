# 7.enter two list of integers.check(a)whether list are of same length (b)whether lists sums to same value (c)whether any value occur in both.
l1=[20,50,36,45,47]
l2=[50,45,36,25,70]

leg1=len(l1)
leg2=len(l2)
if leg1==leg2:
  print("a)lists length are same")
else:
  print("a)not same")

total1=sum(l1)
total2=sum(l2)
print("  sum of the list1",total1)
print("  sum of list2",total2)
if total1==total2:
  print("b)sums are same value")
else:
  print("b)not same")

for i in l1:
  for x in l2:
    if i==x:
      print("c)match values are:",i)  