
import timeit

start = timeit.default_timer()

#############################

def myMethod(x):
    s = ""
    if x == 0 : print(0)
    while x!=0:
        s += str(x%2)
        x=x//2
    print(s[::-1])

myMethod(15)

##############################

stop = timeit.default_timer()

print('Time: ', stop - start)  