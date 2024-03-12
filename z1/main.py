import bench
import shell
import heap
import merge
import quickrec
import quickiter


def main():
    d = {
        "shellsort": shell.sort,
        "heapsort": heap.sort,
        "mergesort": merge.sort,
        "quicksort recursive": quickrec.sort,
        "quicksort iterative": quickiter.sort 
    }
    for name, func in d.items():
        bench.test(name, func, 10000)

if __name__ == "__main__":
    main()