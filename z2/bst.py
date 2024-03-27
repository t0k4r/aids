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


def delete_subtree(root, value):
    """
    Usuwa poddrzewo o korzeniu o wartości równiej value (nie usuwa korzenia).
    """
    if root is None:
        return

    if root.left and root.left.value == value:
        # Usuwa lewe poddrzewo
        root.left = None
    elif root.right and root.right.value == value:
        # Usuwa prawe poddrzewo
        root.right = None
    else:
        # Rekurencyjnie sprawdza lewe i prawe poddrzewo
        delete_subtree(root.left, value)
        delete_subtree(root.right, value)



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


def rotate_right(node, left_child=None):
    if node is None or (left_child is None and node.left is None):
        return node
    
    if left_child is None:
        left_child = node.left
    
    new_root = left_child
    if new_root.right is not None:
        node.left = new_root.right
    else:
        node.left = None
    new_root.right = node
    return new_root


def create_backbone(root):
    new_root = None
    current = root
    prev = None
    while current is not None:
        left_child = current.left
        if left_child is not None:
            current.left = left_child.right
            left_child.right = current
            current = left_child
            if prev is None:
                new_root = current
            if prev is not None:
                prev.right = current
        else:
            prev = current
            if new_root is None:
                new_root = prev
            current = current.right
    return new_root




def create_perfect_tree(root, n):
    if n <= 1:
        return root
    m = 2 ** (int(n ** 0.5)) - 1
    remaining = n - m

    for i in range(remaining):
        if root is not None:
            root = rotate_right(root)
    while m > 1:
        m //= 2
        for i in range(m):
            root.left = rotate_right(root.left)
            root = root.right
    return root







def is_balanced(root):
    if root is None:
        return True
    left_height = height_of_subtree(root.left)
    right_height = height_of_subtree(root.right)
    return abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)



def balance_tree(root):
    while not is_balanced(root):
        root = create_backbone(root)
        count = count_nodes(root)
        root = create_perfect_tree(root, count)
    return root




class Tree():
    def __init__(self, arr: list) -> None:
        self.root: Node|None = None
        for i in arr:
            self.root = insert(self.root, i)    
    def preorder(self):
        preorder_traversal(self.root)
    def max(self):
        return find_max(self.root,self.root.value) #type: ignore
    def min(self):
        return find_min(self.root,self.root.value) #type: ignore
    def searchprint(self ,value):
        if self.root == None: raise Exception("404")
        rt = ""
        now = self.root
        while now != None:
            rt += f"Node({now.value})"
            if now.value > value:
                rt+=f".left -> "
                now = now.left
            elif now.value < value:
                rt+=f".right -> "
                now = now.right
            else:
                print(rt) 
                return
        raise Exception("404")
    def searchlevel(self,value):
        if self.root == None: return -1
        now = self.root
        i = 1
        while now != None:
            if now.value > value:
                now = now.left
            elif now.value < value:
                now = now.right
            else: 
                return i
            i+=1
        return -1
    
    def finddelete(self,value):
        print("poziom", self.searchlevel(value))
        self.root = delete_node(self.root, value)
    def desc(self):
        inorder_reverse_traversal(self.root)
    def findnode(self, value):
        return find_node(self.root, value)
    def subdelete(self, value):
        delete_subtree(self.root, value)
    def balance(self):
        self.root = balance_tree(self.root)

import time

def main():
    t = Tree([5, 3, 7, 1, 4, 6, 8])
    while True:
        c = int(input("""procedury: 
    0) exit
    1) min,max,search
    2) poziom,usuń
    3) malejąco
    4) preorder,delete
    5) równoważenie
prompt: """))
        ti = time.time()
        match c:
            case 0: break
            case 1:
                print("min: ", t.min())
                t.searchprint(t.min())
                print("max: ", t.max())
                t.searchprint(t.max())
            case 2: 
                v = int(input("value: "))
                t.finddelete(v)
            case 3:
                t.desc()
                print()
            case 4:
                v = int(input("value: "))
                preorder_traversal(t.root)
                print()
                t.subdelete(v)
                preorder_traversal(t.root)
                print()
            case 5:
                print("TODO test this!!!")
                preorder_traversal(t.root)
                print()
                t.balance()
                preorder_traversal(t.root)
                print()                
        print("took", time.time()-ti)

if __name__ == "__main__":
    main()




# #######   TWORZENIE DRZEWA

# root = None # Bieżący węzeł jakby, to taka zmienna do rekurencji
# arr = [5, 3, 7, 1, 4, 6, 8]
# for i in arr:
#     root = insert(root, i)

# # Wyświetlanie wartości drzewa w kolejności pre-order
# preorder_traversal(root)



# #######   MAKSYMALNE I MINIMALNE + TRASY
# print()


# maks=find_max(root, float('-inf'))
# print(maks)
# path_to_max = find_path_to_max(root, maks)

# # Wydrukuj ścieżkę od korzenia do wartości maksymalnej

# print("Ścieżka od korzenia do wartości maksymalnej:")
# for i in path_to_max: #type: ignore
#     print(i)


# min_value = find_min(root, float('inf'))
# print(min_value)
# path_to_min = find_path_to_min(root, min_value)

# print("Ścieżka od korzenia do wartości minimalnej:")
# for i in path_to_min: #type: ignore
#     print(i)



# ###########  Usuwanie elementu
# print()
# print()
# preorder_traversal(root)
# print()
# root = find_level_and_delete(root, 5)
# preorder_traversal(root)

# print()
# ###### sortowanie
# print()
# print()
# print("posortowane:")
# inorder_reverse_traversal(root)
# print()
# print()


# #######  wypisanie w porządku pre-order podrzewa, 
# #ktorego korzeń (klucz) podaje użytkownik, 
# #podanie wysokości tego poddrzewa, 
# #a następnie usunięcie tego poddrzewa metodą post-order
# preorder_traversal(root)
# print()
# key = int(input("Podaj klucz korzenia poddrzewa: "))  # Pobranie klucza korzenia od użytkownika
# subtree_root = find_node(root, key)  # Znalezienie węzła o podanym kluczu
# if subtree_root is not None:
#     print("Poddrzewo w porządku pre-order:")
#     preorder_subtree(subtree_root)  # Wypisanie poddrzewa w porządku pre-order
#     print("\nWysokość poddrzewa:", height_of_subtree(subtree_root))  # Obliczenie i wypisanie wysokości poddrzewa
#     delete_subtree(root, key)  # Usunięcie poddrzewa
#     print("Poddrzewo zostało usunięte.")
# else:
#     print("Węzeł o podanym kluczu nie istnieje.")

# preorder_traversal(root)

# ############# dsw(Day-Stout-Warren)

# print()
# preorder_traversal(root)
# print()

# # Wykonaj równoważenie drzewa
# root = balance_tree(root)

# # Wydrukuj wartości drzewa w porządku pre-order po zrównoważeniu
# print("wynik:")
# preorder_traversal(root)



