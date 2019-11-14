counter = 0

def board_gen(board_size):
	"""Generate the board correspond to the given size
		Arg: board size in Integer
		Return: Board in the correcpond size
	"""

	row_list, board = list(), list()

	while len(board) < board_size:
		for x in range(board_size): 
		  row_list.append(0)
		board.append(row_list)
		row_list = []#reset

	return board
			
def position_checker(board, original_row, original_col, size):
	"""Check if queen position placement is okay
		Arg: Board, Row position, Column position, size of the board
		Return: False if position is not available
				True if the position is available to place
	"""

	#check row on left side
	for col in range(original_col):
		if board[original_row][col] == 1:
			return False
	
	row, col = original_row, original_col
	while row >= 0 and col >= 0:
		if board[row][col] == 1:
			return False
		row -= 1
		col -= 1
	
	o_row, o_col = original_row,original_col
	while o_row < size and o_col >= 0:
		if board[o_row][o_col] == 1:
			return False
		o_row += 1
		o_col -= 1

	return True

def board_solver(board, col, size):
	"""Count the posible board
		Arg: Board, Column position, Board size
		Return: None on board is not valid
				Backtracking on sucessful board
	"""

	global counter

	#incase col reach outside row size
	if col >= size:
		return None
	
	for row in range(size):
		if position_checker(board, row, col, size):
			board[row][col] = 1
			if col == size - 1:
				counter += 1
				print_board(board)
				board[row][col] = 0
				return None
			board_solver(board, col + 1, size)
			#backtracking find next solution
			board[row][col] = 0

def print_board(board):
	""" Display the posibility board
		Arg: Board
		Return: Nothing
	"""
	print(f"Board - {counter}")
	for row_s in board:
		print(row_s)
	print(" ")

def queen_bonus(board_size):
	"""Do the N queen problem posibility counter
		Arg: Board size
		Return: Posibility counter
	"""
	if board_size >=1 and board_size <= 12:
		board = board_gen(board_size)
		board_solver(board, 0, board_size)
		return counter
	else:
		print("Board size and Number of queens accept from 1 to 12 only")
		return counter

queen_bonus(12)
queen_bonus(13)
