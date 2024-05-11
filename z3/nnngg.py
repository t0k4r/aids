import ln


def glm(n:int):
    graf = ln.Graph()
    for i in range(n):
        graf.push(i)
    for i in range(n-1):
        graf.edge(i, i+1)
    for i in range(0,n-3,3):
        graf.edge(i, i+3)
    for i in range(0,n-5,5):
        graf.edge(i, i+5)
    for i in range(0,n-7,7):
        graf.edge(i, i+7)
    return graf

g = glm(100)

g.Khan()