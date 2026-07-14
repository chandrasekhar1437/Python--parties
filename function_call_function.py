# program to demonstrate function calls
def add(x,y,z):
    return x+y+z


def avg(a,b,c):
    s=add(a,b,c)
    av=s//3
    return av

def avg50(p,q,r):
    az=avg(p,q,r)
    if (az>50):
        print("greater than 50")
    else:
        print("less than 50 ")
avg50(50,60,50)
print(add(1,2,3))
print(avg(1,2,3))