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

def sort(arr:list[int]):
    m = len(arr) - 1
    pom=0
    while m > 0:
        if m % 2 == 0:
            if arr[m] > arr[(m - 1) // 2]:
                pom = arr[m]
                arr[m] = arr[(m - 1) // 2]
                arr[(m - 1) // 2] = pom
                sort(arr)
        else:
            if arr[m] > arr[(m - 1) // 2]:
                pom = arr[m]
                arr[m] = arr[(m - 1) // 2]
                arr[(m - 1) // 2] = pom
                sort(arr)
        m -= 1
    
def main():
    bench.debug(gen.Rand, sort, 10)


if __name__ == "__main__":
    main()