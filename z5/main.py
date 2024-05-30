import matplotlib.pyplot as plt


import random
def gen(n, maxsize):
    i = 0
    ret = []
    while i < n:
        item = (random.randint(1, maxsize-1), random.randint(1, n) )
        if item not in ret:
            ret.append(item)
            i+=1
        # print(f"gen{i}")
    return ret
    
    
import sil
import dyn
import zah
import time

def main():
    sill = []
    for i in range(2, 16, 2):
        t = time.time()
        its  = gen(i+5, i)
        sil.maksymalna_wartosc(its,i)
        sill.append(time.time()-t) 
    
    dynl = []
    for i in range(2, 16, 2):
        t = time.time()
        its  = gen(i+5, i)
        dyn.knapsack(i, its)
        dynl.append(time.time()-t) 
    
    zahl = []
    for i in range(2, 16, 2):
        t = time.time()
        its  = gen(i+5, i)
        zah.zachlanny(its,i)
        zahl.append(time.time()-t) 
    
    pass

if __name__ == "__main__":
    main()