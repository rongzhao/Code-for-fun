"""Given input of an adjacency list representation of an undirected graph, use random contraction algorithm to find min cuts"""

from random import shuffle
import time

"""Choose an edge uniformly at random"""
def random_choose_edge(shuffled_edges, random_edge_idx, super_node_mapping):
	while True:
		#Get the edge from the shuffled edge list with index.
		edge_picked = shuffled_edges[random_edge_idx]
		#If it's self-edge, skip and get next edge in the list
		if edge_picked[1] not in super_node_mapping[edge_picked[0]]:
			break
		else:
			random_edge_idx += 1
	return edge_picked, random_edge_idx+1


"""Do nodes contraction"""
def contract(edge_picked, super_node_mapping):
	u, v = edge_picked[0], edge_picked[1]
	super_node_u = super_node_mapping[u]
	super_node_v = super_node_mapping[v]
	#Update the supernode set u and v belong to
	if len(super_node_u) < len(super_node_v):
		super_node_v.update(super_node_u)
		for node in super_node_u:
			super_node_mapping[node] = super_node_v
	else:
		super_node_u.update(super_node_v)
		for node in super_node_v:
			super_node_mapping[node] = super_node_u


"""Run random contraction algorithms"""
def random_contraction(graph, edges):
	#Shuffle the edge list to achieve randomness
	shuffled_edges = edges[:]
	shuffle(shuffled_edges) 
	random_edge_idx = 0
	#Use a dictionary to keep track of the contraction of nodes
	super_node_mapping = {}
	for vertex in graph:
		super_node_mapping[vertex] = set([vertex])
	node_left = len(graph)
	#Keep contracting nodes until there are only two nodes left
	while node_left > 2:
		edge_picked, random_edge_idx = random_choose_edge(shuffled_edges, random_edge_idx, super_node_mapping)
		contract(edge_picked, super_node_mapping)
		node_left = node_left - 1
	#Get the crossing eges connecting two final patitions
	remaining_edges = []
	while random_edge_idx < len(shuffled_edges):
		edge_picked = shuffled_edges[random_edge_idx]
		if edge_picked[1] not in super_node_mapping[edge_picked[0]]:
			remaining_edges.append(edge_picked)
		random_edge_idx += 1
	return len(remaining_edges), remaining_edges


"""Repeatly find min cut"""
def find_min_cuts(graph, edges):
	length = len(graph)
	run_times = length * length 
	print "repeat %s times" % run_times
	best_min_cuts = len(graph)
	best_cuts = []
	#run the algorithms N^2 times so that the probability of missing min cuts is less than 1/e
	for i in xrange(run_times):
		print i
		min_cuts, cuts = random_contraction(graph, edges)
		#update the best min cut
		if min_cuts < best_min_cuts:
			best_min_cuts = min_cuts
			best_cuts = cuts
	return best_min_cuts, best_cuts


"""main function"""
def main():
	f_open = open("UndirectedGraph.txt", 'r')
	graph = {}
	edges = []
	#create adjacency list representation of the undirected graph
	for line in f_open:
		line_split = [int(vertex.rstrip("\n")) for vertex in line.split()]
		graph[line_split[0]] = line_split[1:]
	f_open.close()
	#create a list of edges which are tuples of two vertices
	for vertex in graph:
		for neighbor in graph[vertex]:
			if vertex < neighbor:
				edges.append((vertex, neighbor))
	min_cuts, cuts = find_min_cuts(graph, edges)
	print min_cuts
	print cuts

if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time() - start_time, "seconds"
