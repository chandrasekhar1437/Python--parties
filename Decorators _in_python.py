#step-1 normal funnction
def decor(f):
    def saywelcome():
        n=f()
        print(f"welocome {n}")
    return saywelcome

@decor
def myfunction():
    return "python"
#step2


myfunction()