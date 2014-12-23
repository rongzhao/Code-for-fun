""" Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below."""

def minimumTotal(triangle):
	nrow = len(triangle)
	min_list = list(triangle[-1])
	for i in xrange(1, nrow):
		i = nrow-i-1
		for j in xrange(len(triangle[i])):
			min_list[j] = min(min_list[j], min_list[j+1]) + triangle[i][j]
	return min_list[0]

if __name__ == '__main__':
	triangle = [
		    [2],
			[3,4],
			[6,5,7],
			[4,1,8,3]
			]
	print minimumTotal(triangle)

