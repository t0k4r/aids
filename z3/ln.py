

def main():
    g = Graph()
    g.edge(2137, 420)


class Graph():
    def __init__(self):
        self.verts: dict[int, list[int]] = {}
    
    def push(self, v: int):
        self.verts[v] = []

    def edge(self, e_from: int, e_to: int):
        if e_from in self.verts:
            self.verts[e_from].append(e_to)
        else:
            self.verts[e_from] = [e_to]


    def Khan(self, done:list[int]=[]) -> list[int]:
        out = []
        if len(self.verts) == len(done):
            return out
        ind = {}
        for k, v in self.verts.items():
            if k in done:
                continue
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
        out.append(done)
        out.extend(self.Khan(done))
        return out

if __name__ == "__main__":
    main()