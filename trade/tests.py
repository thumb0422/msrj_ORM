
import time

def myDecorate2(func):
    def aaaTime(*args,**kwargs):
        print('aaaTime -----1')
        func(*args,**kwargs)
        print('aaaTime -----2')
    return aaaTime


def myDecorate1(func):
    def countTime(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print('spent time = %s'%(end-start))
    return countTime

@myDecorate2
@myDecorate1
def sumAB(a,b):
    print(a*b)
    return a*b


sumAB(10,20)