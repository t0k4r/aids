import time
import avl
def testavl(arr:list):
    print("AVL")
    arr.sort()
    t = avl.Tree(arr)
    ti = time.time()
    t.min()
    print("min", time.time()-ti)
    ti = time.time()
    t.max()
    print("max", time.time()-ti)

import bst
def testbst(arr):
    print("BST")
    t = bst.Tree(arr)
    ti = time.time()
    t.min()
    print("min", time.time()-ti)
    ti = time.time()
    t.max()
    print("max", time.time()-ti)
    ti = time.time()
    t.balance()
    print("balansowanie", time.time()-ti)

import time
import bench
import inp
import matplotlib.pyplot as plt
def creategr():
    atr = []
    btr = []
    for i in range(10, 10_000, 10):
        ar = bench.Results()
        br = bench.Results()
        for _ in range(10):
            arr = inp.rand(i)
            start = time.time()
            bst.Tree(arr)
            br.values.append(time.time()-start)
            arr.sort()
            start = time.time()
            avl.Tree(arr)
            ar.values.append(time.time()-start)
        atr.append(ar)
        btr.append(br)

    ax = plt.subplot()
    x = [i for i in range(10,10_000,10)]
    y =list(map(lambda x: x.avg(),atr))
    ax.plot(x,y, label="AVL")
    y =list(map(lambda x: x.avg(),btr))
    ax.plot(x,y, label="BST")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("tworzenie struktury (średia)")
    plt.show()
    ax = plt.subplot()
    x = [i for i in range(10,10_000,10)]
    y =list(map(lambda x: x.stdev(),atr))
    ax.plot(x,y, label="AVL")
    y =list(map(lambda x: x.stdev(),btr))
    ax.plot(x,y, label="BST")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("tworzenie struktury (odchylenie standardowe)")
    plt.show()

def mingr():
    atr = []
    btr = []
    for i in range(10, 10_000, 10):
        ar = bench.Results()
        br = bench.Results()
        for _ in range(10):
            arr = inp.rand(i)
            b = bst.Tree(arr)
            start = time.time()
            b.min()
            br.values.append(time.time()-start)
            arr.sort()
            a = avl.Tree(arr)
            start = time.time()
            a.min()
            ar.values.append(time.time()-start)
        atr.append(ar)
        btr.append(br)

    ax = plt.subplot()
    x = [i for i in range(10,10_000,10)]
    y =list(map(lambda x: x.avg(),atr))
    ax.plot(x,y, label="AVL")
    y =list(map(lambda x: x.avg(),btr))
    ax.plot(x,y, label="BST")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("wyszukiwanie minimum (średnia)")
    plt.show()
    ax = plt.subplot()
    x = [i for i in range(10,10_000,10)]
    y =list(map(lambda x: x.stdev(),atr))
    ax.plot(x,y, label="AVL")
    y =list(map(lambda x: x.stdev(),btr))
    ax.plot(x,y, label="BST")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("wyszukiwanie minimum (odchylenie standardowe)")
    plt.show()


def balgr():
    btr = []
    for i in range(10, 10_000, 10):
        br = bench.Results()
        for _ in range(10):
            arr = inp.rand(i)
            b = bst.Tree(arr)
            start = time.time()
            b.balance
            br.values.append(time.time()-start)
        btr.append(br)

    ax = plt.subplot()
    x = [i for i in range(10,10_000,10)]
    y =list(map(lambda x: x.avg(),btr))
    ax.plot(x,y, label="BST")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("równowarzenie (średnia)")
    plt.show()
    ax = plt.subplot()
    x = [i for i in range(10,10_000,10)]
    y =list(map(lambda x: x.stdev(),btr))
    ax.plot(x,y, label="BST")
    ax.legend()
    ax.set_xlabel("ilość elementów")
    ax.set_ylabel("czas (s)")
    ax.set_title("równowarzenie (odchylenie standardowe)")
    plt.show()

def main():
    # creategr()
    #mingr()
    balgr()

if __name__ == "__main__":
    main()