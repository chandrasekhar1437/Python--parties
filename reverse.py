#module to calculate reverse of number
def rev(n):
    re = 0
    ld = 0
    while n>0:
        ld=n%10
        re=(re*10)+ld
        n=n//10
    return re
p=rev(456)

print(p)