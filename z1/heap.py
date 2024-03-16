import gen
import bench

def swap(l,i,j):
    l[i], l[j] = l[j], l[i]

def siftDown(l,i,upper): #upper bound heap-u
    while(True):
        left=i*2+1
        right=i*2+2
        if max(left,right) < upper: #dwójka dzieci
            if l[i] >=max(l[left],l[right]): #rodzic większy
                break
            elif l[left]<l[right]: #lewy większy
                swap(l,i,left)
                i=left
            else:                   #prawy większy
                swap(l,i,right)
                i = right
        elif left < upper: #tylko lewy
            if l[left]<l[i]:
                swap(l,i,left)
                i=left
            else:
                break
        elif right < upper: #tylko prawy
            if l[right] < l[i]:
                swap(l,i,right)
                i=right
            else:
                break
        else:   #brak dzieci
            break
                    
def heapSort(l):
    for i in range((len(l)-2)//2, -1, -1): #odnoszenie się do ostatniego rodzica, idziemy od końca do początku kopca
       siftDown(l,i,len(l))
    for upper in range(len(l)-1,-1,-1):
        swap(l,0,upper) #Zamiana pierwszego i ostatniego
        siftDown(l,0,upper)        


def sort(arr: list[int]):
    heapSort(arr)
    pass

import time
import matplotlib.pyplot as plt
def main():
    ax = plt.subplot()
    x = [10*i for i in range(1,129)]
    y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.Rand)))
    ax.plot(x,y, label="losowe")
    y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.A)))
    ax.plot(x,y, label="A")
    y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.V)))
    ax.plot(x,y, label="V")
    y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.Asc)))
    ax.plot(x,y, label="rosnące")
    y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.Desc)))
    ax.plot(x,y, label="malejące")
    ax.legend()
    ax.set_xlabel("długość listy")
    ax.set_ylabel("czas (s)")
    ax.set_title("heapsort")
    plt.show()
    # start = time.perf_counter()
    # bench.run(gen.Rand, sort, 10_000, 1)
    # bench.debug(gen.Rand, sort, 10)
    # end = time.perf_counter()
    # print(end-start)    # bench.debug(gen.Rand, sort, 1000)
 
if __name__ == "__main__":
    main()