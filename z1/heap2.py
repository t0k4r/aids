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
            if l[left]<l[i]:
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
    for i in range((len(l)-2)//2, -1, -1): #odnoszenie się do ostatniego rodzica, idziemy od końca do początku kopca
       siftDown(l,i,len(l))





def sort(arr: list[int]):
    wynik=[]
    # l=[9,7,5,3,1,2,4,6,8]
    heapSort(arr)
    for i in range(len(arr)):
        if len(arr)>2:
            wynik.append(arr[0])
            del arr[0]
            heapSort(arr)
        else:
            wynik.append(max(arr))
            arr.remove(max(arr))
        heapSort(arr)
    for e in wynik:
        arr.append(e)

import time
def main():
    start = time.perf_counter()
    bench.run(gen.Rand, sort, 10_000, 1)
    # bench.debug(gen.Rand, sort, 10)
    end = time.perf_counter()
    print(end-start)

if __name__ == "__main__":
    main()