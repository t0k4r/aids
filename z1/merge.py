import gen
import bench

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

def main():
    bench.debug(gen.Rand, sort, 10)

if __name__ == "__main__":
    main()