"""Use Prim's greedy algorithm to compute a minimum spanning tree from an undirected graph"""

import time

"""A minimum heap class to extract minimum and update keys"""
class Min_heap:
	def __init__(self, init_node, nodes, graph):
		self.graph = graph
		self.heap = []
		self.position = {}
		idx = 0
		for node in nodes:
			self.heap.append((None, node, float('inf')))
			self.position[node] = idx
			idx += 1
		for element in graph[init_node]:
			node, length = element[0], element[1]
			self.heap[self.position[node]] = (init_node, node, length)
		self.heapify()

	def heapify(self):
		length = len(self.heap)
		idx = length/2 - 1
		while idx >= 0:
			self.bubble_down(idx, length-1)
			idx = idx - 1
	
	def extract_min(self):
		length = len(self.heap)
		self.swap(0, length-1)
		min_node = self.heap.pop()
		del self.position[min_node[1]]
		self.bubble_down(0, length-2)
		self.update_key(min_node[1])
		return min_node

	def update_key(self, node):
		existing_nodes = self.position.keys()
		for element in self.graph[node]:
			if element[0] in existing_nodes:
				if element[1] < self.heap[self.position[element[0]]][2]:
					self.heap[self.position[element[0]]] = (node, element[0], element[1])
					self.bubble_up(self.position[element[0]], 0)

	def bubble_down(self, start_idx, end_idx):
		left_child_idx = 2*start_idx + 1
		right_child_idx = 2*start_idx + 2
		min_idx = start_idx
		if left_child_idx <= end_idx and self.heap[left_child_idx][2] < self.heap[min_idx][2]:
			min_idx = left_child_idx
		if right_child_idx <= end_idx and self.heap[right_child_idx][2] < self.heap[min_idx][2]:
			min_idx = right_child_idx
		if min_idx != start_idx:
			self.swap(start_idx, min_idx)
			self.bubble_down(min_idx, end_idx)

	def bubble_up(self, start_idx, end_idx):
		parent_idx = (start_idx+1)/2 - 1
		if parent_idx >= end_idx and self.heap[start_idx][2] < self.heap[parent_idx][2]:
			self.swap(start_idx, parent_idx)
			self.bubble_up(parent_idx, end_idx)

	def swap(self, idx1, idx2):
		tmp = self.heap[idx1]
		self.heap[idx1] = self.heap[idx2]
		self.heap[idx2] = tmp
		self.position[self.heap[idx1][1]] = idx1
		self.position[self.heap[idx2][1]] = idx2

"""Get the graph from a file"""
def get_graph(file_name):
	graph = {}
	with open(file_name, 'r') as f_open:
		graph_metadata = f_open.next()
		for row in f_open:
			row_split = row.rstrip('\n').split()
			first_node, second_node, length = row_split[0], row_split[1], int(row_split[2])
			graph.setdefault(first_node, []).append((second_node, length))
			graph.setdefault(second_node, []).append((first_node, length))
	return graph

"""Prim's greedy algorithm"""
def prim_algorithm(graph):
	nodes = graph.keys()
	init_node = nodes[0]
	node_heap = Min_heap(init_node, nodes[1:], graph)
	overall_cost = 0
	nodes_used = [init_node]
	minimum_spanning_tree = []
	while len(nodes_used) < len(nodes):
		min_node = node_heap.extract_min()
		start_node, target_node, cost = min_node[0], min_node[1], min_node[2]
		if cost == float("inf"):
			break
		nodes_used.append(target_node)
		minimum_spanning_tree.append((start_node, target_node))
		overall_cost += cost
	return minimum_spanning_tree, overall_cost
	
"""Main function"""
def main():
	file_name = "UndirectedGraph.txt"
	graph = get_graph(file_name)
	MST, overall_cost = prim_algorithm(graph)
	print overall_cost


if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time()-start_time, "seconds"
