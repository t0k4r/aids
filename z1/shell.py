import bench
import gen

def sort(arr: list[int]):
    n = len(arr)
    h=1
    while h<n//3:
        h=3*h+1
    while h >= 1:
        for i in range(h, n):
            j=i
            while j>=h and arr[j] < arr[j-h]:
                pim = arr[j]
                arr[j] = arr[j - h]
                arr[j - h] = pim
                j=j-h
        h=(h-1)//2


def main():
    bench.debug(gen.A3, sort, 10)

if __name__ == "__main__":
    main()