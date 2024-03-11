import gen
import bench

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
    stack = []
    stack.append((lo, hi))
    while True:
        iter = stack.pop()
        lo, hi = iter[0], iter[1]
        if lo < hi:
            q = partition(arr, lo, hi)
            stack.append((lo, q-1))
            stack.append((q+1, hi))
        if len(stack) == 0: break
    
def main():
    bench.debug(gen.Rand, sort, 10)

if __name__ == "__main__":
    main()