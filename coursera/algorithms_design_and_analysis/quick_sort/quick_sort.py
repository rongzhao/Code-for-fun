"""Compute the total number of comparisons used to sort the given input file by QuickSort"""

total_comparisons = 0

"""Get the median of three integers"""
def get_median(A, B, C):
	min_three = min([A, B, C])
	max_three = max([A, B, C])
	if A not in [min_three, max_three]:
		return A
	elif B not in [min_three, max_three]:
		return B
	else:
		return C

"""Choose pivot and exchange the pivot element with the first element"""
def choose_and_place_pivot(array, start_idx, end_idx, option='FIRST'):
	# use the last element in the given array as pivot
	if option == 'LAST':
		swap(array, start_idx, end_idx)
	# use "median-of-three" pivot rule to select pivot
	elif option == 'MEDIAN':
		length = end_idx - start_idx + 1
		if length % 2 == 0:
			middle_idx = length/2 + start_idx - 1
		else:
			middle_idx = length/2 + start_idx
		median = get_median(array[start_idx], array[middle_idx], array[end_idx])
		if median == array[middle_idx]:
			swap(array, start_idx, middle_idx)
		elif median == array[end_idx]:
			swap(array, start_idx, end_idx)
	assert option in ('LAST', 'FIRST', 'MEDIAN')
	return True

"""Swap two elements in the array"""
def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

"""Partition subroutine"""
def split_partition(array, start_idx, end_idx):
	l = start_idx
	i, j = l+1, l+1
	pivot = array[l]
	while j<= end_idx:
		if array[j] < pivot:
			if j > i:
			    swap(array, i, j)
			i += 1
		j += 1
	swap(array, l, i-1)
	return (i-2, i)

"""quick_sort function"""
def quick_sort(array, start_idx, end_idx):
	global total_comparisons
	length = end_idx - start_idx + 1
	if length > 1:
		choose_and_place_pivot(array, start_idx, end_idx, "FIRST")
		end_left_part, start_right_part = split_partition(array, start_idx, end_idx)
		if end_left_part >= start_idx:
			total_comparisons += end_left_part - start_idx
			quick_sort(array, start_idx, end_left_part)
		if start_right_part <= end_idx:
			total_comparisons += end_idx - start_right_part
			quick_sort(array, start_right_part, end_idx)

"""main function"""
def main():
	fopen = open("IntegerArray.txt", "rb")
	array = fopen.readlines()
	array = [int(e.strip("\n")) for e in array]
	fopen.close()
	global total_comparisons
	total_comparisons += len(array) -1
	quick_sort(array, 0, len(array)-1)
	print total_comparisons

if __name__ == '__main__':
	main()
