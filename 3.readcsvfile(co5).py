import csv
with open("trial.csv","w",newline="") as file:
    write=csv.writer(file)
    write.writerow(["S1_No","movie","Rating"])
    write.writerow(["1","don't breath","1"])
    write.writerow(["2","narnia","3"])

    with open("trial.csv")as csvfile:
        data=csv.reader(csvfile)
        for r in data:
            print(r)