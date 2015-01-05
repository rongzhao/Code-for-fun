"""Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero."""
"""Elements in a triplet (a,b,c) must be in non-descending order. """
"""The solution set must not contain duplicate triplets."""


def threeSum(num):
	triplets = []
	# Sort the array
	num.sort()
	n = len(num)
	if n < 3:
		return triplets
	for i in xrange(n-2):
		# Change the problem to b+c=-a where c>=b>=a
		l = i + 1
		r = n - 1
		# Skip duplicates of a
		if i != 0 and num[i] == num[i-1]:
			continue
		while l < r:
			# Skip duplicates of b and c
			if (l > i+1) and num[l] == num[l-1]:
				l += 1
			# Change b and c based on the comparison with -a
			elif (num[l] + num[r]) < -num[i]:
				l += 1
			elif (num[l] + num[r]) > -num[i]:
				r -= 1
			else:
				triplets.append([num[i], num[l], num[r]])
				l += 1
				r -= 1
	return triplets


if __name__ == '__main__':
	num = [-1, 0, 1, 2, -1, -4]
	print threeSum(num)
