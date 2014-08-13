"""The goal is to compute the "shortest shortest path" for three graphs. Precisely, we must first identify which, if any, of the three graphs have no negative cycles. For each such graph, we should compute all-pairs shortest paths and remember the smallest length of the paths."""

import time

class heap:
	def __init__(self, source, node_count, neighbors):
		pos_idx = 0
		#Create an arbitrary heap along with a corresponding mapping between vertex and its position in the heap
		self.position = {}
		self.heap = []
		for node in xrange(1, node_count+1):
			if node != source:
				self.position[node] = pos_idx
				# Each key in the heap is a tuple of vertex and its shortest distance from 1
				self.heap.append((node, float("inf")))
				pos_idx += 1
		#Given the source vertex, update the shortest distances of some vertices that connect to the source vertex
		for entry in neighbors:
			vertex = entry[0]
			edge_length = entry[1]
			self.heap[self.position[vertex]] = entry 
		#This variable is to keep track of the number of nodes left in the heap
		self.left_nodes_count = len(self.heap)
		#Initialize the heap with heap properties
		self.heapify()

	#Initialize the heap
	def heapify(self):
		last_idx = len(self.heap) - 1
		parent_idx = (last_idx + 1)/2 - 1
		while parent_idx >= 0:
			self.bubble_down(parent_idx, last_idx)
			parent_idx = parent_idx - 1

	#Update the shortest distances of some vetices that connect to the vertex just extracted
	def update_score(self, edges, node_dist):
		for entry in edges:
			vertex, edge_length = entry[0], entry[1]
			if vertex in self.position:
				dijkstra_greedy_score = node_dist + edge_length
				vertex_idx = self.position[vertex]
				if self.heap[vertex_idx][1] > dijkstra_greedy_score:
					self.heap[vertex_idx] = (vertex, dijkstra_greedy_score)
					self.bubble_up(vertex_idx)

	#Swap two vertices in heap
	def swap(self, idx1, idx2):
		self.position[self.heap[idx1][0]] = idx2
		self.position[self.heap[idx2][0]] = idx1
		self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

	#Extract the root node from the heap
	def extract_min(self):
		last_idx = self.left_nodes_count - 1
		self.swap(0, last_idx)
		self.left_nodes_count -= 1
		self.bubble_down(0, self.left_nodes_count - 1)
		del self.position[self.heap[last_idx][0]]
		return self.heap[last_idx] 

	#Bubble up the target node recursively
	def bubble_up(self, target_idx):
		parent_idx = (target_idx + 1)/2 - 1
		if parent_idx >= 0 and self.heap[parent_idx][1] > self.heap[target_idx][1]:
			self.swap(parent_idx, target_idx)
			self.bubble_up(parent_idx)

	#Bubble down the target node recursively
	def bubble_down(self, target_idx, end_idx):
		left_child_idx = 2 * target_idx + 1
		right_child_idx = 2* target_idx + 2
		min_value = self.heap[target_idx][1]
		min_idx = target_idx
		if left_child_idx <= end_idx and self.heap[left_child_idx][1] < min_value:
			min_value = self.heap[left_child_idx][1]
			min_idx = left_child_idx
		if right_child_idx <= end_idx and self.heap[right_child_idx][1] < min_value:
			min_value = self.heap[right_child_idx][1]
			min_idx = right_child_idx
		if min_idx != target_idx:
			self.swap(target_idx, min_idx)
			self.bubble_down(min_idx, end_idx)

"""Bellman Ford algorithm"""
def bellman_ford(s, graph, node_count):
	#Initialize base case
	new_array = [None] * (node_count+1)
	for node in xrange(node_count+1):
		if node == s:
			new_array[node] = 0
		else:
			new_array[node] = float("inf")
	#Loop over the constraints of # of edges that can be used to compute the shortest path
	for i in xrange(node_count+1):
		current_array = new_array
		new_array = [None] * (node_count+1)
		#Compute shortest paths for all vertices in this iteration
		for node in xrange(node_count+1):
			optimal_dist = current_array[node]
			for neighbor in graph.get(node, []):
				dist = current_array[neighbor[0]] + neighbor[1]
				if dist < optimal_dist:
					optimal_dist = dist
			new_array[node] = optimal_dist
		if current_array == new_array:
			break
	if current_array != new_array:
		return None
	else:
		return new_array

"""Floyd Warshall algorithm"""
def floyd_warshall(node_count, edges):
	#Initialize base case
	new_array = np.zeros((node_count+1, node_count+1))
	new_array = [[]]
	for i in xrange(1, node_count+1):
		sub_array = [None]
		for j in xrange(1, node_count+1):
			if i == j:
				sub_array.append(0)
			elif (i, j) in edges:
				sub_array.append(edges[(i, j)])
			else:
				sub_array.append(float("inf"))
		new_array.append(sub_array)
	#Loop over the constraints of first # vertices that can be used as internal nodes to compute the shortest path
	for k in xrange(1, node_count+1):
		current_array = new_array
		new_array = [[]]
		#Compute shortest paths for all-pairs in this iteration
		for i in xrange(1, node_count+1):
			sub_array = [None]
			for j in xrange(1, node_count+1):
				optimal_dist = current_array[i][j]
				dist = current_array[i][k] + current_array[k][j]
				if dist < optimal_dist:
					optimal_dist = dist
				sub_array.append(optimal_dist)
			new_array.append(sub_array)
	for i in xrange(1, node_count+1):
		if new_array[i][i] < 0:
			return None
	return new_array

