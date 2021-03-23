import csv

f=open("fruit.csv","w")
writer=csv.DictWriter(f,fieldnames=["fruit","count"])
writer.writeheader()
writer.writerow({"fruit":"apple","count":"1"})
writer.writerow({"fruit":"banana","count":"2"})
f.close()
c=0
f=open("fruit.csv")
reader=csv.DictReader(f)
for row in reader:
    if c==0:
        print(f'{" ".join(row)}')
    print(f'{["fruit"]},{row["count"]}')
f.close()