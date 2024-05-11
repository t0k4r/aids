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

    def topological_sort_kahn(self):
        sorted_order = []  # Lista przechowująca posortowaną kolejność wierzchołków
        # Kolejka FIFO przechowująca wierzchołki o zerowym stopniu wejściowym
        queue = []

        # Dodanie wierzchołków o zerowym stopniu wejściowym do kolejki
        for node in range(self.num_vertices):
            if self.in_degree[node] == 0:
                queue.append(node)

        # Algorytm sortowania topologicznego za pomocą algorytmu Khana
        while queue:
            node = queue.pop(0)
            sorted_order.append(node)  # Dodanie wierzchołka do posortowanej kolejności

            # Aktualizacja stopni wejściowych sąsiadujących wierzchołków
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[node][neighbor] == 1:
                    self.in_degree[neighbor] -= 1
                    if self.in_degree[neighbor] == 0:
                        queue.append(neighbor)  # Dodanie sąsiada do kolejki, jeśli jego stopień wejściowy wynosi 0

        # Jeśli liczba posortowanych wierzchołków nie jest równa liczbie wierzchołków w grafie,
        # oznacza to, że istnieje cykl w grafie
        if len(sorted_order) != self.num_vertices:
            return None
        else:
            return sorted_order

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
import time
def main():
    choice = input("Czy chcesz wczytać graf z pliku? (T/N): ").upper()
    if choice == "T":
        filename = input("Podaj nazwę pliku z grafem: ")
        graph = read_graph_from_file(filename)
    else:
        graph = read_graph_from_input()

    start = time.time()
    sorted_order = graph.topological_sort_kahn()
    end = time.time()
    if sorted_order is None:
        print("Graf zawiera cykl. Sortowanie niemożliwe.")
    else:
        sorted_order = list(map(lambda x: x+1, sorted_order))
        print("Posortowana kolejność wierzchołków:", sorted_order, end-start)

if __name__ == "__main__":
    main()