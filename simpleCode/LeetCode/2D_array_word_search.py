""" Given a 2D board and a word, find if the word exists in the grid."""
""" The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once."""


def canConstructWord(board, s):
	visited = [[None]*len(board[0][0]) for i in xrange(len(board))]
	for i in xrange(len(board)):
		for j in xrange(len(board[0][0])):
			if board[i][0][j] == s[0]:
				result = search_word_DFS(board, s[1:], i,j, visited)
				if result:
					return True
	return False

def search_word_DFS(board, s, i, j, visited):
	if len(s) == 0:
		return True
	visited[i][j] = True
	possible_pos = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
	for new_i,new_j in possible_pos:
		if new_i<len(board) and new_i>=0 and new_j<len(board[0][0]) and new_j>=0 and not visited[new_i][new_j]:
			if board[new_i][0][new_j] == s[0]:
				result = search_word_DFS(board, s[1:], new_i, new_j, visited)
				if result:
					return True
	visited[i][j] = None
	return False

if __name__ == '__main__':
	board = [["ABCE"], 
			 ["SFCS"],
			 ["ADEE"]
			]
	s = 'ABCCED'
	s = 'SEE'
	s = 'ABCB'
	s = 'ABA'
	s = 'ECC'
	print canConstructWord(board, s)
