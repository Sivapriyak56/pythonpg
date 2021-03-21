cr1 = ["red", "blue", "green","yellow",]
cr2 = ["red", "yellow", "pink","orange"]
cr = []
for x in cr1:
    for i in cr2:
        if x == i:
            break
    else:
        cr.append(x)
print(cr)