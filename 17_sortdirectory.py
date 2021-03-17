d = {
    "m1": 50,
    "m3": 40,
    "m2": 45
}

s={}
print("in ascending order:")
for x in sorted(d.items()):
    s.update({x})
print(s)

t={}
print("in descending order:")
for a in (sorted(d.items(),reverse=-1)):
    t.update({a})
print(t)








