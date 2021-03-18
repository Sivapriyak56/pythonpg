# 6.store a list of names.count the occurrences of "a" with in the list
l=["apple","banana","kiwi","ab"]
count=0
for x in l:
  for i in x:
    if "a" in i:
      count=count+1
print(count)      