import bench
import gen

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
    bench.debug(gen.V, sort, 10)

if __name__ == "__main__":
    main()