"""Compute the number of inversions in a file where the ith row of the file indicates the ith entry of an array, by implementing the divide-and-conquer algorithm"""

# Merge and count split inversions
def merge_and_countSplitInv(left, right):
	left_tt_len, right_tt_len = len(left), len(right)
	left_idx, right_idx = 0, 0
	merged_list, split_count = [], 0
	while left_idx < left_tt_len and right_idx < right_tt_len:
		if left[left_idx] <= right[right_idx]:
			merged_list.append(left[left_idx])
			left_idx += 1
		else:
			merged_list.append(right[right_idx])
			numbers_left = left_tt_len - left_idx
			split_count += numbers_left
			right_idx += 1
	while right_idx < right_tt_len:
		merged_list.append(right[right_idx])
		right_idx += 1
	while left_idx < left_tt_len:
		merged_list.append(left[left_idx])
		left_idx += 1
	return (merged_list, split_count)

# Count total number of inversions recursively
def count_inversion(ls):
	length = len(ls)
	if length <= 1:
		return (ls, 0)
	split_idx = length/2
	left_half = ls[:split_idx]
	right_half = ls[split_idx:]
	left_list_sorted, left_count = count_inversion(left_half)
	right_list_sorted, right_count = count_inversion(right_half)
	list_sorted, split_count = merge_and_countSplitInv(left_list_sorted, right_list_sorted)
	return list_sorted, left_count+right_count+split_count

if __name__ == '__main__':
	f = open("IntegerArray.txt", "rb")
	ls = f.readlines()
	f.close()
	ls = [int(l.strip("\n")) for l in ls]
	total_count = count_inversion(ls)[1]
	print "total_count is: %d" % total_count
