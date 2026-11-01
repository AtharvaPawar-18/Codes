#Can place Queen
def isSafe(board, row, col, n):

  #Check row
  for i in range(col):
    if board[row][i] == 1:
      return False

  #Check upper Diagonal
  i, j = row-1, col-1
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i = i-1
    j = j-1

  #Check lower Diagonal
  i, j = row+1, col-1
  while i < n and j >= 0:
    if board[i][j] == 1:
      return False
    i = i+1
    j = j-1

  return True

#Solving
def solve(board, col, n):

  if col >= n:
    return True

  for i in range(n):

     if isSafe(board, i, col, n):

       board[i][col] = 1

       if solve(board, col+1, n):
         return True

       board[i][col] = 0
       
  return False

#Main program
n = int(input("Enter the no of Queens : "))

board = [[0 for i in range(n)] for j in range(n)]

if solve(board, 0, n):
  print("Solution")
  for row in board:
    print(row)
else:
  print("No solution")
