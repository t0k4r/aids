# Python code to balance BST using DSW algorithm
import math



def bsttolist(grand) -> int:
	count = 0
	tmp = grand.right
	while tmp:
		if tmp.left:
			oldTmp = tmp
			tmp = tmp.left
			oldTmp.left = tmp.right
			tmp.right = oldTmp
			grand.right = tmp
		else:
			count += 1
			grand = tmp
			tmp = tmp.right
	return count

def unwind(grand, m: int):
	tmp = grand.right
	for i in range(m):
		oldTmp = tmp
		tmp = tmp.right
		grand.right = tmp
		oldTmp.right = tmp.left
		tmp.left = oldTmp
		grand = tmp
		tmp = tmp.right

import bst
def balanceBST(root):
	dummy = bst.Node(0)
	dummy.right = root
	count = bsttolist(dummy)

	# get the height of tree in which all levels are completely filled
	h = int(math.log2(count + 1))
	# get number of nodes until second last level
	m = pow(2, h) - 1

	unwind(dummy, count - m)


	for m in [m // 2**i for i in range(1, h + 1)]:
		unwind(dummy, m)
	return dummy.right
