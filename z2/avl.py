def deletenode(root, key):
    if root == None:
        return root
    if root.value == key and root.left == None and root.right == None:
        return None

    if root.value == key and root.left == None:
        return root.right
    if root.value == key and root.right == None:
        return root.left
    if root.value == key:
        successor = treemin(root.right)
        root.right = deletenode(root.right, successor)
        root.value = successor
    
    root.left = deletenode(root.left, key)
    root.right = deletenode(root.right, key)

    return root

def deletesubtree(root, value):
    if root == None:
        return
    if root.left and root.left.value == value:
        root.left = None
    elif root.right and root.right.value == value:
        root.right = None
    else:
        deletesubtree(root.left, value)
        deletesubtree(root.right, value)

class Node():
    def __init__(self, value):
        self.value = value
        self.left: Node|None = None
        self.right: Node|None = None
        self.height: int = 1

def treebuild(root: Node|None, sorted: list, height=1) -> Node|None:
    if len(sorted) == 0: return root
    i = len(sorted)//2
    if len(sorted)%2==0: i-=1
    root = Node(sorted[i])
    root.height = height
    root.left = treebuild(root.left, sorted[0:i], height+1)
    root.right = treebuild(root.right, sorted[i+1:len(sorted)], height+1)
    return root


def treesearchprint(root:Node|None ,value):
    if root == None: raise Exception("404")
    rt = ""
    now = root
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

def treesubtree(root: Node|None, value):
    if root == None: raise Exception("404")
    now = root
    while now != None:
        if now.value > value:
            now = now.left
        elif now.value < value:
            now = now.right
        else:
            return now
    raise Exception("404")

def treegetlevel(root: Node|None, height:int)->list:
    values = []
    if root == None: pass
    elif root.height < height:
        values.extend(treegetlevel(root.left, height))
        values.extend(treegetlevel(root.right, height))
    elif root.height == height:
        values.append(root.value)     
    return values

def treemin(root:Node|None):
    now = root
    if now == None: raise Exception("empty")
    while now.left != None:
        now = now.left 
    return now.value

def treemax(root:Node|None):
    now = root
    if now == None: raise Exception("empty")
    while now.right != None:
        now = now.right 
    return now.value

def preorder(root: Node|None):
    if root == None:
        return
    print(root.value,  end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root: Node|None):
    if root == None:
        return
    inorder(root.right)
    print(root.value)
    inorder(root.left)

def inorderdesc(root: Node|None):
    if root == None:
        return
    inorderdesc(root.right)
    print(root.value, end=" ")
    inorderdesc(root.left)

def treedeletenode(root: Node|None, value):
    if root == None: return None
    elif root.value == value and root.left == None and root.right == None:
        return None
    elif root.value == value and root.left == None and root.right != None:
        return root.right
    elif root.value == value and root.left != None and root.right == None:
        return root.left
    elif root.value == value:
        return None
    else:
        return root
def treedeletesubtree(root: Node|None, value):
    pass
def treebalance(root: Node|None):
    pass

import dsw

import bst

class Tree():
    def __init__(self, sorted:list) -> None:
        self.root = treebuild(None, sorted)
    def max(self):
        return treemax(self.root)
    def min(self):
        return treemin(self.root)
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
    def finddelete(self, value):
        i = self.searchlevel(value)
        print("poziom", i )
        bst.print_nodes_at_level(self.root, i)
        self.root = deletenode(self.root, value)
        self.balance()
    def desc(self):
        inorderdesc(self.root)
    def subdelete(self, value):
        deletesubtree(self.root, value)
        self.balance()
    def balance(self):
        self.root = treebuild(None, inorderlist(self.root))
        
def inorderlist(root: Node|None):
    arr = []
    if root == None:
        return arr
    arr.extend(inorderlist(root.left))
    arr.append(root.value)
    arr.extend(inorderlist(root.right))
    return arr

def main():
    t = Tree(sorted([8, 2, 5, 14, 10, 12, 13, 6, 9]))
    while True:
        c = int(input("""procedury: 
    0) exit
    1) min,max,search
    2) poziom,usuń
    3) malejąco
    4) preorder,delete
prompt: """))
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
                preorder(t.root)
                print()
                t.subdelete(v)
                preorder(t.root)
                print()



if __name__ == "__main__":
    main()