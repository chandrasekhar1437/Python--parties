# program to read to module
import csv
with open("abc.csv","r") as f:
    c=csv.reader(f)
    print(c)
    for i in c:
        print(i)
