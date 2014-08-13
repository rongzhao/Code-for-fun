"""Use Dynamic Programming to solve knapsack problem with integer weights and capacity"""

import numpy as np

def get_items(file_name):
	items = []
	with open(file_name, 'r') as f_open:
		meta_data = f_open.next()
		capacity = int(meta_data.split()[0])
		for row in f_open:
			row_split = row.rstrip('\n').split()
			items.append((float(row_split[0]), int(row_split[1])))
	return items, capacity

def dynamic_programming(items, capacity):
	number_of_items = len(items)
	array = np.zeros((number_of_items+1, capacity+1))
	for i in range(1, len(items)+1):
		for w in range(1, capacity+1):
			item_value, item_weight = items[i-1][0], items[i-1][1]
			if item_weight > w:
				optimal_value = array[i-1][w]
			else:
				subproblem1 = array[i-1][w]
				subproblem2 = array[i-1][w - item_weight] + item_value
				optimal_value = max(subproblem1, subproblem2)
			array[i][w] = optimal_value
	return array[number_of_items][capacity]


def main():
	file_name = 'items1.txt'
	items, capacity = get_items(file_name)
	optimal_value = dynamic_programming(items, capacity)
	print optimal_value

if __name__ == '__main__':
	main()
