"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

    """
    x_cnt = sum(row.count(X) for row in board)
    o_cnt = sum(row.count(O) for row in board)

    return O if x_cnt > o_cnt else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(len(board)):
        for col in range(3):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if not (0 <= i < 3) or not (0 <= j < 3):
        raise Exception("Invalid action: out of bounds")

    if board[i][j] is not EMPTY:
        raise Exception("Unavaliable move")
    
    copy_board = copy.deepcopy(board)
    copy_board[i][j] = player(board)

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] is not EMPTY and row[0] == row[1] == row[2]:
            return row[0]
        
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
        return board[1][1] if board[1][1] is not EMPTY else None

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_cnt = sum(row.count(EMPTY) for row in board)
    
    if not empty_cnt or winner(board):
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """ 
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxValue(board):
        if terminal(board):
            return utility(board), None
        
        v = float('-inf')
        pos = None
        
        for action in actions(board):
            min_res, _ = minValue(result(board, action))
            if min_res > v:
                v = min_res
                pos = action
        
        return (v, pos)

    def minValue(board):
        if terminal(board):
            return utility(board), None
        
        v = float('inf')
        pos = None
        for action in actions(board):
            max_res, _ = maxValue(result(board, action))
            if max_res < v:
                v = max_res
                pos = action

        return (v, pos)
    
    player_turn = player(board)

    if player_turn == X:
        return maxValue(board)[1]
    else:
        return minValue(board)[1]

