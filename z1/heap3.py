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
            elif l[left]>l[right]: #lewy większy
                swap(l,i,left)
                i=left
            else:                   #prawy większy
                swap(l,i,right)
                i = right
        elif left < upper: #tylko lewy
            if l[left]>l[i]:
                swap(l,i,left)
                i=left
            else:
                break
        elif right < upper: #tylko prawy
            if l[right] > l[i]:
                swap(l,i,right)
                i=right
            else:
                break
        else:   #brak dzieci
            break
                    
def heapSort(l):
    wynik=[]
    for i in range((len(l)-2)//2, -1, -1): #odnoszenie się do ostatniego rodzica, idziemy od końca do początku kopca
       siftDown(l,i,len(l))
    for upper in range(len(l)-1,-1,-1):
        swap(l,0,upper) #Zamiana pierwszego i ostatniego
        siftDown(l,0,upper)        
        wynik.append(l[upper]) #dodaje to co wyłączam
    # print(l)
    # print(wynik)

def sort(arr: list[int]):
    heapSort(arr)
    pass

import time
def main():
    start = time.perf_counter()
    bench.run(gen.Rand, sort, 10_000, 1)
    # bench.debug(gen.Rand, sort, 10)
    end = time.perf_counter()
    print(end-start)    # bench.debug(gen.Rand, sort, 1000)

if __name__ == "__main__":
    main()