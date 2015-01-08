"""Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST."""

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		
# Get the length of the linked list
def length_count(head):
	count = 0
	while head:
		count += 1
		head = head.next
	return count

# Bottom-up approach to build Binary Search Tree by accessing the nodes in the order of the list
def buildBST(list_node, start, end):
	if start > end:
		return None
	middle = start + (end-start)/2
	left_child = buildBST(list_node, start, middle-1)
	root = TreeNode(list_node.next.val)
	list_node.next = list_node.next.next
	root.left = left_child
	root.right = buildBST(list_node, middle+1, end)
	return root

# Main function to convert a sorted linked list into a balanced BST
def sortedListToBST(head):
	list_node = ListNode(None)
	list_node.next = head
	n = length_count(head)
	return buildBST(list_node, 0, n-1)

if __name__ == '__main__':
	head = ListNode(0)
	root = sortedListToBST(head)
