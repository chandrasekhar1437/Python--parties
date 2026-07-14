""""
        #operators of python
        1. arithmetic operators:+ addition ,-sub ,*mul ,/ division ,//floordiv ,% modulus(remainder) ,** exponent
        2.assignment operators:=,+=,-=,*=,/=,//=,**=,%=
        3.comparision/relation operators:== equal, != not equal ,> greater than < less than >= greater than or equal to,<= less than or equai to
        4.logical operators:and  logical AND,or    logical OR, not  logical NOT
        #and :true,true= true. true,false= false. false,true=false. false,false=false.
        #OR : true,true=true.false,true= true.true,false=true. false,false=false.
        #NOT:not(true)=false.not(false)=true.
        5.identity operators:two objects====>same memory location or not  examples :- is, is not
        6.membership operators:in ,not in
        7.bitwise operators:1.& bitwise AND
                            2.| bitwise OR
                            3.^ bitwise XOR
                            4.~ bitwise ones complement
                            5.<< bitwise left shift
                            6.>> bitwise right shift



"""
#example of logical operators AND ,OR
a=10
b=20
c=30
print((a<b)and(a<c))
print((a<b)or(a<c))
print((not(a>b))or(a==c))
#identity of example
a=[10,20,30]
b=a
c=[10,20,30]
d=a.copy()
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))
print(a is b)
#membership operator
a=[10,20,300,400,76]
print(10 in a)
print(11 not in a)
#bitwise operators
print(5&8)
print(5&9)
print(6|8)
a=14
print(a<<3)
a=35
print(a<<5)
print(a>>4)
print(bin(76))

