"""Given an array where elements are sorted in ascending order, convert it to a height balanced BST."""

# Definition for a binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Top down approach to build a BST
def buildBST(num, start, end):
	if start > end:
		return None
	middle = start + (end-start)/2
	root = TreeNode(num[middle])
	root.left = buildBST(num, start, middle-1)
	root.right = buildBST(num, middle+1, end)
	return root

def sortedArrayToBST(num):
	n = len(num)
	return buildBST(num, 0, n-1)

if __name__ == '__main__':
	num = []
	root = sortedArrayToBST(num)
