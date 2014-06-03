"""Computing strongly connected components in a directed graph using Kosaraju's Two-Pass Algorithm (Two DFS)"""


import time
import numpy as np

#global variable to keep track of strongly connected components
leader = None
#global variable to keep track of visited nodes in DFS 
visited = {}

"""simple merge sort to do the sorting"""
def merge_sort(ls):
	length = len(ls)
	if length < 2:
		return ls
	first_part = merge_sort(ls[:length/2])
	second_part = merge_sort(ls[length/2:])
	new_list = []
	i, j = 0, 0
	while i < len(first_part) and j < len(second_part):
		if first_part[i] > second_part[j]:
			new_list.append(first_part[i])
			i += 1
		else:
			new_list.append(second_part[j])
			j += 1
	while i < len(first_part):
		new_list.append(first_part[i])
		i += 1
	while j < len(second_part):
		new_list.append(second_part[j])
		j += 1
	return new_list

"""First DFS to get the ordering of the nodes for second DFS"""
def dfs_first(graph, vertex, finishing_time):
	#use stack to achieve DFS
	stack = []
	stack.append(vertex)
	visited[vertex] = 1
	while stack:
		node = stack[-1]
		#visited node has two status 1 and 2. Status 1 is for bookkeeping explored nodes and status 2 is for computing ordering of the nodes
		if visited[node] == 2:
			finishing_time.append(node)
			stack.pop()
		else:
			visited[node] = 2
			for neighbor in graph[node]:
				if visited[neighbor] == 0:
					stack.append(neighbor)
					visited[neighbor] = 1

"""Second DFS to compute SCC"""
def dfs_second(graph, vertex, scc):
	stack = []
	stack.append(vertex)
	visited[vertex] = 1
	while stack:
		node = stack.pop()
		scc.setdefault(leader, []).append(node)
		for neighbor in graph[node]:
			if visited[neighbor] == 0:
				stack.append(neighbor)
				visited[neighbor] = 1

"""Get the sizes of the five largest SCCs in decreasing order"""
def largest_five_count(scc):
	sizes = np.zeros(len(scc))
	idx = 0
	for leader in scc:
		sizes[idx] = len(scc[leader])
		idx += 1
	sizes_in_order = merge_sort(sizes)
	return sizes_in_order[:5]

"""Kosaraju Two-Pass Algorithm"""
def find_scc(graph, graph_reversed):
	#first pass of DFS to compute finishing time of the nodes
	for node in graph_reversed:
		visited[node] = 0
	finishing_time = []
	for node in graph_reversed:
		if visited[node] == 0:
			dfs_first(graph_reversed, node, finishing_time)
	#second pass of DFS to compute SCCs
	for node in graph:
		visited[node] = 0
	scc = {}
	global leader
	vertices_count = len(finishing_time)
	#traverse the nodes from largest finishing time to smallest
	for idx in xrange(vertices_count):
		node = finishing_time[vertices_count-1-idx]
		if visited[node] == 0:
			leader = node
			dfs_second(graph, node, scc)
	return scc

"""Get the graph and its reversed graph from a file"""
def get_graph(file_name):
	graph, graph_reversed = {}, {}
	f_open = open(file_name, "r")
	for edge in f_open:
		edge_splitted = [e.strip('\n') for e in edge.split()]
		node1, node2 = edge_splitted[0], edge_splitted[1]
		graph.setdefault(node1, []).append(node2)
		graph.setdefault(node2,[])
		graph_reversed.setdefault(node2, []).append(node1)
		graph_reversed.setdefault(node1, [])
	f_open.close()
	return graph, graph_reversed

"""Main function"""
def main():
	file_name = "DirectedGraph.txt"
	#file_name = "test.txt"
	graph, graph_reversed = get_graph(file_name)
	scc = find_scc(graph, graph_reversed)
	sizes_of_five_largest_scc = largest_five_count(scc)
	print [int(e) for e in sizes_of_five_largest_scc]

if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time() - start_time, "seconds"
