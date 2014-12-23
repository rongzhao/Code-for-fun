"""Given an array of integers, find two numbers such that they add up to a specific target number."""
"""The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based."""
"""You may assume that each input would have exactly one solution."""

def twoSum(num, target):
	num_mapping = {}
	for i in xrange(len(num)):
		num_mapping[num[i]] = i
	for i in xrange(len(num)):
		number = num[i]
		if (target-number) in num_mapping:
			if i < (num_mapping[target-number]):
				return (i+1, num_mapping[target-number]+1)
	return ()


if __name__ == '__main__':
	num, target = [2, 7, 11, 15], 9
	print twoSum(num, target)
