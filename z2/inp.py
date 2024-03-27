import random

def rand(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(10, 10000))
    return arr

def keyboard():
    n = int(input("n="))
    arr = []
    for i in range(n):
        arr.append(int(input(f"{i}/{n}=")))
    return arr