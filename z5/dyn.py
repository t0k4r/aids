def knapsack(capacity, items):
    W = [item[0] for item in items]
    V = [item[1] for item in items]

    if W is None or V is None or len(W) != len(V) or capacity < 0:
        print("Złe dane")
        
    
    N = len(W) #ilość elementów

    
    # tablica z 0
    DP = [[0] * (capacity + 1) for _ in range(N + 1)]

    # uzupełnianie tablicy
    for i in range(1, N + 1):
        w = W[i - 1]
        v = V[i - 1]

        for sz in range(1, capacity + 1):
            DP[i][sz] = DP[i - 1][sz]
            if sz >= w:
                if DP[i - 1][sz - w] + v > DP[i][sz]:
                    DP[i][sz] = DP[i - 1][sz - w] + v


    sz = capacity
    itemsSelected = []

    #idziemy od końca
    for i in range(N, 0, -1):
        if DP[i][sz] != DP[i - 1][sz]:
            itemIndex = i - 1
            itemsSelected.append(itemIndex)
            sz -= W[itemIndex]

    itemsSelected.reverse()
    print("Wybrane przedmioty:")
    for itemIndex in itemsSelected:
        print("Pojemność:", items[itemIndex][0], "Wartość:", items[itemIndex][1])

    return DP[N][capacity]

n, b = map(int, input().split())

items = []
for i in range(n):
    r, w = map(int, input().split())
    items.append((r, w))

print("Wartość zapakowanego plecaka", knapsack(b, items))
