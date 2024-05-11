import ln

import copy

def daggen(out:str,  n:int):
    g = ln.Graph()
    for i in range(n):
        g.push(i+1)
    while True:
        gn = copy.deepcopy(g)
        try:
            gn.Khan()
            g=gn
        except:
            continue

def main():
    pass

if __name__ == "__main__":
    main()