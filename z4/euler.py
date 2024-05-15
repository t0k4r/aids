def read_graph():
    """
    Wczytuje macierz sąsiedztwa.

    Zwraca:
        graph: Tablica dwuwymiarowa, gdzie i-ty wiersz i j-ta kolumna
               reprezentują połączenie między wierzchołkiem i a wierzchołkiem j.
    """
    vertices, edges = map(int, input().split())
    graph = []
    for i in range(vertices):
        row = []
        for j in range(vertices):  # Poprawiono indeksowanie
            row.append(0)
        graph.append(row)

    for _ in range(edges):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1
    return graph

def has_odd_degree(graph):
    """
    Sprawdza, czy graf ma wierzchołki o nieparzystym stopniu.

    Argumenty:
        graph: Tablica dwuwymiarowa reprezentująca graf.

    Zwraca:
        True, jeśli graf ma wierzchołki o nieparzystym stopniu.
        False w przeciwnym przypadku.
    """
    for vertex in range(len(graph)):
        degree = 0
        for neighbor in range(len(graph)):
            if graph[vertex][neighbor] == 1:
                degree += 1
        if degree % 2 != 0:
            return True
    return False

def afind_eulerian_cycle(graph):
    """
    Znajduje cykl Eulera w grafie nieskierowanym.

    Argumenty:
        graph: Tablica dwuwymiarowa reprezentująca graf w positaci macierzy sąsiedztwa.

    Zwraca:
        eulerian_cycle: Lista wierzchołków tworzących cykl Eulera.
    """
    if has_odd_degree(graph):
        raise Exception("Graf nie ma cyklu Eulera")

    current_vertex = 0
    eulerian_cycle = [current_vertex]
    while True:
        if sum(graph[current_vertex]) == 0:
            break
        next_vertex = None
        for neighbor in range(len(graph)):
            if graph[current_vertex][neighbor] == 1:
                next_vertex = neighbor
                break
        if next_vertex is not None:
            graph[current_vertex][next_vertex] -= 1
            graph[next_vertex][current_vertex] -= 1
            eulerian_cycle.append(next_vertex)
            current_vertex = next_vertex
        else:
            # Backtrack
            current_vertex = eulerian_cycle.pop()
            if not eulerian_cycle:
                break

    return eulerian_cycle


# def dfs(matrix, v):
#     visited = [False] * len(matrix)
#     out = []
#     def dfs(matrix, v, visited):
#         visited[v] = True
#         out.append(v)
#         for i in range(len(matrix)):
#             if matrix[v][i] == 1 and not visited[i]:
#                 dfs(matrix, i, visited)
#     dfs(matrix, v, visited)
#     return out
# def is_bridge(matrix, u ,v):
#     A = dfs(matrix, v)
#     matrix[u][v] = 0
#     matrix[v][u] = 0
#     B = dfs(matrix, v)
#     matrix[u][v] = 1
#     matrix[v][u] = 1
#     if len(A) != len(B):
#         return True
#     for a,b in zip(A,B):
#         if a != b:
#             return True
#     return False
def dfs(matrix, v, visited):
    visited[v] = True
    out = [v]
    for i in range(len(matrix)):
        if matrix[v][i] == 1 and not visited[i]:
            out.extend(dfs(matrix, i, visited))
    return out

def is_bridge(matrix, u ,v):
    visited = [False] * len(matrix)
    A = dfs(matrix, v, visited)
    matrix[u][v] = 0
    matrix[v][u] = 0
    visited = [False] * len(matrix)
    B = dfs(matrix, v, visited)
    matrix[u][v] = 1
    matrix[v][u] = 1
    # print(A)
    # print(B)
    return len(A) != len(B)

def Fleury(matrix:list[list[int]]):
    def ok():
        nonlocal matrix
        for vertex_degree in map(sum, matrix):
            if vertex_degree % 2 != 0:
                return False
        return True
    
    def find_eulerian_cycle(matrix, u, cycle):
        bs = []
        for v in range(len(matrix)):
            if  matrix[u][v] > 0:
                if is_bridge(matrix,u,v): 
                    bs.append((u,v))
                    # print("b")
                    continue
                # print("nb")
                matrix[u][v] = 0
                matrix[v][u] = 0
                find_eulerian_cycle(matrix, v, cycle)
        for u,v in bs:
            matrix[u][v] = 0
            matrix[v][u] = 0
            find_eulerian_cycle(matrix, v, cycle)
        cycle.append(u)

    if not ok():
        raise Exception("Graf wejściowy nie zawiera cyklu.")
    
    start_vertex = 0  # Wybierz dowolny wierzchołek startowy
    cycle = []
    find_eulerian_cycle(matrix, start_vertex, cycle)
    
    return cycle[::-1]
# graph = read_graph()
# try:
#     eulerian_cycle = find_eulerian_cycle(graph)
# except Exception as e:
#     print(e)
# else:
#     print("Cykl Eulera:", eulerian_cycle)

import sys
sys.setrecursionlimit(2137*420*69)
import gen
def gen_graph():
    n,s = 5,10
    G = gen.directed_eulerian(n,s)
    graph = []
    for i in range(n):
        row = []
        for j in range(n):  # Poprawiono indeksowanie
            row.append(0)
        graph.append(row)

    edges = []
    edges.append((1,2))
    edges.append((1,4))
    edges.append((2,4))
    edges.append((3,4))
    edges.append((3,5))
    edges.append((5,4))
    # edges.append((1,3))
    # edges.append((1,4))
    # edges.append((2,4))
    # edges.append((2,0))
    # edges.append((3,4))
    # edges.append((3,0))

    for i, j in edges:
        graph[i-1][j-1] = 1
        graph[j-1][i-1] = 1
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end="\t")
        print()
    return graph



def read_graph_from_file(filename):
    # Wczytywanie grafu z pliku tekstowego
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        graph = []
        for i in range(num_vertices):
            row = [0] * num_vertices
            graph.append(row)
        # Dodawanie krawędzi na podstawie danych z pliku
        for _ in range(num_edges):
            i, j = map(int, file.readline().split())
            graph[i][j] = 1
            graph[j][i] = 1
        return graph


def cykeEulera():
    graph = gen_graph()
    # print(find_eulerian_cycle(graph))
    print(Fleury(graph))
    pass

if __name__ == "__main__":
    cykeEulera()
    pass