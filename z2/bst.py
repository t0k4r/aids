class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root == None: # Sprawdź, czy istnieje już węzeł, jeśli nie, to go utwórz
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    
    return root

# Funkcja do wypisania drzewa w porządku pre-order
def preorder_traversal(node):
    if node != None:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def find_max(node, maks):
    if node is not None:
        if node.value > maks:
            maks = node.value
        maks_left = find_max(node.left, maks)
        maks_right = find_max(node.right, maks)
        return max(maks, maks_left, maks_right)
    else: # Po przejściu przez całe drzewo
        return maks


def find_path_to_max(root, maks):
    if root is None:
        return None

    if root.value == maks:
        return [root.value] # Zwracanie listy ścieżki, gdy aktualna wartość jest równa maksymalnej

    left_path = find_path_to_max(root.left, maks) # Dodawanie
    if left_path is not None:
        return [root.value] + left_path # Dodawanie dwóch list

    right_path = find_path_to_max(root.right, maks)
    if right_path is not None:
        return [root.value] + right_path

    return None


def find_min(node, min_value):
    if node is not None:
        if node.value < min_value:
            min_value = node.value

        # Rekurencyjnie znajduje minimalną wartość w lewym poddrzewie
        min_left = find_min(node.left, min_value)
        min_right = find_min(node.right, min_value)
        # Zwraca minimalną wartość spośród wartości bieżącego węzła, lewego i prawego poddrzewa
        return min(min_value, min_left, min_right)
    else: 
        return min_value


def find_path_to_min(root, min_value):
    if root is None:
        return None

    if root.value == min_value:
        return [root.value]  # Zwracanie listy ścieżki, gdy aktualna wartość jest równa minimalnej

    left_path = find_path_to_min(root.left, min_value)  # Przeszukiwanie lewego poddrzewa
    if left_path is not None:
        return [root.value] + left_path

    right_path = find_path_to_min(root.right, min_value)  # Przeszukiwanie prawego poddrzewa
    if right_path is not None:
        return [root.value] + right_path

    return None


def inorder_reverse_traversal(node):
    if node is not None:
        inorder_reverse_traversal(node.right)
        print(node.value, end=" ")
        inorder_reverse_traversal(node.left)



def level_of_node(root, key, current_level=1): # Szukanie poziomu
    if root is None:
        return 0
    if root.value == key:
        return current_level
    left_level = level_of_node(root.left, key, current_level + 1)
    if left_level != 0: # Jeśli == 0 -> nie ma w lewym poddrzewie
        return left_level # Rekurencja
    return level_of_node(root.right, key, current_level + 1)

def print_nodes_at_level(root, level):
    if root is None:
        return # Koniec drzewa, koniec funkcji
    if level == 1: 
        print(root.value, end=" ")
    elif level > 1:
        print_nodes_at_level(root.left, level - 1)
        print_nodes_at_level(root.right, level - 1)



def delete_node(root, key):
    if root == None:
        return root
    
    # Przypadek 1: Węzeł do usunięcia jest liściem (nie ma dzieci)
    if root.value == key and root.left == None and root.right == None:
        return None
    
    # Przypadek 2: Węzeł do usunięcia ma jedno dziecko
    if root.value == key and root.left == None:
        return root.right
    if root.value == key and root.right == None:
        return root.left
    
    # Przypadek 3: Węzeł do usunięcia ma dwoje dzieci
    if root.value == key:
        # Znajdź węzeł zastępczy (najmniejszy w prawym poddrzewie)
        successor = find_min(root.right, root.right.value)
        # Usuń węzeł zastępczy
        root.right = delete_node(root.right, successor)
        # Zastąp usuwany węzeł przez węzeł zastępczy
        root.value = successor
    
    # Rekurencyjnie usuń węzeł z lewego i prawego poddrzewa
    root.left = delete_node(root.left, key)
    root.right = delete_node(root.right, key)
    
    return root


def find_level_and_delete(root, key, current_level=1):
    if root == None:
        return None

    if current_level == level_of_node(root, key):
        print("Elementy na poziomie {}: ".format(current_level), end=" ")
        print_nodes_at_level(root, current_level)
        print()
        root = delete_node(root, key)
        print("Węzeł o kluczu {} został usunięty".format(key))
        return root

    root.left = find_level_and_delete(root.left, key, current_level + 1)
    root.right = find_level_and_delete(root.right, key, current_level + 1)

    return root


def preorder_subtree(node):
    if node != None:
        print(node.value, end=" ")  # Wypisanie wartości bieżącego węzła
        preorder_subtree(node.left)  # Rekurencja dla lewego poddrzewa
        preorder_subtree(node.right)  # Rekurencja dla prawego poddrzewa

def height_of_subtree(node):
    if node == None:
        return 0
    else:
        # Obliczenie wysokości lewego i prawego poddrzewa
        left_height = height_of_subtree(node.left)
        right_height = height_of_subtree(node.right)
        # Zwrócenie większej wysokości z lewego i prawego poddrzewa, plus jeden dla bieżącego węzła
        return max(left_height, right_height) + 1

