
import random  
def fun1():
    int1 = random.randint(1000,10000)
    for i in range(2,int1):
        if (int1 % i) == 0:
            return 0
    else:
        return int1
fun1=fun1()
def fun2():
    int2 = random.randint(1000,10000)    
    for i in range(2,int2):
        if (int2 % i) == 0:
            return 0
    else:
        return int2
fun2=fun2()

if (fun1!=0)&(fun2!=0)&(fun1>fun2):
    print(fun2)
elif (fun1!=0)&(fun2!=0)&(fun1<fun2):
    print(fun1)
elif (fun1==0)&(fun2==0):
    print()
elif(fun1!=0)&(fun2==0):
    print(fun1)
else:
    print(fun2)
