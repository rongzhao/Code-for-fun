def recursive_permutation(array):
	new_permutation = []
	if len(array) == 1:
		return [array]
	else:
		for i in xrange(len(array)):
			sub_array = array[:i] + array[i+1:]
			sub_permutation = recursive_permutation(sub_array)
			for e in sub_permutation:
				new_permutation.append(e+array[i:i+1])
		return new_permutation

if __name__ == '__main__':
	array = [1,2,3]
	permutation = recursive_permutation(array)
	print permutation
