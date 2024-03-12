import random


def Rand(n:int)->list[int]:
    return [ random.randint(1, 10*n) for _ in range(n)]
    

def Desc(n:int)->list[int]:
    start = random.randint(1,10*n)
    step =  (start) // n
    return [start-(i*step) for i in range(n)]

def Asc(n:int)->list[int]:
    start = random.randint(1,10*n)
    step =  (10*n-start) // n
    return [start+(i*step) for i in range(n)]

def A2(n: int) -> list[int]:
    l = []
    x = n // 2
    a = random.randint(1, 10 * n)
    while a % 2 == 0:
        a = random.randint(1, 10 * n)
    r = random.randint(1, 10 * n)
    while r % 2 != 0:
        r = random.randint(1, 10 * n)

    for _ in range(x + (n % 2)):
        l.append(a)
        r = random.randint(1, 10 * n)
        while r % 2 != 0:
            r = random.randint(1, 10 * n)
        a += r
    while a > 1:
        l.append(a)
        r = random.randint(1, 10 * n)
        while r % 2 != 0:
            r = random.randint(1, 10 * n)
        a -= r

    return l



def randmod2(a,b):
    pass
    n = random.randint(a,b-1)
    if n%2==0: return n
    return n+1

def A(n: int) -> list[int]:
    arr = []
    mid = n//2
    for i in range(mid):
        if i == 0:
            arr.append(randmod2(1, 10)+1)
            continue
        prev = arr[i-1]
        arr.append(randmod2(prev, 10*(i*2))+1)
    for i in range(mid, n):
        prev = arr[i-1]
        min = prev-1//n-i
        arr.append(randmod2(min, prev-2))


    return arr




def V(n:int)->list[int]:
    arr = A(n)
    n = len(arr)
    l = arr[:n//2]
    p = arr[n//2:]
    p.extend(l)
    return p

def In(n:int)->list[int]:
    l =[]
    print("array input:")
    for i in range(n):
        v = input(f"{i}/{n}:")
        l.append(v)
    return l

def Run(name, fn):
    print(f"{name:}")
    for _fn in [ Asc, Desc, A, V, Rand]:
        l = _fn(10)
        print(f"{_fn.__name__}: {l}")
        fn(l) # type: ignore
        print(f"sorted: {l}")