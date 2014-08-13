"""The goal is to code up the single link clustering algorithm using Kruskal's MST algorithm for computing a max-spacing k-clustering, but on a VERY big graph"""
"""Each node is labeled as a 24 bits string and the distance between two nodes u and v is defined as the Hamming distance--- the number of differing bits --- between the two nodes' labels"""
"""The problem is to compute what is the largest value of k such that there is a k-clustering with spacing at least 3"""

import time

"""Union Find data structure using Lazy Unions with union-by-rank and path compression"""
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

"""Get the graph from the file represented as a hash table with bitset as key"""
def get_from_file(file_name):
	bitset_dict= {}
	with open(file_name, "r") as f_open:
		meta_data = f_open.next()
		for row in f_open:
			bitstring = row.replace(' ', '')
			bitset = int(bitstring, 2)
			bitset_dict[bitset] = True
	node_label = 1
	for bitset in bitset_dict:
		bitset_dict[bitset] = node_label
		node_label += 1
	return bitset_dict, int(meta_data.split()[1])


"""Use the idea of Kruskal's algorithm to compute max-spacing k-clustering"""
def modified_kruskal_algorithm(bitset_dict, spacing_limit, num_of_bits):
	#Use Gosper's hack to generate all possible bitsets that have specific number of 1s
	fixed_bit_set = []
	for s in xrange(1,spacing_limit+1):
		x = (1 << s) - 1
		while x < (1<<num_of_bits):
			fixed_bit_set.append(x)
			y = x & -x
			c = x + y
			x = (((x ^ c) >> 2) / y) | c
	nodes_list = bitset_dict.values()
	cluster_count = len(nodes_list)
	clusters = union_find(nodes_list)
	c=1
	#For each node, if there's any node that is 2 or 1 away from it, merge them.
	for bitset in bitset_dict:
		print c, 'of', len(nodes_list)
		c += 1
		node1 = bitset_dict[bitset]
		for i in fixed_bit_set:
			#Compute possible node that is 2 or 1 away from current node using bit-wise operation XOR
			possible_bitset = bitset ^ i
			if possible_bitset in bitset_dict:
				node2 = bitset_dict[possible_bitset]
				if clusters.find(node1) != clusters.find(node2):
					clusters.union(node1, node2)
					cluster_count -= 1
	return cluster_count

def main(spacing_limit):
	#file_name = "test.txt"
	file_name = "big_graph.txt"
	bitset_dict, num_of_bits = get_from_file(file_name)
	k = modified_kruskal_algorithm(bitset_dict, spacing_limit, num_of_bits)
	print k

if __name__ == '__main__':
	start_time = time.time()
	main(2)
	print time.time()-start_time, "seconds"
