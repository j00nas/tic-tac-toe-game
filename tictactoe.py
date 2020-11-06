class TicTacToe(object):

	def __init__(self):
		self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
		self.positions_p1 = []
		self.positions_p2 = []
		self.run = True
		self.remis = False
		self.current_player = 1
		self.start()


	def start(self):
		while self.run:
			position = input(f'Player {self.current_player}, bitte eine Position zum ankreuzen angeben (1-9): ')

			while self.check_input(position):
				position = input(f'[WRONG INPUT] Player {self.current_player}, bitte eine gültige Position zum ankreuzen angeben (1-9): ')

			self.checkwin()
			self.current_player = 2 if self.current_player == 1 else 1
			if not self.remis: self.print_board()


	def check_input(self, position):
		if position.isdigit() and 0 < int(position) < 10 and int(position) not in self.positions_p1 and int(position) not in self.positions_p2:
			if self.current_player == 1:	
				self.board[int(position)-1] = "X"
				self.positions_p1.append(int(position))
			else:
				self.board[int(position)-1] = "O"
				self.positions_p2.append(int(position))
			return False
		return True


	def checkwin(self):
		win_combinations = [[0,1,2], [0,4,8], [0,3,6], [6,7,8], [2,5,8], [2,4,6]]
		for i in win_combinations:
			if self.board[i[0]] == 'X' and self.board[i[1]] == 'X' and self.board[i[2]] == 'X':
				print("Player 1 hat gewonnen!")
				self.run = False
			if self.board[i[0]] == 'O' and self.board[i[1]] == 'O' and self.board[i[2]] == 'O':
				print("Player 2 hat gewonnen!")
				self.run = False
		
		if len(self.positions_p1) == 5:
			print('Remis!')
			self.remis = True
			self.run = False

	def print_board(self):
		print(f'\n{self.board[0]} | {self.board[1]} | {self.board[2]}\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n{self.board[6]} | {self.board[7]} | {self.board[8]}\n')

TicTacToe()



