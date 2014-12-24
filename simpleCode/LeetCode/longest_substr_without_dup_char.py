"""Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1."""

def lengthOfLongestSubstring(s):
	max_length_so_far = 0
	start_pos = 0
	char_so_far = {}
	for i in xrange(len(s)):
		char = s[i]
		if char in char_so_far and char_so_far[char] >= start_pos:
			max_length_so_far = max(max_length_so_far, (i - start_pos))
			start_pos = char_so_far[char] + 1
		char_so_far[char] = i
	max_length_so_far = max(max_length_so_far, (len(s) - start_pos))
	return max_length_so_far

if __name__ == '__main__':
	s = 'qopubjguxhxdipfzwswybgfylqvjzhar'
	print lengthOfLongestSubstring(s)

