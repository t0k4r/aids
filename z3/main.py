import matplotlib.pyplot as plt 
import ln
import mst
import msk
import statistics

def glm(n:int):
    graf = ln.Graph()
    for i in range(n):
        graf.push(i)
    for i in range(n-1):
        graf.edge(i, i+1)
    for i in range(0,n-3,3):
        graf.edge(i, i+3)
    for i in range(0,n-5,5):
        graf.edge(i, i+5)
    for i in range(0,n-7,7):
        graf.edge(i, i+7)
    return graf
def gmst(n:int):
    graf = mst.Graph(n)
    for i in range(n-1):
        graf.add_edge(i, i+1)
    for i in range(0,n-3,3):
        graf.add_edge(i, i+3)
    for i in range(0,n-5,5):
        graf.add_edge(i, i+5)
    for i in range(0,n-7,7):
        graf.add_edge(i, i+7)
    return graf
def gmsk(n:int):
    graf = msk.Graph(n)
    for i in range(n-1):
        graf.add_edge(i, i+1)
    for i in range(0,n-3,3):
        graf.add_edge(i, i+3)
    for i in range(0,n-5,5):
        graf.add_edge(i, i+5)
    for i in range(0,n-7,7):
        graf.add_edge(i, i+7)
    return graf

class Results:
    def __init__(self) -> None:
        self.values: list[float] = []
    def min(self):
        return min(self.values)
    def max(self):
        return max(self.values)
    def avg(self):
        return sum(self.values)/len(self.values)
    def stdev(self):
        return statistics.stdev(self.values)
        
import sys
sys.setrecursionlimit(2137*420*69)
import time

import matplotlib.pyplot as plt
import numpy as np


def triann():
    idx = [ i for i in range(10,1000,10)]
    lln = []
    lms = []
    for i in range(10, 1000, 10):
        lnr = Results()
        msr = Results()
        for _ in range(10):
            ln = glm(i)
            ms = gmst(i)
            
            lns = time.time()
            ln.Trjan()
            lnr.values.append(time.time()-lns) 

            mss = time.time()
            ms.tarjan_topological_sort()
            msr.values.append(time.time()-mss) 
        print(lnr.max(),lnr.min())
        lln.append(lnr)
        lms.append(msr)


    ax = plt.subplot()
    y =list(map(lambda x: x.avg(),lln))
    ax.plot(idx,y, label="lista następników")
    y =list(map(lambda x: x.avg(),lms))
    ax.plot(idx,y, label="macierz sąsiedztwa")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("tarjan")
    plt.show()

    ax = plt.subplot()
    y =list(map(lambda x: x.stdev(),lln))
    ax.plot(idx,y, label="lista następników")
    y =list(map(lambda x: x.stdev(),lms))
    ax.plot(idx,y, label="macierz sąsiedztwa")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("tarjan (odchylenie standardowe)")
    plt.show()

def khann():
    idx = [ i for i in range(10,1000,10)]
    lln = []
    lms = []
    for i in range(10, 1000, 10):
        lnr = Results()
        msr = Results()
        for _ in range(10):
            ln = glm(i)
            ms = gmsk(i)
            
            lns = time.time()
            ln.Khan()
            lnr.values.append(time.time()-lns) 

            mss = time.time()
            ms.topological_sort_kahn()
            msr.values.append(time.time()-mss) 
        print(lnr.max(),lnr.min())
        lln.append(lnr)
        lms.append(msr)


    ax = plt.subplot()
    y =list(map(lambda x: x.avg(),lln))
    ax.plot(idx,y, label="lista następników")
    y =list(map(lambda x: x.avg(),lms))
    ax.plot(idx,y, label="macierz sąsiedztwa")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("kahn")
    plt.show()

    ax = plt.subplot()
    y =list(map(lambda x: x.stdev(),lln))
    ax.plot(idx,y, label="lista następników")
    y =list(map(lambda x: x.stdev(),lms))
    ax.plot(idx,y, label="macierz sąsiedztwa")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("kahn (odchylenie standardowe)")
    plt.show()


def khanl():
    idx = [ i for i in range(10,1000,10)]
    lln = []
    lms = []
    for i in range(10, 1000, 10):
        lnr = Results()
        msr = Results()
        for _ in range(10):
            ln = glm(i)
            ms = gmsk(i)
            
            lns = time.time()
            ln.Khan()
            lnr.values.append(time.time()-lns) 

            mss = time.time()
            ms.topological_sort_kahn()
            msr.values.append(time.time()-mss) 
        print(lnr.max(),lnr.min())
        lln.append(lnr)
        lms.append(msr)

    # ax = plt.subplot()
    # y =list(map(lambda x: x.stdev(),lln))
    # ax.plot(idx,y, label="lista następników")
    # y =list(map(lambda x: x.stdev(),lms))
    # ax.plot(idx,y, label="macierz sąsiedztwa")
    # ax.legend()
    # ax.set_xlabel("ilość elementów")
    # ax.set_ylabel("czas (s)")
    # ax.set_title("khan (odchylenie standardowe)")
    # plt.show()

    ax = plt.subplot()
    plt.yscale("log")
    # plt.xscale("log")
    y =list(map(lambda x: x.avg(),lln))
    ax.plot(idx,y, label="lista następników")
    y =list(map(lambda x: x.avg(),lms))
    ax.plot(idx,y, label="macierz sąsiedztwa")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("kahn")
    plt.show()

def trianl():
    idx = [ i for i in range(10,1000,10)]
    lln = []
    lms = []
    for i in range(10, 1000, 10):
        lnr = Results()
        msr = Results()
        for _ in range(10):
            ln = glm(i)
            ms = gmst(i)
            
            lns = time.time()
            ln.Trjan()
            lnr.values.append(time.time()-lns) 

            mss = time.time()
            ms.tarjan_topological_sort()
            msr.values.append(time.time()-mss) 
        print(lnr.max(),lnr.min())
        lln.append(lnr)
        lms.append(msr)

    # ax = plt.subplot()
    # y =list(map(lambda x: x.stdev(),lln))
    # ax.plot(idx,y, label="lista następników")
    # y =list(map(lambda x: x.stdev(),lms))
    # ax.plot(idx,y, label="macierz sąsiedztwa")
    # ax.legend()
    # ax.set_xlabel("ilość elementów")
    # ax.set_ylabel("czas (s)")
    # ax.set_title("tarjan (odchylenie standardowe)")
    # plt.show()

    ax = plt.subplot()
    plt.xscale("log")
    y =list(map(lambda x: x.avg(),lln))
    ax.plot(idx,y, label="lista następników")
    y =list(map(lambda x: x.avg(),lms))
    ax.plot(idx,y, label="macierz sąsiedztwa")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("tarjan")
    plt.show()


def main():
    # khann()
    # triann()
    khanl()
    # triann()

if __name__ == "__main__":
    main()