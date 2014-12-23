"""Given two integers representing the numerator and denominator of a fraction, return the fraction in string format."""
"""If the fractional part is repeating, enclose the repeating part in parentheses."""


def fractionToDecimal(numerator, denominator):
	result = ''
	if denominator == 0:
		return '0'
	if (numerator % denominator == 0):
		return str(numerator/denominator)
	if ((numerator < 0) ^ (denominator < 0)):
		result += '-'
	numerator, denominator = abs(numerator), abs(denominator)
	result += str(numerator/denominator)
	result += '.'
	remainder = numerator % denominator
	r_mapping = {}
	while remainder:
		remainder = remainder * 10
		if remainder in r_mapping:
			result = result[:r_mapping[remainder]] + '(' + result[r_mapping[remainder]:] + ')'
			break
		r_mapping[remainder] = len(result)
		result += str(remainder/denominator)
		remainder = remainder % denominator
	return result


if __name__ == '__main__':
	numerator, denominator = -2, 3
	print fractionToDecimal(numerator, denominator)
