"""Implement a variant of the 2-SUM algorithm. The goal is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t."""

"""Get array of integers from a file"""
def get_array_from_file(file_name):
	with open(file_name, "r") as f_open:
		array = f_open.readlines()
	array = [int(element.rstrip('\n')) for element in array]
	return array

"""2-SUM algorithm"""
def two_sum_algorithm(array, array_hash_table, target_sum):
	for integer in array:
		corresponding_integer = target_sum - integer
		if integer != corresponding_integer:
			if corresponding_integer in array_hash_table:
				return True
	return False

"""Main function"""
def main():
	file_name = "IntegerArray.txt"
	array = get_array_from_file(file_name)
	array_hash_table = {}
	#Use a hashtable to store all the integers for quick lookup
	for integer in array:
		array_hash_table[integer] = True
	valid_values = {}
	for target_sum in xrange(-10000, 10001):
		boolean_value = two_sum_algorithm(array, array_hash_table, target_sum)
		if boolean_value:
			valid_values[target_sum] = True
		print target_sum
	print len(valid_values)

if __name__ == '__main__':
	main()
