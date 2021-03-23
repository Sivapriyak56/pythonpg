import csv
with open("movie_trial.csv","w",newline="")as file:
    write=csv.writer(file)
    write.writerow(["S1_No","movie","Rating"])
    write.writerow(["1","don't breath","1"])
    write.writerow(["2","touching the void","2"])
with open("movie_trial.csv")as csvfile:
    data=csv.DictReader(csvfile)
    for r in data:
        print(r['S1_No'],r['movie'])


