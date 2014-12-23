# RPN evaluator
def rpn
	# A stack to store all the operands
	operands = []
	# Read input argument as string and loop over each character in it
	input = ARGV[0]
	input_split = input.split
	input_split.each do |element|
		case element
			# If the character is a number, convert and add it to the stack
			when /\A[+-]?\d+(\.\d+)?\Z/
				operands.push(atoif(element))
			when '+'
				last_two_operands = operands.pop(2)
				raise ArgumentError, "Not enough arguments" unless last_two_operands.length>1
				result = last_two_operands[0] + last_two_operands[1]
				# add the new number to the stack
				operands.push(result)
			when '-'
				last_two_operands = operands.pop(2)
				raise ArgumentError, "Not enough arguments" unless last_two_operands.length>1
				result = last_two_operands[0] - last_two_operands[1]
				operands.push(result)
			when '*'
				last_two_operands = operands.pop(2)
				raise ArgumentError, "Not enough arguments" unless last_two_operands.length>1
				result = last_two_operands[0] * last_two_operands[1]
				operands.push(result)
			when '/'
				last_two_operands = operands.pop(2)
				raise ArgumentError, "Not enough arguments" unless last_two_operands.length>1
				result = last_two_operands[0] / last_two_operands[1]
				operands.push(result)
			else
				raise ArgumentError, 'Invalid number'
		end
	end
	raise ArgumentError, "too many arguments" if operands.length > 1
	puts operands.pop()
end

# A function that converts string to numeric
def atoif(str)
	negative = false
	number_of_decimal = 0
	numeric_value = 0
	# Give a flag and convert it to positive if the number is negative
	if str[0] == '-'
		negative = true
		str = str[1, str.length-1]
	end
	# Calculate the # of decimal digits in the number and convert it to whole number
	if str.split('.').length == 2
		number_of_decimal = str.split('.')[1].length
		str = str.delete('.')
	elsif str.split('.').length > 2
		raise ArgumentError, "Invalid number"
	end
	# Convert a string to integer
	str.each_byte do |x|
		if x < '0'.ord or x > '9'.ord
			raise ArgumentError, "Invalid number"
		end
		numeric_value = numeric_value*10 + (x - '0'.ord)
	end
	# Convert it back to negative value if needed
	numeric_value = -1 * numeric_value if negative
	# Convert it back to decimal if needed
	numeric_value = numeric_value/(10.0**number_of_decimal) if number_of_decimal > 0
	return numeric_value
end

rpn()
