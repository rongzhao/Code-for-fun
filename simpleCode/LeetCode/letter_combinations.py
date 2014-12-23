""" Given a digit string, return all possible letter combinations that the number could represent """

digit_mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def find_letter_combinations(digits):
	if len(digits) == 0:
		return ['']
	else:
		letters = digit_mapping[int(digits[-1])]
		new_combs = []
		for letter in letters:
			current_combs = find_letter_combinations(digits[:-1])
			for comb in current_combs:
				new_combs.append(comb+letter)
		return new_combs



if __name__ == '__main__':
	digits = "23"
	combs = find_letter_combinations(digits)
	print combs
