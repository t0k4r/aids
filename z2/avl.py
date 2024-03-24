def main():
    t= Tree()
    t.build([8, 2, 5, 14, 10, 12, 13, 6, 9])
    print(t)
    pass

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
        larr = arr[0:i-1]
        rarr = arr[i+1:len(arr)-1]
        while len(larr) != 0:
            self.add(larr.pop(len(larr)//2))
        while len(rarr) != 0:
            self.add(rarr.pop(len(rarr)//2))

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
    
    def minroute(self):
        pass
    
    def max(self):
        now = self.root
        if now == None: raise Exception("empty")
        while now.right != None:
            now = now.right 
        return now.value
    
    def maxroute(self):
        pass
    
    def height(self):
        pass

    
if __name__ == "__main__":
    main()