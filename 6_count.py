# 6.store a list of names.count the occurrences of "a" with in the list
l=["apple","banana","kiwi"]
for x in l:
  for i in x:
    if "a" in i:
      count=count+1
print(count)      