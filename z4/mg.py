class Graph():
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix: list[list[int]] = matrix # macierz grafu
    def ln(self):
        n = len(self.matrix)
        successors = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n+1):
                v = self.matrix[i][j]
                if v < 0 or v>n: continue
                successors[i].append(v-1)
            successors[i] = list(set(successors[i]))
        return successors
    
    def RobertsFlores(self):
        n = len(self.matrix)
        successors = self.ln()

        def Hamiltonian(v, O, visited, Path, k, start, n):
            O[v] = True
            visited += 1
            for i in successors[v]:
                if i == start and visited == n:
                    return True
                if not O[i]:
                    if Hamiltonian(i, O, visited, Path, k, start, n):
                        Path[k] = v
                        k += 1
                        return True
            O[v] = False
            visited -= 1
            return False

        def Hcycle():
                O = [False] * (n + 1)
                Path = [0] * (n + 1)
                Path[1] = start = 1
                visited = 0
                k = 2
                if Hamiltonian(start, O, visited, Path, k, start, n): 
                    npath = []
                    last = 0
                    while len(npath) != len(Path):
                        v = successors[last][Path[last]]
                        npath.append(v+1)
                        last = v
                        pass
                    return npath                    
                raise Exception("Graf wejściowy nie zawiera cyklu")
        
        return Hcycle()

    def Fleury(self):
        graph: list[list[int]] = self.ln()
        in_degrees = [0] * len(graph)
        out_degrees = [0] * len(graph)

        for i, neighbors in enumerate(graph):
            out_degrees[i] = len(neighbors)
            for neighbor in neighbors:
                in_degrees[neighbor] += 1

        for in_degree, out_degree in zip(in_degrees, out_degrees):
            if in_degree != out_degree:
                raise Exception("Graf wejściowy nie zawiera cyklu")

        def DFS_Euler(v, graph, euler_path):
            while graph[v]:
                u = graph[v].pop()
                DFS_Euler(u, graph, euler_path)
            euler_path.append(v)

        euler_path = []
        start_vertex = 0

        DFS_Euler(start_vertex, graph, euler_path)
        euler_path.reverse()
        return list(map(lambda x: x+1,euler_path))

  
        
        

class GraphBuilder():
    def __init__(self, n) -> None:
        self.matrix: list[list[int]] = [[ 0 for _ in range(n+4)] for _ in range(n) ]
    def edge(self, efrom, eto):
        self.matrix[efrom-1][eto-1] = 1

    def edge2(self, e1,e2):
        self.matrix[e1-1][e2-1] = 1
        self.matrix[e2-1][e1-1] = 1

    def build(self):
        n = len(self.matrix)
        ln = [[] for _ in range(n)]
        lp =  [[] for _ in range(n)]
        lb = [[] for _ in range(n)]
        lc = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 0: continue
                elif self.matrix[i][j] == self.matrix[j][i]:
                    lc[i].append(j)

        for i in range(n):
            for j in range(n):
                if j in lc[i]: continue
                if self.matrix[i][j] == 1:
                    ln[i].append(j)
                    lp[j].append(i)

        for i in range(n):
            for j in range(n):
                if j not in ln[i] and j not in lp[i] and j not in lc[i]:
                    lb[i].append(j)
            

 
        for i in range(n):
            for j in range(n):
                self.matrix[i][j] = 0

        for i in range(n):
            ln[i].sort()
            lni = 0
            try: 
                self.matrix[i][n] = ln[i][lni] +1
                for j in range(n):
                    if j not in ln[i]: continue
                    if lni+1 < len(ln[i]): lni+=1
                    self.matrix[i][j] = ln[i][lni]+1
            except: continue

        for i in range(n):
            lp[i].sort()
            lpi = 0
            try:
                self.matrix[i][n+1] = lp[i][lpi] +1
                for j in range(n):
                    if j not in lp[i]: continue
                    if lpi+1 < len(lp[i]): lpi+=1
                    self.matrix[i][j] = lp[i][lpi]+1+n
            except: continue 

        for i in range(n):
            lb[i].sort()
            lbi = 0
            try:
                self.matrix[i][n+2] = lb[i][lbi] +1
                for j in range(n):
                    pass
                    if j not in lb[i]: continue
                    if lbi+1 < len(lb[i]): lbi+=1
                    self.matrix[i][j] = -lb[i][lbi]-1
            except: continue
        
        for i in range(n):
            lc[i].sort()
            lci = 0
            try: 
                self.matrix[i][n] = lc[i][lci] +1
                for j in range(n):
                    if j not in lc[i]: continue
                    if lci+1 < len(lc[i]): lci+=1
                    self.matrix[i][j] = lc[i][lci]+1+ 2*n
            except: continue

        return Graph(self.matrix)

def cyklHamiltona():
    b = GraphBuilder(6)
    b.edge(1,2)
    b.edge(2,3)
    b.edge(2,5)
    b.edge(3,1)
    b.edge(3,4)
    b.edge(4,6)
    b.edge(5,3)
    b.edge(5,4)
    b.edge(6,1)
    g = b.build()
    print(g.RobertsFlores())

import gen

import networkx as nx
def cyklEulera():
    n_values = [10, 15, 20]  # Adjust according to your needs
    s_values = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    i = 0
    j = 0
    while True:
        try:
            n = n_values[i]
            s = s_values[j]
            gg = gen.generate_eulerian_digraph4(n,s/100)
            print(n,s)
            raise Exception("")
            break
        except: 
            j+=1
            if j == len(s_values):
                i+=1
                j = 0
            continue
    # print(nx.is_eulerian(gg))
    # nx.to_directed(gg)
    # print(nx.has_eulerian_path(gg))
    print(list(nx.eulerian_circuit(gg)))
    # return
    b = GraphBuilder(n)
    # return
    # print("loop")
    for i,j in gg.edges:
        # print(i,j)
        b.edge(i,j)
    # print("endloop")
    # b.edge(1,2)
    # b.edge(2,3)
    # b.edge(3,1)
    g = b.build()
    print(g.ln())
    print(g.Fleury())

if __name__ == "__main__":
    # cyklHamiltona()
    cyklEulera()
    pass

