# program to demonstrate filter function in python
def even(n):
    if n%2==0:
        return True
    else:
        return False
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
r=filter(even,l)
print(list(r))
print()

#program to demonstrate filter function in python using anonymous or lambda function
n1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result=filter(lambda n:n%2==0,n1)
print(list(result))
print()

# program to filter positive number from list of number in lambda function in using
number=(10,-20,22,55,-8,-78,26,8,78,-89,23,-56,72,-2)
poslist=filter(lambda n:0<n,number)
print(list(poslist))
print()
# program to filter positive number from list of number
number1=(10,-20,22,55,-8,-78,26,8,78,-89,23,-56,72,-2)
def poslist(n):
    return n>0
plist=filter(poslist,number1)
print(list(plist))
#promgram to filter words with length>3
list1=["python","java","php","c","c++","javascript"]
def word(n):
    return len(n)>3
res=filter(word,list1)
print(list(res))
print()
#promgram to filter words with length<=3
list1=["python","java","php","c","c++","javascript"]
res=filter(lambda w:len(w)<=3,list1)
print(list(res))