def delete_subtree(node):
    if node == None:
        return
    # Usunięcie lewego i prawego poddrzewa rekurencyjnie
    delete_subtree(node.left)
    delete_subtree(node.right)

    node.left = None
    node.right = None

def find_node(root, key):
    if root == None:
        return None
    if root.value == key:
        return root
    # Rekurencyjne poszukiwanie w lewym i prawym poddrzewie
    left_result = find_node(root.left, key)
    right_result = find_node(root.right, key)
    # Jeśli węzeł został znaleziony w lewym poddrzewie, zwróć wynik
    if left_result != None:
        return left_result
    # Jeśli węzeł został znaleziony w prawym poddrzewie, zwróć wynik
    if right_result != None:
        return right_result
    # Jeśli węzeł nie został znaleziony w żadnym poddrzewie, zwróć None
    return None


def rotate_right(grandparent, parent):
    grandparent.left = parent.right
    parent.right = grandparent
    return parent

def create_backbone(root):
    ptr = root
    new_root = None
    while ptr != None:
        left_child = ptr.left #Przypisanie lewgeo dziecko bieżącego węzła do zmiennej
        if left_child != None: #Sprawdzamy, czy istnieje lewe dziecko dla bieżącego węzła.
            ptr.left = left_child.right
            left_child.right = ptr
            ptr = left_child
            if new_root is None:
                new_root = ptr
        else:
            if new_root is None:
                new_root = ptr
            ptr = ptr.right
    return new_root

def create_perfect_tree(root, n): #n->liczba węzłów
    m = 2 ** (int(n ** 0.5)) - 1 #liczba węzłów, które zostaną przekształcone w drzewo optymalne 
    remaining = n - m #liczba pozostałych węzłów do przetworzenia po wyborze m węzłów

    for i in range(remaining): #dwie pętle to zmiany w drzewo optymalne
        root = rotate_right(root, root.left)
        root = root.right
    while m > 1:
        m //= 2
        root = root.right
        for i in range(m):
            root = rotate_right(root, root.left)
            root = root.right
    return root


def balance_tree(root):
    root = create_backbone(root)
    count = 0 #liczba węzłów w drzewie
    ptr = root
    while ptr != None:
        ptr = ptr.right
        count += 1
    return create_perfect_tree(root, count)







#######   TWORZENIE DRZEWA

root = None # Bieżący węzeł jakby, to taka zmienna do rekurencji
arr = [5, 3, 7, 1, 4, 6, 8]
for i in arr:
    root = insert(root, i)

# Wyświetlanie wartości drzewa w kolejności pre-order
preorder_traversal(root)



#######   MAKSYMALNE I MINIMALNE + TRASY
print()


maks=find_max(root, float('-inf'))
print(maks)
path_to_max = find_path_to_max(root, maks)

# Wydrukuj ścieżkę od korzenia do wartości maksymalnej

print("Ścieżka od korzenia do wartości maksymalnej:")
for i in path_to_max: #type: ignore
    print(i)


min_value = find_min(root, float('inf'))
print(min_value)
path_to_min = find_path_to_min(root, min_value)

print("Ścieżka od korzenia do wartości minimalnej:")
for i in path_to_min: #type: ignore
    print(i)



###########  Usuwanie elementu
print()
print()
root = find_level_and_delete(root, 5)


###### sortowanie
print()
print()
print("posortowane:")
inorder_reverse_traversal(root)
print()
print()


#######  wypisanie w porządku pre-order podrzewa, 
#ktorego korzeń (klucz) podaje użytkownik, 
#podanie wysokości tego poddrzewa, 
#a następnie usunięcie tego poddrzewa metodą post-order

key = int(input("Podaj klucz korzenia poddrzewa: "))  # Pobranie klucza korzenia od użytkownika
subtree_root = find_node(root, key)  # Znalezienie węzła o podanym kluczu
if subtree_root != None:
    print("Poddrzewo w porządku pre-order:")
    preorder_subtree(subtree_root)  # Wypisanie poddrzewa w porządku pre-order
    print("\nWysokość poddrzewa:", height_of_subtree(subtree_root))  # Obliczenie i wypisanie wysokości poddrzewa
    delete_subtree(subtree_root)  # Usunięcie poddrzewa
    print("Poddrzewo zostało usunięte.")
else:
    print("Węzeł o podanym kluczu nie istnieje.")


############# dsw(Day-Stout-Warren)

print("Wartości drzewa przed zrównoważeniem:")
preorder_traversal(root)

# Wykonaj równoważenie drzewa
root = balance_tree(root)

# Wydrukuj wartości drzewa w porządku pre-order po zrównoważeniu
print("\nWartości drzewa po zrównoważeniu:")
preorder_traversal(root)



