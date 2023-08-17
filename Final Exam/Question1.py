import numpy as np

G_BOARD = [[1, 1],
           [0, 1],
           [1, 0],
           [2, 1],
           [8, 3],
           [3, 5]]

STARTING_POINT = 1

def max_n_index(l_pair, curr_state):
    """
    This function
    Args:
        l_pair ():
        curr_state ():

    Returns:

    """
    if l_pair[0] > l_pair[1]:
        return l_pair[0], 0 - curr_state, 0   # smart move here.
    else:
        return l_pair[1], 1 - curr_state, 1
def find_max_path(board, row, starting_point):
    """
    This method function to find the maximum path sum
    Args:
        board ():
        row ():
        starting_point ():

    Returns:

    """
    if len(board) == 0: # תנאי עצירה
        return 0

    value, change_value, new_state = max_n_index(board[row], starting_point)
    path_sum = value - np.abs(change_value) + find_max_path(board, row + 1, new_state)
    return path_sum

if __name__ == "__main__":
    print(find_max_path(G_BOARD, 0, STARTING_POINT))






