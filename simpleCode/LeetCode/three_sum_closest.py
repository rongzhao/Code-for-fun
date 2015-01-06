"""Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution."""

def threeSumClosest(num, target):
	closest_sum = float("inf")
	num.sort()
	n = len(num)
	if n < 3:
		return 0
	for i in xrange(n-2):
		l = i + 1
		r = n - 1
		while l < r:
			three_sum = num[i] + num[l] + num[r]
			if abs(three_sum-target) < abs(closest_sum-target):
				closest_sum = three_sum
			if three_sum < target:
				l += 1
			elif three_sum > target:
				r -= 1
			else:
				return three_sum
	return closest_sum

if __name__ == '__main__':
	num = [-1, 2, 1, -4]
	target = 1
	print threeSumClosest(num, target)
