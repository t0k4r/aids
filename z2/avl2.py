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

def treemax(root:Node|None):
    now = root
    if now == None: raise Exception("empty")
    while now.left != None:
        now = now.left 
    return now.value

def treemin(root:Node|None):
    now = root
    if now == None: raise Exception("empty")
    while now.right != None:
        now = now.right 
    return now.value

def preorder(root: Node|None):
    if root == None:
        return
    print(root.value)
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
    print(root.value)
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


class Tree():
    def __init__(self, sorted:list) -> None:
        self.root = treebuild(None, sorted)
    def max(self):
        return treemax(self.root)
    def min(self):
        return treemin(self.root)



def main():
    root = None
    arr = [8, 2, 5, 14, 10, 12, 13, 6, 9]
    arr.sort()
    root = treebuild(root, arr)
    treesearchprint(root, 14)
    print(treegetlevel(root, 2))

if __name__ == "__main__":
    main()