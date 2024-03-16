import bench
import shell
import heap
import merge
import quickrec
import quickiter

import bench
import matplotlib.pyplot as plt
import gen
def rand():
    ax = plt.subplot()
    x = [10*i for i in range(1,129)]
    y =list(map(lambda x: x.avg(),bench.runtests("", quickiter.sort, gen.Rand)))
    ax.plot(x,y, label="quicksort iteracyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", quickrec.sort, gen.Rand)))
    ax.plot(x,y, label="quicksort rekurencyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", shell.sort, gen.Rand)))
    ax.plot(x,y, label="shellsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", heap.sort, gen.Rand)))
    ax.plot(x,y, label="heapsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", merge.sort, gen.Rand)))
    ax.plot(x,y, label="mergesort")
    ax.legend()
    ax.set_xlabel("długość listy")
    ax.set_ylabel("czas (s)")
    ax.set_title("losowe")
    plt.show()

def A():
    ax = plt.subplot()
    x = [10*i for i in range(1,129)]
    y =list(map(lambda x: x.avg(),bench.runtests("", quickiter.sort, gen.A)))
    ax.plot(x,y, label="quicksort iteracyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", quickrec.sort, gen.A)))
    ax.plot(x,y, label="quicksort rekurencyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", shell.sort, gen.A)))
    ax.plot(x,y, label="shellsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", heap.sort, gen.A)))
    ax.plot(x,y, label="heapsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", merge.sort, gen.A)))
    ax.plot(x,y, label="mergesort")
    ax.legend()
    ax.set_xlabel("długość listy")
    ax.set_ylabel("czas (s)")
    ax.set_title("A")
    plt.show()

def V():
    ax = plt.subplot()
    x = [10*i for i in range(1,129)]
    y =list(map(lambda x: x.avg(),bench.runtests("", quickiter.sort, gen.V)))
    ax.plot(x,y, label="quicksort iteracyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", quickrec.sort, gen.V)))
    ax.plot(x,y, label="quicksort rekurencyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", shell.sort, gen.V)))
    ax.plot(x,y, label="shellsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", heap.sort, gen.V)))
    ax.plot(x,y, label="heapsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", merge.sort, gen.V)))
    ax.plot(x,y, label="mergesort")
    ax.legend()
    ax.set_xlabel("długość listy")
    ax.set_ylabel("czas (s)")
    ax.set_title("V")
    plt.show()

def asc():
    ax = plt.subplot()
    x = [10*i for i in range(1,129)]
    y =list(map(lambda x: x.avg(),bench.runtests("", quickiter.sort, gen.Asc)))
    ax.plot(x,y, label="quicksort iteracyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", quickrec.sort, gen.Asc)))
    ax.plot(x,y, label="quicksort rekurencyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", shell.sort, gen.Asc)))
    ax.plot(x,y, label="shellsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", heap.sort, gen.Asc)))
    ax.plot(x,y, label="heapsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", merge.sort, gen.Asc)))
    ax.plot(x,y, label="mergesort")
    ax.legend()
    ax.set_xlabel("długość listy")
    ax.set_ylabel("czas (s)")
    ax.set_title("rosnąco")
    plt.show()

def desc():
    ax = plt.subplot()
    x = [10*i for i in range(1,129)]
    y =list(map(lambda x: x.avg(),bench.runtests("", quickiter.sort, gen.Desc)))
    ax.plot(x,y, label="quicksort iteracyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", quickrec.sort, gen.Desc)))
    ax.plot(x,y, label="quicksort rekurencyjny")
    y =list(map(lambda x: x.avg(),bench.runtests("", shell.sort, gen.Desc)))
    ax.plot(x,y, label="shellsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", heap.sort, gen.Desc)))
    ax.plot(x,y, label="heapsort")
    y =list(map(lambda x: x.avg(),bench.runtests("", merge.sort, gen.Desc)))
    ax.plot(x,y, label="mergesort")
    ax.legend()
    ax.set_xlabel("długość listy")
    ax.set_ylabel("czas (s)")
    ax.set_title("malejąco")
    plt.show()


def main():
    desc()
    return
    d = {
        "shellsort": shell.sort,
        "heapsort": heap.sort,
        "mergesort": merge.sort,
        "quicksort recursive": quickrec.sort,
        "quicksort iterative": quickiter.sort 
    }
    for name, func in d.items():
        bench.test(name, func, 1_000)

if __name__ == "__main__":
    main()