import gen
import sys
import bench
import matplotlib.pyplot as plt

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

    return
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
    ax.set_title("quicksort rekurencyjny")
    plt.show()


if __name__ == "__main__":
    main()