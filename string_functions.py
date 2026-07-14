"""
#string function
1. capitalize(): converts frist letter of the frist word into upper case
2.title():converts every words first letter into upper case
3.swap_case():converts uppercase into lower lowercase into upper for each and every character
4.upper():to converts upper case
5.lower():to converts lower case
6.isupper():check whether given string is in upper case or not  (ture/false)
7.islower(): check whether given string is in  lower case or not (true/false)
8.isalpha():check whether string is formed with alphabets only or not(ture/false)
9.isdigit():check whether string is formed with digits only or not (ture/false)
10.isalnum():check whether string is formed with alphabets and digits combination or not
11.split():split the given string into list of items. here default delimiter is space.
12. join():
"""
s="python"
print(s.capitalize())
print(s.title())
s2="Python"
print(s2.swapcase())
print(s.upper())
print(s2.lower())
print(s2.isupper())
print(s.islower())
s3="chandu143@"
print(s3.islower())
print(s3.isalpha())
s1="python-is-easy-language. a must learn langauge "
l=["this","is","chandu",]
s4=""
t=" "
print(s1.capitalize())
print(s1.title())
print(s1.split( " ",2))
print(s4.join(l))
print(t.join(l))
import copy
a=10
print(a,type(a),id(a))
b=copy.copy(a)
print(b,type(b),id(b))
c=copy.deepcopy(a)
print(c,type(c),id(c))
d=[[1,2,3],[10,20,30]]
print(d,type(d),id(d))
for i in d:
    print(i,id(i))
e=copy.copy(d)
print(e,type(e),id(e))
for u in e:
    print(u,id(u))
f=copy.deepcopy(d)
print(f,type(f),id(f))
for t in f :
    print(t,id(t))