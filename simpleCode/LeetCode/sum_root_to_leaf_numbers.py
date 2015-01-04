"""Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number."""
"""An example is the root-to-leaf path 1->2->3 which represents the number 123"""
"""Find the total sum of all root-to-leaf numbers."""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def sumNumbers(root):
	total_sum = DFS(root, 0)
	return total_sum

def DFS(node, parent_value):
	if node:
		current_value = parent_value*10 + node.val
		if node.left or node.right:
			return DFS(node.left, current_value) + DFS(node.right, current_value)
		else:
			return current_value
	else:
		return 0

if __name__ == '__main__':
	node = TreeNode(5)
	node.left = TreeNode(2)
	node.right = TreeNode(3)
	node.right.right = TreeNode(1)
	print sumNumbers(node)
