#!/usr/bin/env python3

class BingoBoard:
	def __init__(self, val):
		self.board = []
		self.marked = []
		for i in range(5):
			row = []
			rowMarked = []
			for j in range(5):
				row.append(int(val[i][j]))
				rowMarked.append(False)
			self.board.append(row)
			self.marked.append(rowMarked)
	
	def mark(self, num):
		for i in range(5):
			for j in range(5):
				if self.board[i][j] == num:
					self.marked[i][j] = True

	def wins(self):
		for i in range(5):
			rowCnt = 0
			colCnt = 0
			for j in range(5):
				if self.marked[i][j]:
					rowCnt += 1
				if self.marked[j][i]:
					colCnt += 1
			if rowCnt == 5 or colCnt == 5:
				return True 
		return False

	def unmarked(self):
		sumNum = 0
		for i in range(5):
			for j in range(5):
				if not self.marked[i][j]:
					sumNum += self.board[i][j]
		return sumNum

f = open("puzzle.txt","r")
lines = f.readlines()

numbers = lines[0].split(',')
boards = []

index = 1
while index < len(lines):
	if lines[index] == "\n":
		index += 1
		continue
	
	val = []
	for ii in range(5):
		nums = []
		for symbol in lines[index + ii].split(" "):
			if len(symbol) == 0:
				continue
			if symbol[-1] == '\n':
				symbol = symbol[:-1]
			if symbol.isdigit():
				nums.append(symbol)
		row = []
		for jj in range(5):
			row.append(nums[jj])
		val.append(row)
	index += 5

	boards.append(BingoBoard(val))

last = 0
for num in numbers:
	for board in boards:
		if board.wins():
			continue
		board.mark(int(num))
		if board.wins():
			last = board.unmarked() * int(num)

print(last)
