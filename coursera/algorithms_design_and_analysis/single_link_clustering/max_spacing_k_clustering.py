"""The goal is to code up the single link clustering algorithm using Kruskal's MST algorithm for computing a max-spacing k-clustering"""

import random

"""Union Find data structure using Lazy unions with union by rank and path compression"""
class union_find:
	def __init__(self, nodes):
		self.array = [None] * len(nodes)
		self.rank = [None] * len(nodes)
		for node in nodes:
			self.array[node-1] = node
			self.rank[node-1] = 0
	
	def union(self, node1, node2):
		leader1 = self.find(node1)
		leader2 = self.find(node2)
		if self.rank[leader1-1] < self.rank[leader2-1]:
			self.array[leader1-1] = leader2
		else:
			self.array[leader2-1] = leader1
			if self.rank[leader1-1] == self.rank[leader2-1]:
				self.rank[leader1-1] = self.rank[leader1-1] + 1

	def find(self, node):
		current_node = node
		traversed_nodes = []
		while current_node != self.array[current_node-1]:
			traversed_nodes.append(current_node)
			current_node = self.array[current_node-1]
		for node in traversed_nodes:
			self.array[node-1] = current_node
		return current_node

"""Get the graph from the file"""
def get_from_file(file_name):
	nodes = {}
	dist = []
	with open(file_name, "r") as f_open:
		number_of_nodes = f_open.next()
		for row in f_open:
			row_split = row.rstrip('\n').split()
			node1, node2, cost = int(row_split[0]), int(row_split[1]), int(row_split[2])
			nodes[node1] = True
			nodes[node2] = True
			dist.append((node1, node2, cost))
	return nodes, dist

def swap(array, i, j):
	tmp = array[i]
	array[i] = array[j]
	array[j] = tmp

def partition(edges, start_idx, end_idx):
	pivot = random.randint(start_idx, end_idx)
	swap(edges, start_idx, pivot)
	pivot_value = edges[start_idx]
	i, j = start_idx + 1, start_idx + 1
	while j<= end_idx:
		if edges[j][2] < pivot_value[2]:
			if j > i:
				swap(edges, i, j)
			i += 1
		j += 1
	swap(edges, start_idx, i-1)
	return (start_idx, i-2), (i, end_idx)

"""Quick sort"""
def sort(edges, start_idx, end_idx):
	if start_idx < end_idx:
		first_part, second_part = partition(edges, start_idx, end_idx)
		sort(edges, first_part[0], first_part[1])
		sort(edges, second_part[0], second_part[1])

"""Using Kruskal's algorithm to compute max-spacing k-clustering"""
def modified_kruskal_algorithm(nodes, nodes_dist, k):
	nodes_count = len(nodes)
	#Sort the edges by distance from smallest to largest
	sort(nodes_dist, 0, len(nodes_dist)-1)
	clusters = union_find(nodes)
	#For closest pair of nodes so far, union them if they are in different clusters
	for dist in nodes_dist:
		if clusters.find(dist[0]) == clusters.find(dist[1]):
			continue
		else:
			if nodes_count == k:
				max_spacing = dist[2]
				break
			clusters.union(dist[0], dist[1])
			nodes_count = nodes_count - 1
	return clusters, max_spacing

def main(k):
	file_name = "Nodes.txt"
	nodes, nodes_distances = get_from_file(file_name)
	clusters, max_spacing = modified_kruskal_algorithm(nodes, nodes_distances, k)
	print max_spacing

if __name__ == '__main__':
	main(k=4)
