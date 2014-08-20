"""Use Strongly Connected Component approach to compute 2-Satisfiability problem. The task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable"""

"""The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not" """

import time

"""Global variable"""
visited = {}
leader = None

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

"""Check if there's any pair of x and -x in the same SCC. If yes, this instance is not satisfiable"""
def check_satisfiability(scc):
	for leader in scc:
		sorted_list = merge_sort(scc[leader])
		for idx in xrange(len(sorted_list)-1):
			if (sorted_list[idx+1]^1) == sorted_list[idx]:
				return False
	return True

"""First DFS to compute the finishing time of nodes in the graph"""
def dfs_first(graph, node, finishing_time):
	stack = []
	stack.append(node)
	visited[node] = 1
	while stack:
		current_node = stack[-1]
		#Visited node has three status 1, 2, and 3. Status 1 is for bookkeeping explored nodes and status 2 is for bookkeeping nodes whose neighbors have been explored, and status 3 is for bookkeeping nodes whose ordering have been computed
		if visited[current_node] == 2:
			finishing_time.append(current_node)
			stack.pop()
			visited[current_node] = 3
		elif visited[current_node] == 3:
			stack.pop()
		else:
			for neighbor in graph[current_node]:
				if visited[neighbor] < 2:
					stack.append(neighbor)
					visited[neighbor] = 1
			visited[current_node] = 2

"""Second DFS to find the SCC given the leader node"""
def dfs_second(graph, node, scc):
	stack = []
	stack.append(node)
	visited[node] = 1
	while stack:
		current_node = stack.pop()
		scc[leader].append(current_node)
		for neighbor in graph[current_node]:
			if visited[neighbor] == 0:
				stack.append(neighbor)
				visited[neighbor] = 1

"""Kosaraju's two pass algorithm"""
def kosaraju_two_pass_DFS(graph, graph_reversed):
	for node in graph_reversed:
		visited[node] = 0
	finishing_time = []
	for node in graph_reversed:
		if visited[node] == 0:
			dfs_first(graph_reversed, node, finishing_time)
	scc = {}
	global leader
	for node in graph:
		visited[node] = 0
	finishing_time_len = len(finishing_time)
	for idx in xrange(finishing_time_len):
		node = finishing_time[finishing_time_len-1-idx]
		if visited[node] == 0:
			leader = node
			scc[leader] = []
			dfs_second(graph, node, scc)
	return scc

"""Convert 2-SAT instance into an implication graph with two vertices per variable and two directed edges per clause"""
def get_implication_graph(file_name):
	graph, graph_reversed = {}, {}
	with open(file_name, 'r') as f_open:
		number_of_variables = int(f_open.next())
		for row in f_open:
			row_split = row.rstrip('\n').split()
			first_var, second_var = int(row_split[0]), int(row_split[1])
			if first_var < 0:
				first_var = abs(first_var)<<1
			else:
				first_var = (abs(first_var)<<1) ^ 1
			if second_var < 0:
				second_var = abs(second_var)<<1
			else:
				second_var = (abs(second_var)<<1) ^ 1
			vertex1, vertex2 = (first_var ^ 1), second_var
			graph.setdefault(vertex1, []).append(vertex2)
			graph.setdefault(vertex2, [])
			graph_reversed.setdefault(vertex2, []).append(vertex1)
			graph_reversed.setdefault(vertex1, [])
			vertex1, vertex2 = (second_var ^ 1), first_var
			graph.setdefault(vertex1, []).append(vertex2)
			graph.setdefault(vertex2, [])
			graph_reversed.setdefault(vertex2, []).append(vertex1)
			graph_reversed.setdefault(vertex1, [])
	return graph, graph_reversed

"""Main function"""
def main():
	file_names = ['2sat1.txt', '2sat2.txt', '2sat3.txt', '2sat4.txt', '2sat5.txt', '2sat6.txt']
	SAT_status = ''
	for file_name in file_names:
		implication_graph, implication_graph_reversed = get_implication_graph(file_name)
		ssc = kosaraju_two_pass_DFS(implication_graph, implication_graph_reversed)
		satisfiability = check_satisfiability(ssc)
		if satisfiability:
			print 'SAT'
			SAT_status += '1'
		else:
			print 'non-SAT'
			SAT_status += '0'
	print SAT_status

if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time()-start_time, 'seconds'
