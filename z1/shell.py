import bench
import gen
import matplotlib.pyplot as plt

def sort(arr: list[int]):
    n = len(arr)
    h=1
    #szukam największego możliwego przyrostu
    while h<n//3:
        h=2*h+1
    pom=0
    while h >= 1:
        for i in range(h, n):
            j=i
            while j>=h and arr[j] > arr[j-h]:
                pom = arr[j]
                arr[j] = arr[j - h]
                arr[j - h] = pom
                j=j-h
        #zmniejszenie gap-u
        h=(h-1)//2
            



def main():
    # ax = plt.subplot()
    # x = [10*i for i in range(1,129)]
    # y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.Rand)))
    # ax.plot(x,y, label="losowe")
    # y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.A)))
    # ax.plot(x,y, label="A")
    # y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.V)))
    # ax.plot(x,y, label="V")
    # y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.Asc)))
    # ax.plot(x,y, label="rosnące")
    # y =list(map(lambda x: x.avg(),bench.runtests("", sort, gen.Desc)))
    # ax.plot(x,y, label="malejące")
    # ax.legend()
    # ax.set_xlabel("długość listy")
    # ax.set_ylabel("czas (s)")
    # ax.set_title("shellsort")
    # plt.show()
    bench.debug(gen.V, sort, 10)

if __name__ == "__main__":
    main()