import time
import avl
def testavl(arr:list):
    print("AVL")
    arr.sort()
    t = avl.Tree(arr)
    ti = time.time()
    t.min()
    print("min", time.time()-ti)
    ti = time.time()
    t.max()
    print("max", time.time()-ti)

import bst
def testbst(arr):
    print("BST")
    t = bst.Tree(arr)
    ti = time.time()
    t.min()
    print("min", time.time()-ti)
    ti = time.time()
    t.max()
    print("max", time.time()-ti)
    ti = time.time()
    t.balance()
    print("balansowanie", time.time()-ti)

import inp
def main():
    testavl(inp.rand(15))
    testbst(inp.rand(15))


if __name__ == "__main__":
    main()