"""Optimized implementation of Dynamic Programming to solve Knapsack problem with a large dataset (so large that straightforward implementation takes infeasible amount of time and space). """

import time 

"""Get items with their values and weights from a file"""
def get_items(file_name):
	items = []
	with open(file_name, 'r') as f_open:
		meta_data = f_open.next()
		capacity = int(meta_data.split()[0])
		for row in f_open:
			row_split = row.rstrip('\n').split()
			items.append((float(row_split[0]), int(row_split[1])))
	return items, capacity

"""merge two sorted lists into single sorted list"""
def sort(possible_changes1, possible_changes2):
	i, j = 0, 0
	possible_changes = []
	while i < len(possible_changes1) and j < len(possible_changes2):
		if possible_changes1[i][0] < possible_changes2[j][0]:
			possible_changes.append(possible_changes1[i])
			i += 1
		elif possible_changes1[i][0] > possible_changes2[j][0]:
			possible_changes.append(possible_changes2[j])
			j += 1
		else:
			if possible_changes1[i][1] > possible_changes2[j][1]:
				possible_changes.append(possible_changes1[i])
			else:
				possible_changes.append(possible_changes2[j])
			i += 1
			j += 1
	while i < len(possible_changes1):
		possible_changes.append(possible_changes1[i])
		i += 1
	while j < len(possible_changes2):
		possible_changes.append(possible_changes2[j])
		j += 1
	return possible_changes

"""Optimized implementation of Dynamic Programming"""
def dynamic_programming(items, capacity):
	number_of_items = len(items)
	#We only store the updates from last iteration
	current_compressed_column = [(0, 0)]
	for i in range(1, len(items)+1):
		item_value, item_weight = items[i-1][0], items[i-1][1]
		new_compressed_column = []
		possible_changes1 = []
		possible_changes2 = []
		for cell in current_compressed_column:
			possible_changes1.append((cell[0], cell[1]))
			if cell[0]+item_weight <= capacity:
				possible_changes2.append((cell[0]+item_weight, cell[1]+item_value))
		possible_changes = sort(possible_changes1, possible_changes2)
		#We only store the updates for values that are different from previous one (i.e. unique values this iteration)
		for i in xrange(len(possible_changes)):
			if possible_changes[i][0] == 0:
				new_compressed_column.append((0,0))
			else:
				previous_change_value = new_compressed_column[-1][1]
				change_weight, change_value = possible_changes[i][0], possible_changes[i][1]
				if change_value > previous_change_value:
					new_compressed_column.append((change_weight, change_value))
		current_compressed_column = new_compressed_column
	return current_compressed_column[-1]

def main():
	file_name = 'items2.txt'
	items, capacity = get_items(file_name)
	weight, optimal_value = dynamic_programming(items, capacity)
	print weight, optimal_value

if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time()-start_time, "seconds"
