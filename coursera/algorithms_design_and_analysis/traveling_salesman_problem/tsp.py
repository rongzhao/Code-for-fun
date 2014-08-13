import math
import time

"""Gosper's Hack to generate all possible bitsets"""
def get_sets_in_order(node_set, subset_size):
	n = len(node_set)
	subset_list = []
	x = (1<<subset_size)-1
	while x < (1<<n):
		subset_list.append(x)
		y = x & -x
		c = x + y
		x = (((x ^ c) >> 2) / y) | c
	return subset_list

"""Use Dynamic Programming to solve Traveling Salesman Problem """
def dynamic_programming(graph, nodes_list):
	last_iter_position = {}
	last_array = []
	n = len(nodes_list)
	nodes_set = nodes_list
	#Get the start_node labeled as 0 and remove this node from the nodes list
	start_node = nodes_set.pop(0)
	#Loop over the size of nodeSet that contains all internal nodes(except for start node) from 1 to n
	for size in xrange(1, n):
		print size
		#2D array to store total cost of specific combination of subset and ending node
		new_array = []
		#Use a dictionary to map subset(bitset represented as an integer) to the position in the 2D array
		new_iter_position = {}
		pos = 0
		#Use Gosper's Hack to generate all possible subsets with specific size in bitset representation from a set of nodes
		new_set = get_sets_in_order(nodes_set, size)
		#Loop over all possible such subsets
		for s in new_set:
			#Map subset to the position in 2D array
			new_iter_position[s] = pos
			#Initialize a sub array per subset to store the cost of each ending node
			sub_array = [None]*n
			available_nodes = []
			#Get the bits(nodes) that are set to 1
			for j in xrange(1, n):
				check_bit_string = 1 << (j-1)
				if (s & check_bit_string) != 0:
					available_nodes.append(j)
			#Loop over all possible ending nodes
			for j in available_nodes:
				#Consider base case
				if size == 1:
					optimal_value = graph[start_node][j]
				else:
					optimal_value = float("inf")
					#Remove ending node from the subset
					sub_s = s & (~(1 << (j-1)))
					for w in available_nodes:
						if j != w:
							#Compute the minimum cost of this combination of subset and ending node from the values in the previous iteration
							new_value = last_array[last_iter_position[sub_s]][w] + graph[w][j]
							if new_value < optimal_value:
								optimal_value = new_value
				sub_array[j] = optimal_value
			new_array.append(sub_array)
			pos += 1
		#Only keep the values got from last iteration
		del last_iter_position
		del last_array
		last_iter_position = new_iter_position
		last_array = new_array
	#Compute final minimum cost of all cycles from start node to start_node, traversing every internal node exactly once
	final_optimal_value = float("inf")
	for node in xrange(1, n):
		final_value = last_array[0][node] + graph[start_node][node]
		if final_optimal_value > final_value:
			final_optimal_value = final_value
	return final_optimal_value

"""Get the graph in matrix representation"""
def get_graph(file_name):
	coordinates = [] 
	with open(file_name, 'r') as f_open:
		number_of_nodes = int(f_open.next())
		for line in f_open:
			line_split = line.rstrip('\n').split()
			coordinates.append((float(line_split[0]), float(line_split[1])))
	graph_matrix = [[None]*number_of_nodes for x in xrange(number_of_nodes)]
	nodes_list = []
	for i in xrange(number_of_nodes):
		nodes_list.append(i)
		graph_matrix[i][i] = 0
		j = i + 1
		while j < number_of_nodes:
			i_position, j_position = coordinates[i], coordinates[j]
			length_i_j = math.sqrt((i_position[0]-j_position[0])**2 + (i_position[1]-j_position[1])**2)
			graph_matrix[i][j], graph_matrix[j][i] = length_i_j, length_i_j
			j += 1
	return graph_matrix, nodes_list

def main():
	file_name='tsp.txt'
	#file_name='test.txt'
	graph, nodes_list = get_graph(file_name)
	optimal_cost = dynamic_programming(graph, nodes_list)
	print optimal_cost

if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time()-start_time, 'seconds'
