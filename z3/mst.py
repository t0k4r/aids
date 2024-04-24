class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # Inicjalizacja pustej macierzy sąsiedztwa (zainicjowanej zerami)
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        # Inicjalizacja listy przechowującej stopnie wejściowe wierzchołków
        self.in_degree = [0] * num_vertices

    def add_edge(self, start, end):
        # Dodanie krawędzi do macierzy sąsiedztwa oraz aktualizacja stopni wejściowych
        start-=1
        end-=1
        self.adj_matrix[start][end] = 1
        self.in_degree[end] += 1

    def tarjan_topological_sort(self, start_vertex=None):
        # Inicjalizacja stosu, zbioru odwiedzonych wierzchołków i listy wynikowej
        stack = []
        visited = set()
        result = []

        # Funkcja dfs wywołująca algorytm Tarjana
        def dfs(vertex):
            # Dodanie wierzchołka do zbioru odwiedzonych
            visited.add(vertex)
            # Rekurencyjne wywołanie dfs dla sąsiadów wierzchołka
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[vertex][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
            # Dodanie wierzchołka do stosu po przetworzeniu wszystkich sąsiadów
            stack.append(vertex)

        # Rozpoczęcie algorytmu Tarjana z wybranego wierzchołka lub z wierzchołka o zerowym stopniu wejściowym
        if start_vertex is not None:
            dfs(start_vertex - 1)
        else:
            # Znalezienie wierzchołka o zerowym stopniu wejściowym
            start_vertices = [i for i in range(self.num_vertices) if self.in_degree[i] == 0]
            for start_vertex in start_vertices:
                if start_vertex not in visited:
                    dfs(start_vertex)

        # Odwrócenie wyniku (wierzchołki na stosie zostają zdjęte w odwrotnej kolejności)
        while stack:
            result.append(stack.pop())

        # Jeśli liczba wierzchołków w wyniku jest równa liczbie wierzchołków w grafie, zwracamy wynik
        # W przeciwnym razie zwracamy None, co oznacza, że graf zawiera cykl
        return result if len(result) == self.num_vertices else None

def read_graph_from_input():
    # Wczytywanie liczby wierzchołków i krawędzi
    num_vertices, num_edges = map(int, input("Podaj liczbę wierzchołków i liczbę krawędzi oddzielone spacją: ").split())
    graph = Graph(num_vertices)
    print("Podaj pary krawędzi (oddzielone spacją):")
    # Dodawanie krawędzi na podstawie danych wprowadzonych przez użytkownika
    for _ in range(num_edges):
        start, end = map(int, input().split())
        graph.add_edge(start, end)
    return graph

def read_graph_from_file(filename):
    # Wczytywanie grafu z pliku tekstowego
    with open(filename, 'r') as file:
        num_vertices, num_edges = map(int, file.readline().split())
        graph = Graph(num_vertices)
        # Dodawanie krawędzi na podstawie danych z pliku
        for _ in range(num_edges):
            start, end = map(int, file.readline().split())
            graph.add_edge(start, end)
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
    sorted_order = graph.tarjan_topological_sort()
    end = time.time()

    if sorted_order is None:
        print("Graf zawiera cykl. Sortowanie niemożliwe.")
    else:
        sorted_order = list(map(lambda x: x+1, sorted_order))
        print("Posortowana kolejność wierzchołków:", sorted_order, end-start)

if __name__ == "__main__":
    main()