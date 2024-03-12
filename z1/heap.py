import bench
import gen

# def sort(arr:list[int]):
#     m = len(arr) - 1
#     pom=0
#     levels=1
#     a=1
#     while 2**levels - 1 <= len(arr):
#         levels=levels+1

#     for i in range(levels):
#         while m > 0:
#             if m % 2 == 0:
#                 if arr[m] > arr[(m - 1) // 2]:
#                     pom = arr[m]
#                     arr[m] = arr[(m - 1) // 2]
#                     arr[(m - 1) // 2] = pom
                    
#             else:
#                 if arr[m] > arr[(m - 1) // 2]:
#                     pom = arr[m]
#                     arr[m] = arr[(m - 1) // 2]
#                     arr[(m - 1) // 2] = pom
                    
#             m -= 1

# def sort(arr:list[int]):
#     m = len(arr) - 1
#     pom=0
#     while m > 0:
#         if m % 2 == 0:
#             if arr[m] > arr[(m - 1) // 2]:
#                 pom = arr[m]
#                 arr[m] = arr[(m - 1) // 2]
#                 arr[(m - 1) // 2] = pom
#                 sort(arr)
#         else:
#             if arr[m] > arr[(m - 1) // 2]:
#                 pom = arr[m]
#                 arr[m] = arr[(m - 1) // 2]
#                 arr[(m - 1) // 2] = pom
#                 sort(arr)
#         m -= 1

def heapSort(l):
    m = len(l) - 1
    pom=0
    levels=1
    a=1
    while 2**levels - 1 <= len(l):
        levels=levels+1

    for i in range(levels):
        while m > 0:
            if m % 2 == 0:
                if l[m] > l[(m - 1) // 2]:
                    pom = l[m]
                    l[m] = l[(m - 1) // 2]
                    l[(m - 1) // 2] = pom
                    
            else:
                if l[m] > l[(m - 1) // 2]:
                    pom = l[m]
                    l[m] = l[(m - 1) // 2]
                    l[(m - 1) // 2] = pom
                    
            m -= 1
        
    return l


def sort(arr: list[int]):
    n = len(arr)
    wynik=[]

    g=len(arr)-1
    heapSort(arr)
    for _ in range(n):
        pom=arr[0]
        arr[0]=arr[g]
        arr[g]=pom
        g=g-1
        wynik.append(arr[len(arr)-1])
    
        arr.pop(len(arr)-1)
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