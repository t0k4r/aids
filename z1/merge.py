import gen
import bench

scal = 0

def sort(arr: list[int]):
    n = len(arr)
    if n == 1:
        return
    
    l = arr[:n//2]
    r = arr[n//2:]
    sort(l)
    sort(r)

    i,j = 0,0
    narr=[]
    global scal
    scal +=1
    while i<len(l) or j<len(r):
        if j == len(r):
            narr.append(l[i])
            i+=1
        elif i == len(l):
            narr.append(r[j])
            j+=1
        elif l[i] > r[j]:
            narr.append(l[i])
            i+=1
        else:
            narr.append(r[j])
            j+=1

    for i, e in enumerate(narr):
        arr[i] = e
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
    ax.set_title("mergesort")
    plt.show()
    #bench.debug(gen.Rand, sort, 10)
    #global scal
    #print(f"scalcount: {scal}")

if __name__ == "__main__":
    main()