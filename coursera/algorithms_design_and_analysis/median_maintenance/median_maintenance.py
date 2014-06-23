"""Implement the "Median Maintenance" algorithm. Calculate the real-time median for a stream of numbers, arriving one by one"""

import time

"""Min Heap"""
class MinHeap:
	def __init__(self):
		self.array = []

	def get_min(self):
		if self.array:
			return self.array[0]
		else:
			return None

	def extract_min(self):
		self.swap(0, len(self.array)-1)
		min_node = self.array.pop()
		self.bubble_down(0)
		return min_node

	def insert(self, node):
		self.array.append(node)
		self.bubble_up(len(self.array)-1)

	def get_length(self):
		return len(self.array)

	def swap(self, a, b):
		tmp = self.array[a]
		self.array[a] = self.array[b]
		self.array[b] = tmp

	def bubble_down(self, start_pos):
		left_child_pos = 2 * start_pos + 1
		right_child_pos = 2 * start_pos + 2
		smallest_pos = start_pos
		if left_child_pos < len(self.array) and self.array[left_child_pos] < self.array[smallest_pos]:
			smallest_pos = left_child_pos
		if right_child_pos < len(self.array) and self.array[right_child_pos] < self.array[smallest_pos]:
			smallest_pos = right_child_pos
		if smallest_pos != start_pos:
			self.swap(smallest_pos, start_pos)
			self.bubble_down(smallest_pos)

	def bubble_up(self, start_pos):
		parent_pos = (start_pos+1)/2 - 1
		if parent_pos >=0 and self.array[start_pos] < self.array[parent_pos]:
			self.swap(start_pos, parent_pos)
			self.bubble_up(parent_pos)

"""Max Heap"""
class MaxHeap:
	def __init__(self):
		self.array = []

	def get_max(self):
		if self.array:
			return self.array[0]
		else:
			return None

	def extract_max(self):
		self.swap(0, len(self.array)-1)
		max_node = self.array.pop()
		self.bubble_down(0)
		return max_node

	def insert(self, node):
		self.array.append(node)
		self.bubble_up(len(self.array)-1)

	def get_length(self):
		return len(self.array)

	def swap(self, a, b):
		tmp = self.array[a]
		self.array[a] = self.array[b]
		self.array[b] = tmp

	def bubble_down(self, start_pos):
		left_child_pos = 2 * start_pos + 1
		right_child_pos = 2 * start_pos + 2
		largest_pos = start_pos
		if left_child_pos < len(self.array) and self.array[left_child_pos] > self.array[largest_pos]:
			largest_pos = left_child_pos
		if right_child_pos < len(self.array) and self.array[right_child_pos] > self.array[largest_pos]:
			largest_pos = right_child_pos
		if largest_pos != start_pos:
			self.swap(largest_pos, start_pos)
			self.bubble_down(largest_pos)

	def bubble_up(self, start_pos):
		parent_pos = (start_pos+1)/2 - 1
		if parent_pos >= 0 and self.array[start_pos] > self.array[parent_pos]:
			self.swap(start_pos, parent_pos)
			self.bubble_up(parent_pos)

"""Get the median of a list of existing integers plus one more new integer"""
def get_median(low_half, high_half, integer):
	min_high_half = high_half.get_min()
	max_low_half = low_half.get_max()
	#Insert the new integer into the right heap
	if integer >= min_high_half:
		high_half.insert(integer)
	else:
		low_half.insert(integer)
	#Rebalance the heaps to make sure the difference between the lengths of two heaps is at most 1
	if high_half.get_length() - low_half.get_length() == 2:
		integer_moved = high_half.extract_min()
		low_half.insert(integer_moved)
	elif low_half.get_length() - high_half.get_length() == 2:
		integer_moved = low_half.extract_max()
		high_half.insert(integer_moved)
	#Compute the median and return it
	if high_half.get_length() > low_half.get_length():
		return high_half.get_min()
	else:
		return low_half.get_max()

"""Main function"""
def main():
	file_name = "IntegerArray.txt"
	with open(file_name, "r") as f_open:
		data = f_open.readlines()
	array = [int(element.rstrip('\n')) for element in data]
	#Create two heaps (min heap to store largest 1/2 integers and max heap to store smallest 1/2 integers)
	low_half = MaxHeap()
	high_half = MinHeap()
	medians = []
	for integer in array:
		#Calculate real-time median everytime we get a new integer
		median = get_median(low_half, high_half, integer)
		medians.append(median)
	last_four_digits = sum(medians) % 10000
	print last_four_digits

if __name__ == '__main__':
	start_time = time.time()
	main()
	print time.time()-start_time, "seconds"
