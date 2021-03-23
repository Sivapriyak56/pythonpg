f=open("pgg.txt","r")
f1=open("newtext.txt","w")
r=f.readline()
for i in range(0,len(r)):
    if(i%2!=0):
        f1.write(r[i])
    else:
        pass

f.close()
f1.close()
g=open("newtext.txt","r")
h=g.read()
print(h)
g.close()