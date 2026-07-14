l=[10,56,55,25,89,98]
largest=l[0]
for number in l:
    if number>largest:
        largest=number
print(f"largest number is:{largest}")
# program to demonstrate of list asscreding order
sum=[12,78,21,56,45,60]
sum.sort()
print(sum)
#program to demonstrate biggest number to smallest
num=[45,89,96,88,97,99]
num.sort(reverse=True)
print(num)
#program to demonstrate total values
num=[10,20,30,40]
sum=0
for i in num:
    sum=sum+i
print(f"total value:{sum}")