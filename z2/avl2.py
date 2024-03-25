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
    print("left",sorted[0:i],"rigth",sorted[i+1:len(sorted)] )
    root.left = treebuild(root.left, sorted[0:i], height+1)
    root.right = treebuild(root.right, sorted[i+1:len(sorted)], height)
    return root

def treesearch(root ,value):
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

def treesubtree(root, value):
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

def treemax(root):
    now = root
    if now == None: raise Exception("empty")
    while now.left != None:
        now = now.left 
    return now.value

def treemin(root):
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




def main():
    root = None
    arr = [8, 2, 5, 14, 10, 12, 13, 6, 9]
    arr.sort()
    root = treebuild(root, arr)
    treesearch(root, 13)

if __name__ == "__main__":
    main()