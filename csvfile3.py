import csv
h=["rno","sname","branch"]
d=[[1,"s","cse"],[2,"b","ece"],[3,"c","mech"]]
with open("ab.csv","w") as f:
    w=csv.writer(f)
    w.writerow(h)
    w.writerows(d)