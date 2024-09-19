import time
"""
N-QUEENS GAME (Backtracking Edition)
A classic problem solved through backtracking. NumPy is not used in this solution.
The object of the game is to place N Queens on an N x N chessboard without any of
them being able to take eachother.

If there is no solution False will be returned. If there is a solution the first one
will be returned as a list of coordinates (top left is considered origin), a visual
representation of the board, and the time taken to complete the operation.

Yes, numpy makes this more efficient, and my code is not the most efficient. However, I
learned about the problem, devoted time to it, and will come back/revise it in the future.
While heavily documented in coding history, I would like to still try and improve
my own version of the NQueens problem. These improvements will come in optimizations. 
"""

def test_diag_pos(board):
    """
    Will see if there is more than one queen in each positive slope diagonal. 
    Returns True if no queens in same positive diagonal and False if a conflict.
        [1, 0, 0]
        [0, 1, 0]
        [0, 0, 1]
        Returns true because each positively sloped diagonal has either 1 or 0 queens
        [0, 0, 1]
        [0, 1, 0]
        [0, 0, 0] 
        Returns false because the central positively sloped diagonal has two queens 
    """
    summed_cols = board[0] + [0] * (len(board[0]) - 1)
    for i in range(len(board[0]) - 1):
        new_arr = ([0] * (i + 1)) + board[i + 1] + ([0] * (len(board[0]) - (i + 2)))
        summed_cols = [new_arr[i] + summed_cols[i] for i in range(len(summed_cols))]
    return True if max(summed_cols) < 2 else False

def test_diag_neg(board):
    """
    Same as sum_diag_pos except uses the negatively slopped diagonals. 
    Will return True if only one queen in each negatively sloped diagonal, else False.
    Examples given in sum_diag_pos are reverse (ex. EX1 returns False here and EX2 returns True)
    """
    return test_diag_pos([row[::-1] for row in board])

def test_rows(board):
    """
    Returns True if there is 0 or 1 queen(s) in each row, otherwise False
    """
    return True if max([sum(row) for row in board]) < 2 else False

def test_cols(board):
    """
    Returns True if there is 0 or 1 queen(s) in each column, otherwise False
    """
    summed_cols = board[0]
    for i in range(1,len(board)):
        summed_cols = [summed_cols[x] + board[i][x] for x in range(len(board))]
    return True if max(summed_cols) < 2 else False

def check_board(board):
    """
    Checks a board to make sure there are no more than one queen in each row, column, and diagonal
    Returns true if all queens on the board cannot take eachother, else false
    """
    if test_diag_pos(board) and test_diag_neg(board) and test_rows(board) and test_cols(board):
        return True
    return False

result = []
def solve_board(board,column):
    """
    Will solve the board using backtracking. Starts at (0,0), places a queen, and continues placing queens
    on the first avalible spot until either (1) the solution is reached or (2) the current placement is not
    a solution. In the case that the current path is not a solution, it rewinds until there are mutliple
    avalible paths and chooses the next path not tested. This "backtracking" to an avalible track happens only
    when one exists; the program will go back any amount of steps needed to test a new path.
    """
    global result
    if check_board(board):
        if sum([sum(row) for row in board]) == len(board[0]):
            return True
        for row in range(len(board[0])):
            board[row][column] = 1
            result.append([column,row])
            if check_board(board):
                if solve_board(board,column+1):
                    return True
                board[row][column] = 0
                result.remove([column,row])
            else:
                board[row][column] = 0
                result.remove([column,row])
    else:
        return False

"""
Below is how the program runs all the functions as well as input/output the 
person using the code sees.
"""
t0 = time.time()
input_n_val = int(input("Enter the size of board/number of queens: "))
board = [([0] * input_n_val) for _ in range(input_n_val)]
if solve_board(board,0):
    [print(row) for row in board]
    print("Queen(s) Coords: " + str(result))
else:
    print("No possible solution")
print("Estimated Execution Time: " + str(time.time() - t0) + " s")
if input_n_val <= 10:
    print("Note: Estimations work best with N >= 10+, below 10 the program runs too fast (less than 0.1 seconds) to get an accurate time")
    