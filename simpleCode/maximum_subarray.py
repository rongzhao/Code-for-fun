def max_subarray(array):
	max_so_far = max_ending_here = 0
	for number in array:
		max_ending_here = max(0, max_ending_here+number)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

if __name__ == '__main__':
	array = [1, 2, -4, 1, 3, -2, 3, -1]
	print max_subarray(array)
