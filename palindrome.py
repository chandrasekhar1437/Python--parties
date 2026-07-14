import reverse as r


n=int(input("enter the number"))
if n==r.rev(n):
    print("palindrome")
else:
    print("not palindrome")