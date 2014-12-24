"""Given a binary tree, populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL."""
"""Initially, all next pointers are set to NULL."""
"""You may only use constant extra space. You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children)."""

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None


def connect(root):
	if root:
		if root.left:
			root.left.next = root.right
			if root.next:
				root.right.next = root.next.left
			connect(root.left)
			connect(root.right)

if __name__ == '__main__':
	root = TreeNode(1)
	connect(root)

