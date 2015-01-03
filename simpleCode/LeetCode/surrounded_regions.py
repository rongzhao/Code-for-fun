"""Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'."""
"""A region is captured by flipping all 'O's into 'X's in that surrounded region."""

# Use DFS to find connected components
def solve_using_DFS(board):
	visited = {}
	for i in xrange(len(board)):
		for j in xrange(len(board[0])):
			if board[i][j]=='O' and (i,j) not in visited:
				current_visited = {}
				result = DFS(board, i, j, current_visited)
				if result:
					for m,n in current_visited:
						board[m][n] = 'X'
				else:
					visited.update(current_visited)

def DFS(board, i, j, current_visited):
	current_visited[(i, j)] = True
	neighbor_status = True
	possible_direction = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
	for idx1,idx2 in possible_direction:
		if idx1>=0 and idx1<len(board) and idx2>=0 and idx2<len(board[0]):
			result = True
			if board[idx1][idx2] == 'X':
				result = True
			elif board[idx1][idx2] == 'O' and (idx1,idx2) not in current_visited:
				result = DFS(board, idx1, idx2, current_visited)
			if neighbor_status:
				neighbor_status = result
		else:
			neighbor_status = False
	if neighbor_status:
		return True
	else:
		return False

# Use BFS to search from boundary
def solve(board):
	if not board:
		return
	n_row, n_column = len(board), len(board[0])
	queue = []
	# Starting from Top and Bottom
	for j in xrange(n_column):
		if board[0][j] == 'O':
			queue.append((0,j))
			board[0][j] = 'T'
		if board[n_row-1][j] == 'O':
			queue.append((n_row-1,j))
			board[n_row-1][j] = 'T'
	# Starting from Left and Right
	for i in xrange(n_row):
		if board[i][0] == 'O':
			queue.append((i,0))
			board[i][0] = 'T'
		if board[i][n_column-1] == 'O':
			queue.append((i, n_column-1))
			board[i][n_column-1] = 'T'
	# BFS
	while queue:
		i, j = queue.pop(0)
		possible_direction = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
		for idx1, idx2 in possible_direction:
			if (idx1>=0 and idx1<n_row and idx2>=0 and idx2<n_column) and board[idx1][idx2]=='O':
				board[idx1][idx2] = 'T'
				queue.append((idx1,idx2))
	# Flip corresponding values
	for i in xrange(n_row):
		for j in xrange(n_column):
			if board[i][j] == 'T':
				board[i][j] = 'O'
			elif board[i][j] == 'O':
				board[i][j] = 'X'

if __name__ == '__main__':
	board = [["O","O","O"],["O","O","O"],["O","O","O"]]
	solve(board)
	print board