"""Get the graph from a file as an adjacency list"""
def get_graph(file_name):
	graph, edges, graph_updated, nodes = {}, {}, {}, {}
	with open(file_name, "rb") as f_open:
		meta_data = f_open.next()
		node_count = int(meta_data.split()[0])
		for row in f_open:
			row_split = row.rstrip('\n').split()
			tail, head, edge_cost = int(row_split[0]), int(row_split[1]), int(row_split[2])
			edges[(tail, head)] = edge_cost
			graph.setdefault(head, []).append((tail, edge_cost))
			graph_updated.setdefault(head, []).append((tail, edge_cost))
			nodes[tail] = True
			nodes[head] = True
	for node in nodes:
		graph_updated.setdefault(node, []).append((0, 0))
	return graph, graph_updated, edges, node_count

"""A modified version of Dijkstra's algorithm"""
def modified_dijkstra(vertex_weight, edges, node_count):
	graph = {}
	#Make all edge-costs positive by adding the difference between weight of tail and weight of head
	for edge in edges:
		tail, head = edge[0], edge[1]
		edge_cost = edges[edge]
		new_edge_cost = edge_cost + vertex_weight[tail] - vertex_weight[head]
		graph.setdefault(tail, []).append((head, new_edge_cost))
	#Compute shortest paths using Dijkstra's algorithm
	array = [[]]
	for i in xrange(1, node_count+1):
		sub_array = [float("inf")]*(node_count+1)
		min_heap = heap(i, node_count, graph.get(i, []))
		for j in xrange(node_count):
			node, min_len = min_heap.extract_min()
			sub_array[node] = min_len
			if min_len == float("inf"):
				break
			min_heap.update_score(graph.get(node, []), min_len)
		array.append(sub_array)
	#Subtract the difference back off to compute the real shortest paths between pairs of vertices
	for i in xrange(1, node_count+1):
		for j in xrange(1, node_count+1):
			array[i][j] = array[i][j] - vertex_weight[i] + vertex_weight[j]
	return array

"""Johnson's algorithm to compute all-pairs shortest-paths"""
def main_Johnson():
	file_names = ["g1.txt", "g2.txt", "g3.txt"]
	#file_names = ["test.txt"]
	min_values = []
	for file_name in file_names:
		graph, graph_updated, edges, node_count = get_graph(file_name)
		#Run Bellman Ford algorithm once on the graph with extra one virtual source
		quick_result = bellman_ford(0, graph_updated, node_count)
		#If negavite cost cycle is found, return infinite
		if quick_result == None:
			print "Negative Cycle Found!"
			min_values.append(float("inf"))
		#If no negative cost cycle is found, use the output of Bellman Ford as vertex weight and feed it into the modified Dijkstra's algorithm
		else:
			print "min:", min(quick_result[1:])
			vertex_weight = quick_result
			result = modified_dijkstra(vertex_weight, edges, node_count)
			min_value = float("inf")
			for i in xrange(1, node_count+1):
				for j in xrange(1, node_count+1):
					if result[i][j] < min_value and i!= j:
						min_value = result[i][j]
			min_values.append(min_value)
		print "one graph completes"
	print min_values

"""Floyd Warshall algorithm plus Bellman Ford algorithm to compute all-pair shortest-paths"""
def main_Floyd_Warshall():
	file_names = ["g1.txt", "g2.txt", "g3.txt"]
	#file_names = ["test.txt"]
	min_values = []
	for file_name in file_names:
		graph, graph_updated, edges, node_count = get_graph(file_name)
		#Run Bellman Ford algorithm once on the graph with one extra virtual source
		quick_result = bellman_ford(0, graph_updated, node_count)
		#If negative cost cycle is found, return infinite
		if quick_result == None:
			print "Negative Cycle Found!"
			min_values.append(float("inf"))
		#If no negative cost cycle is found, use Floyd Warshall algorithm to compute all-pair shortest paths
		else:
			print min(quick_result[1:])
			result = floyd_warshall(node_count, edges)
			#print quick_result
			#print result
			min_value = float("inf")
			for i in xrange(1, node_count+1):
				for j in xrange(1, node_count+1):
					if result[i][j] < min_value and i!= j:
						min_value = result[i][j]
			min_values.append(min_value)
		print "one graph completes"
	print min_values

if __name__ == '__main__':
	start_time = time.time()
	main_Floyd_Warshall()
	main_Johnson()
	print time.time()-start_time, "seconds"

