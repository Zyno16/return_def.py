 
def hi(name):
    return("hello "+name)
hi("amr")
hi("ahmed")
h1 = hi("amr")
h2 = hi("ahmed")
print(h1)
print(h2)


def calc(num1,num2,ope):
    r=0
    if ope == "+":
        r = num1 + num2
    elif ope =="-":
        r = num1 - num2
    elif ope =="*":
        r = num1 * num2
    else:
        if num2 == 0: num2 =1
        r = num1/num2
    return(r)
r1 = calc(7,3,"+")
r2 = calc(7,3,"-")
r3 = calc(7,3,"*")
r4 = calc(7,3,"/")
r5 = calc(7,0,"/")
print(r1)
print(r2)
print(r3)
print(r4)
