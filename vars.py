        #global variables and local variable
""" local_variable:-1.variable defined and used inside a function definition are called local_variable.
                     2. local variable are accessible with function definition.
   global variable:- variable defined outside of function definition are called global_variable
scope: the region of program in which variable is available for use
lifetime:duration of time in which variable exists in memory during execution
visibility: the programs ability to access a variable from memory
"""




#program demonstrate global and local variables.
print("1.global variable",globals())
p=10
print("2.global variable",globals())
def add(x,y):
    z=x+y
    global p
    p=20
    print(f"result is {z}")
    print(f"inside add p is {p} and q values is {q}")
    print("3.inside global variable", globals())
print("4.global variable",globals())

q=20
print("5.global variable",globals())

add(10,20)
print("6.global variable",globals())
a="2"
c="n"
b=str(a+c)
print(b)
