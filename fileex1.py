# program to demonstrate write mode
with open ("abc.txt","w") as f:
    f.write(str(100))
    f.write("\n")
    f.write(str(3.56))
    f.write("\npython")
    f.write("\nsystem")
    s=l=["10,20,30"]
    f.write(str(s))
