class Node():
    def __init__(self, value):
        self.value = value
        self.left: Node|None = None
        self.right: Node|None = None
        self.height = 1

def treebuild(root: Node|None, sorted: list, height=1) -> Node|None:
    if len(sorted) == 0: return root
    i = len(sorted)//2
    if len(sorted)%2==0: i-=1
    root = Node(sorted[i])
    root.height = height
    root.left = treebuild(root.left, sorted[0:i], height+1)
    root.right = treebuild(root.right, sorted[i+1:len(sorted)], height+1)
    return root

def treegetmin(root: Node|None)-> Node:
    if root == None:
        raise Exception("404")
    elif root.left == None:
        return root
    return treegetmin(root.left)

def treegetheight(root):
    if root == None:
        return 0
    return root.height

def treegetbalance(root):
    if root == None:
        return 0
    return treegetheight(root.left) - treegetheight(root.right)

def treedelete(root: Node|None, value):
    if root == None:
        return root

    elif value < root.value:
        root.left = treedelete(root.left, value)
    elif value > root.value:
        root.right = treedelete(root.right, value)
    else:
        if root.left == None:
            ret = root.right
            root = None
            return ret

        elif root.right == None:
            ret = root.left
            root = None
            return ret

        min = treegetmin(root.right)
        root.value = min.value 
        root.right = treedelete(root.right,min.value)

    if root == None:
        return root

    root.height = 1 + max(treegetheight(root.left),treegetheight(root.right))

    balance = treegetbalance(root)
    if balance > 1 and treegetbalance(root.left) >= 0:
        return treerightrotate(root)
    if balance < -1 and treegetbalance(root.right) <= 0:
        return treeleftrotate(root)
    if balance > 1 and treegetbalance(root.left) < 0:
        root.left = treeleftrotate(root.left)
        return treerightrotate(root)
    if balance < -1 and treegetbalance(root.right) > 0:
        root.right = treerightrotate(root.right)
        return treeleftrotate(root)

    return root

def treeleftrotate(z):
    y = z.right
    t = y.left
    y.left = z
    z.right = t
    z.height = 1 + max(treegetheight(z.left), treegetheight(z.right))
    y.height = 1 + max(treegetheight(y.left), treegetheight(y.right))
    return y

def treerightrotate(z):
    y = z.left
    t = y.right
    y.right = z
    z.left = t
    z.height = 1 + max(treegetheight(z.left),treegetheight(z.right))
    y.height = 1 + max(treegetheight(y.left),treegetheight(y.right))
    return y

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

def inorderdesc(root: Node|None):
    if root == None:
        return
    inorderdesc(root.right)
    print(root.value, end=" ")
    inorderdesc(root.left)

class Tree(object):
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
        print("poziom", self.searchlevel(value))
        self.root = treedelete(self.root, value)
    def desc(self):
        inorderdesc(self.root)
    def subdelete(self, value):
        pass


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
                preorder(t.root)
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