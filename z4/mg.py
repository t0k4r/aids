class Graph():
    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix: list[list[int]] = matrix
    def RobertsFlores(self):
        pass
    def Fleury(self):
        pass

class GraphBuilder():
    def __init__(self, n) -> None:
        self.matrix: list[list[int]] = [[ 0 for _ in range(n+4)] for _ in range(n) ]
    def edge(self, efrom, eto):
        self.matrix[efrom-1][eto-1] = 1
    def build(self):
        n = len(self.matrix)
        ln = [[] for _ in range(n)]
        lp =  [[] for _ in range(n)]
        lb = [[] for _ in range(n)]
        lc = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 0:
                    continue
                elif self.matrix[i][j] == self.matrix[j][i]:
                    lc[i].append(j)

        for i in range(n):
            for j in range(n):
                if j in lc[i]:
                    continue
                if g.matrix[i][j] == 1:
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
            lc[i].sort()
            lci = 0
            try: 
                self.matrix[i][n] = lc[i][lci]
                for j in range(n):
                    if j not in lc[i]: continue
                    if lci+1 < len(lc[i]):
                        lci+=1
                    self.matrix[i][j] = lc[i][lci] + 2*n
            except:
                continue

        for i in range(n):
            ln[i].sort()
            lni = 0
            print(i,lni)
            try: 
                self.matrix[i][n] = ln[i][lni]
                for j in range(n):
                    if j not in ln[i]: continue
                    if lni+1 < len(ln[i]):
                        lni+=1
                    self.matrix[i][j] = ln[i][lni]
            except:
                continue
        for i in range(n):
            lp[i].sort()
            lpi = 0
            try:
                self.matrix[i][n+1] = lp[i][lpi]
                for j in range(n):
                    if j not in lp[i]: continue
                    if lpi+1 < len(lp[i]):
                        lpi+=1
                    self.matrix[i][j] = lp[i][lpi]+n
            except:
                continue 

        for i in range(n):
            lb[i].sort()
            lbi = 0
            try:
                self.matrix[i][n+2] = lb[i][lbi]
                for j in range(n):
                    pass
                    if j not in lb[i]: continue
                    if lbi+1 < len(lb[i]):
                        lbi+=1
                    self.matrix[i][j] = -lb[i][lbi]
            except: continue
        return Graph(self.matrix)




g = GraphBuilder(7)
g.edge(1,5)
g.edge(1,1)
g.edge(2,3)
g.edge(2,5)
g.edge(2,6)
g.edge(2,7)
g.edge(3,6)
g.edge(3,6)
g.edge(3,7)
g.edge(5,6)
g.edge(6,5)

# g.edge(1,2)
# g.edge(2,4)
# g.edge(2,5)
# g.edge(3,1)
# g.edge(3,2)
# g.edge(4,3)
# g.edge(5,1)
# g.edge(5,4)

g.build()
for i in range(7):
    for j in range(7+4):
        q = g.matrix[i][j]
        if q >= 0: q+=1
        else: q-=1
        print(q,end="\t")
    print()