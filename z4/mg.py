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
        return euler_path
        return list(map(lambda x: x+1,euler_path))

class GraphBuilder():
    def __init__(self, n) -> None:
        self.matrix: list[list[int]] = [[ 0 for _ in range(n+4)] for _ in range(n) ]
    def edge(self, efrom, eto):
        self.matrix[efrom-1][eto-1] = 1
    def build(self):
        # print("BUILD")
        n = len(self.matrix)
        ln = [[] for _ in range(n)]
        lp = [[] for _ in range(n)]
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
                            
        # print("LN")
        # for i, v in enumerate(ln):
        #     l = []
        #     l.extend(v)  
        #     l.extend(lc[i])
        #     l.sort()
        #     print(i+1,list(map(lambda x: x+1,l )))
        # print("LC")
        # for i, v in enumerate(lc):
        #     l = v
        #     l.sort()
        #     print(i+1,list(map(lambda x: x+1,l )))


        for i in range(n):
            ln[i].sort()
            lni = 0
            if 0 != len(ln[i]):
                self.matrix[i][n] = ln[i][lni] +1
            for j in range(n):
                if j not in ln[i]: continue
                if lni+1 < len(ln[i]): lni+=1
                self.matrix[i][j] = ln[i][lni]+1
            # print(self.matrix[i])
            # except: continue

        for i in range(n):
            lp[i].sort()
            lpi = 0
            if 0 != len(lp[i]):
                self.matrix[i][n+1] = lp[i][lpi] +1
            for j in range(n):
                if j not in lp[i]: continue
                if lpi+1 < len(lp[i]): lpi+=1
                self.matrix[i][j] = lp[i][lpi]+1+n
            # except: continue 

        for i in range(n):
            lb[i].sort()
            lbi = 0
            # try:
            if 0 != len(lb[i]):
                self.matrix[i][n+2] = lb[i][lbi] +1
            for j in range(n):
                pass
                if j not in lb[i]: continue
                if lbi+1 < len(lb[i]): lbi+=1
                self.matrix[i][j] = -lb[i][lbi]-1
            # except: continue
        
        for i in range(n):
            lc[i].sort()
            lci = 0
            # try: 
            if 0 != len(lc[i]):
                self.matrix[i][n+3] = lc[i][lci] +1
            for j in range(n):
                if j not in lc[i]: continue
                if lci+1 < len(lc[i]): lci+=1
                self.matrix[i][j] = lc[i][lci]+1+ 2*n
            # except: continue

        return self.matrix

def RobertsFlores(matrix: list[list[int]]):
    # print("ROBERTSFLORES")
    N = len(matrix)
    O = [False for _ in range(N+1)]
    PATH = []
    def successors(v:int) -> list[int]:
        s = []
        val = matrix[v][N]
        if val != 0:
            s.append(matrix[v][N]-1)
        for i in range(N):
            if matrix[v][N+3] != 0: 
                s.append(matrix[v][N+3]-1)

            val = matrix[v][i]
            if val<=0 or (val>N and val<2*N): continue
            if val <= N:
                s.append(val-1)
            else:
                val = val-2*N -1
                if val <= 0 : continue
                s.append(val)
        l = list(set(s))
        # print(v+1, list(map(lambda x: x+1, l)))
        return l
    
    # for v in range(N):
    #     print(v+1, list(map(lambda x: x+1, successors(v))), matrix[v])
    START = 0
    def hamiltonian(v:int)->bool:
        # print("GET", v+1)
        O[v] = True
        for i in successors(v):
            if i == START and sum(O) == N:
                PATH.append(v)
                return True
            if not O[i]:
                if hamiltonian(i):
                    PATH.append(v)
                    return True
            # print("RET", v+1)
        # print("REM", v+1)
        O[v] = False
        return False
    O[0]= True
    PATH.append(START)
    if not hamiltonian(START):
        raise Exception("Graf wejściowy nie zawiera cyklu")
    PATH.reverse()
    return list(map(lambda x:x+1, PATH))


def Fleury(matrix: list[list[int]]):
    N = len(matrix)
    def successors(v:int) -> list[int]:
        s = []
        s.append(matrix[v][N]-1)
        for i in range(N):
            val = matrix[v][i]
            if val<=0 or (val>N and val<2*N): continue
            if val <= N:
                s.append(val-1)
            else:
                val = val-2*N -1
                if val <= 0 : continue
                s.append(val)
        l = list(set(s))
        l.sort()
        return l
    delege = {}
    START = 0

def cyklHamiltona():
    n, s = 15, 90
    h = gen.directed_hamiltonian(n,s)
    b = GraphBuilder(n)
    for i, j in h.edges:
        # print(i+1,j+1)
        b.edge(i+1,j+1)
    print(RobertsFlores(b.build()))


import gen

import networkx as nx
def cyklEulera():
    n,s = 10,    10
    e = gen.directed_eulerian(n,s)
    b = GraphBuilder(n)
    for i,j in e.edges:
        print(i,j)
        b.edge(i,j)

if __name__ == "__main__":
    cyklHamiltona()
    # cyklEulera()
    pass

