import numpy as np

''' Global Variables '''
G_BOARD = [[1, 1],
           [0, 1],
           [1, 0],
           [2, 1],
           [8, 3],
           [3, 5]]

STARTING_POINT = 1

''' General Answer '''
def max_n_index(l_pair, curr_state):
    if l_pair[0] > l_pair[1]:
        return l_pair[0], 0 - curr_state, 0   # smart move here.
    else:
        return l_pair[1], 1 - curr_state, 1

# Recursive function to find the maximum path sum
def find_max_path_recursive(board, row, state):
    if row == len(board):
        return 0

    value, change_value, new_state = max_n_index(board[row], state)
    path_sum = value - np.abs(change_value) + find_max_path_recursive(board, row + 1, new_state)
    return path_sum

if __name__ == "__main__":
    print(find_max_path_recursive(G_BOARD, 0, STARTING_POINT))
