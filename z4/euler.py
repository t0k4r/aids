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

def find_eulerian_cycle(graph):
    """
    Znajduje cykl Eulera w grafie nieskierowanym.

    Argumenty:
        graph: Tablica dwuwymiarowa reprezentująca graf.

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

graph = read_graph()
try:
    eulerian_cycle = find_eulerian_cycle(graph)
except Exception as e:
    print(e)
else:
    print("Cykl Eulera:", eulerian_cycle)
