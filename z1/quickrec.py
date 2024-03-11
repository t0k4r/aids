import gen
import sys
import bench
sys.setrecursionlimit(2137*420*69)

def sort(arr: list[int]):
    qsort(arr,0, len(arr)-1)

def partition(arr: list[int], lo:int, hi:int)->int:
    pivot = arr[hi]
    i, j = lo, hi
    while True:
        while arr[i] > pivot: i+=1
        while arr[j] < pivot: j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1;j-=1
        else:
            return j   


def qsort(arr: list[int], lo:int, hi:int):
    if lo<hi:
        q = partition(arr, lo, hi)
        qsort(arr, lo,q-1)
        qsort(arr, q+1, hi)



def main():
    bench.debug(gen.Rand, sort, 10)


if __name__ == "__main__":
    main()