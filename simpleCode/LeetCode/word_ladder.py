"""Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that: Only one letter can be changed at a time and Each intermediate word must exist in the dictionary"""

# Find a shortest path from start to end using BFS
def ladderLength(start, end, dict):
	char_list = []
	for i in xrange(26):
		char_list.append(chr(ord('a')+i))
	visited = {}
	queue = []
	visited[start] = 0
	queue.append(start)
	while queue:
		word = queue.pop(0)
		for i in xrange(len(word)):
			for char in char_list:
				new_word = word[:i]+char+word[i+1:]
				if new_word == end:
					return visited[word]+1+1
				elif new_word in dict and new_word not in visited:
					visited[new_word] = visited[word]+1
					queue.append(new_word)
	return 0

if __name__ == '__main__':
	start = "hit"
	end = "cog"
	dict = ["hot","dot","dog","lot","log"]
	print ladderLength(start, end, dict)
