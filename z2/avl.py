def main():
    t= Tree()
    t.build([8, 2, 5, 14, 10, 12, 13, 6, 9])
    t.search(12)
    # t.deletesubtree(9)
    # inorder(t.root)



class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left: Node|None = None
        self.right: Node|None = None
    
    def add(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.add(value)


class Tree:
    def __init__(self) -> None:
        self.root: Node|None = None

    def build(self, arr: list):
        arr.sort()
        i = len(arr)//2
        mean = arr[i]
        self.add(mean)
        larr = arr[0:i]
        rarr = arr[i+1:len(arr)]
        while len(larr) != 0:
            i = len(larr)//2
            if len(larr)%2==0: i-=1
            self.add(larr.pop(i))
        while len(rarr) != 0:
            i = len(rarr)//2
            if len(rarr)%2==0: i-=1
            self.add(rarr.pop(i))

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.add(value)
    
    def min(self):
        now = self.root
        if now == None: raise Exception("empty")
        while now.left != None:  
            now = now.left 
        return now.value 
    
    def delete(self, value):
        pass

    def deletesubtree(self, value):
        if self.root == None: raise Exception("404")
        prev: Node|None = None
        now = self.root
        while now != None:
            if now.value > value:
                prev = now
                now = now.left
            elif now.value < value:
                prev = now
                now = now.right
            else: 
                if prev == None: 
                    self.root = None
                    return
                if prev.left.value == now.value: #type: ignore
                    prev.left = None
                else:
                    prev.right = None
                return
        raise Exception("404")
    
    def balance(self, value):
        pass


    def search(self, value):
        if self.root == None: return False
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
                break
        else:
            return False
        print(rt)
        return True

    def searchnode(self, value):
        pass
        if self.root == None: raise Exception("404")
        now = self.root
        while now != None:
            if now.value > value:
                now = now.left
            elif now.value < value:
                now = now.right
            else: 
                return now
        raise Exception("404")

    def searchlevel(self,value):
        if self.root == None: return -1
        rt = ""
        now = self.root
        i = 0
        while now != None:
            if now.value > value:
                now = now.left
            elif now.value < value:
                now = now.right
            else: 
                break
            i+=1
        else:
            return -1
        return i
    
    def max(self):
        now = self.root
        if now == None: raise Exception("empty")
        while now.right != None:
            now = now.right 
        return now.value

    def height(self):
        pass

def printlevel(root: Node|None, level: int, now: int):
    if root == None: return
    if now < level:
        printlevel(root.left, level, now+1)
        printlevel(root.right, level, now+1)
    elif now == level:
        print(root.value, end=", ")

def preorder(root: Node|None):
    if root == None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def inorder(root: Node|None):
    if root == None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def inorderdesc(root: Node|None):
    if root == None:
        return
    inorderdesc(root.right)
    print(root.value)
    inorderdesc(root.left)


def postorder(root: Node|None):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)

    
if __name__ == "__main__":
    main()