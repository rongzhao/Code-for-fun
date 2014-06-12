"""Code up and run Dijkstra's shortest-path algorithm on an undirected weighted graph, using 1 (the first vertex) as the source vertex, and to compute the shortest-path distances between 1 and every other vertex of the graph. If there is no path between a vertex v and vertex 1, the shortest-path distance between 1 and v will be 1000000. """

import time

"""A heap data structure that stores the shortest distances between 1 and other nodes in the graph"""
class heap:
	def __init__(self, graph, source):
		pos_idx = 0
		#Create an arbitrary heap along with a corresponding mapping between vertex and its position in the heap
		self.position = {}
		self.heap = []
		for node in graph:
			if node != source:
				self.position[node] = pos_idx
				# Each key in the heap is a tuple of vertex and its shortest distance from 1
				self.heap.append((node, 1000000))
				pos_idx += 1
		#Given the source vertex, update the shortest distances of some vertices that connect to the source vertex
		for entry in graph[source]:
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
	def recauclate_score(self, edges, node_dist):
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

"""Dijkstra's shortest path algorithm"""
def dijkstra_shortest_path_algorithm(graph, source):
	#A dictionary to store the shortest path distances of all nodes in the graph
	shortest_path_distance = {source:0}
	min_heap = heap(graph, source)
	while True:
		#For each loop, we compute the shortest path distance of one single node in the graph
		node, dist = min_heap.extract_min()
		shortest_path_distance[node] = dist
		if dist >= 1000000 or len(shortest_path_distance) == len(graph):
			break
		min_heap.recauclate_score(graph[node], dist)
	#Update the distances of some nodes unreachable by source vertex to 1000000
	for node in graph:
		if node not in shortest_path_distance:
			shortest_path_distance[node] = 1000000
	return shortest_path_distance

"""Get the graph from a file"""
def get_graph(file_name):
	graph = {}
	with open(file_name, 'r') as f_open:
		for line in f_open:
			line_splitted = [entry.rstrip('\n') for entry in line.split()]
			graph[line_splitted[0]] = [(entry.split(',')[0], int(entry.split(',')[1])) for entry in line_splitted[1:]]
	return graph

"""Main function"""
def main():
	file_name = "UndirectedWeightedGraph.txt"
	graph = get_graph(file_name)
	source = '1'
	shortest_path_distance = dijkstra_shortest_path_algorithm(graph, source)
	dist = []
	for node in [7,37,59,82,99,115,133,165,188,197]:
		print "distance from 1 to %s is: " % str(node), shortest_path_distance[str(node)]
		dist.append(str(shortest_path_distance[str(node)]))
	print ','.join(dist)


if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time()-start_time, "seconds"
