
def read_graph_from_input():
    # Wczytywanie liczby wierzchołków i krawędzi
    num_vertices, num_edges = map(int, input("Podaj liczbę wierzchołków i liczbę krawędzi oddzielone spacją: ").split())
    graph = Graph()
    for i in range(num_vertices):
        graph.push(i+1)
    print("Podaj pary krawędzi (oddzielone spacją):")
    # Dodawanie krawędzi na podstawie danych wprowadzonych przez użytkownika
    for _ in range(num_edges):
        start, end = map(int, input().split())
        graph.edge(start, end)
    return graph

def read_graph_from_file(filename):
    # Wczytywanie grafu z pliku tekstowego
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        graph = Graph()
        for i in range(num_vertices):
            graph.push(i+1)
        # Dodawanie krawędzi na podstawie danych z pliku
        for _ in range(num_edges):
            start, end = map(int, file.readline().split())
            graph.edge(start, end)
        return graph

import time
def main():
    choice = input("Czy chcesz wczytać graf z pliku? (T/N): ").upper()
    if choice == "T":
        filename = input("Podaj nazwę pliku z grafem: ")
        graph = read_graph_from_file(filename)
    else:
        graph = read_graph_from_input()

    start = time.time()
    sorted_order = graph.Khan()
    end = time.time()
    if sorted_order is None:
        print("Graf zawiera cykl. Sortowanie niemożliwe.")
    else:
        print("Posortowana kolejność wierzchołków:", sorted_order, end-start)
    # g = Graph()
    # for i in range(10):
    #     g.push(i+1)
    # g.edge(1,2)
    # g.edge(1,10)
    # g.edge(2,3)
    # g.edge(2,7)
    # g.edge(3,4)
    # g.edge(4,6)
    # g.edge(5,2)
    # g.edge(5,7)
    # g.edge(6,9)
    # g.edge(7,6)
    # g.edge(7,8)
    # g.edge(7,9)
    # g.edge(8,4)
    # g.edge(8,6)
    # g.edge(8,9)
    # g.edge(10,5)
    # g.edge(10,6)
    # print(g.Khan())


class Graph():
    def __init__(self):
        self.verts: dict[int, list[int]] = {}
    
    def push(self, v: int):
        if v not in self.verts:
            self.verts[v] = []

    def edge(self, e_from: int, e_to: int):
        if e_from in self.verts:
            self.verts[e_from].append(e_to)
        else:
            self.verts[e_from] = [e_to]

    def Khan(self, done:list[int]=[]) -> list[int]:
        out:list[int] = []
        if len(self.verts) == len(done):
            return out
        ind:dict[int, int] = {}
        for k in self.verts.keys():
            if k not in done:
                ind[k] = 0
        for k, v in self.verts.items():
            if k not in done:
                for n in v:
                    ind[n]+=1
        val = None
        for k, v in ind.items():
            if v == 0:
                val = k
                break
        if val == None:
            raise Exception("Graf zawiera cykl. Sortowanie niemożliwe.")
        done.append(val)
        out.append(val)
        out.extend(self.Khan(done))
        return out

    def Trjan(self, start:int|None=None) -> list[int]:
        colors:dict[int, str]={}
        out:list[int] = []
        
        def get_start(done:list[int]=[]) -> int :
            ind: dict[int,int] = {}
            for k in self.verts.keys():
                if k not in done:
                    ind[k] = 0
            for k, v in self.verts.items():
                if k not in done:
                    for n in v:
                        ind[n]+=1
            k, v = sorted(ind.items(), key=lambda x: x).pop(0)
            return k
        
        if start == None:
            start = get_start()
        for k in self.verts.keys():
            colors[k] = "white"
        chain = []
        def visit(v: int):
            nonlocal colors, out
            if colors[v] == "grey":
                raise Exception("Graf zawiera cykl. Sortowanie niemożliwe.")
            if colors[v] == "black":
                return
            colors[v] = "grey"
            for i in self.verts[v]:
                visit(i)
            colors[v] = "black"
            out.insert(0, v)

        visit(start)
        return out

if __name__ == "__main__":
    main()