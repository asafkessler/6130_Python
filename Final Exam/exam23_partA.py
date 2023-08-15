# 316539196
#
import matplotlib
import numpy as np

''' Global Variables '''
# 0 -> 1-1+1-1+1+2+8-1+5 = 15
# 1 -> 1+1-1+1+2+8-1+5 = 16
G_BOARD = [[1,1],
           [0,1],
           [1,0],
           [2,1],
           [8,3],
           [3,5]]

STARTING_POINT = 1

'''General Answer'''
def max_n_index(l_pair, curr_state):
    if l_pair[0] > l_pair[1]:
        return l_pair[0], 0 - curr_state, 0   # smart move here.
    else:
        return l_pair[1], 1 - curr_state, 1

# Q1
def find_max_path(board, starting_point):
    state = starting_point
    last_state = starting_point

    # The answer of the function.
    max_path_sum = board[0][state]

    for index_pair in range(1,len(board)):
        value , change_value, state  = max_n_index(board[index_pair], last_state)
        print("change value : ", change_value)
        max_path_sum += value - np.abs(change_value)
        last_state = state

    return max_path_sum

# Q2 -
# 1. make sure that when creating an instance only one parameter is passed by the user
# 2. make sure that the method name (not the constructor) is more_nodes
# 3. XX should be replaced.
# class Square(XX):
#     pass
#
#
# class Triangle(XX):
#     pass


# Q3

def extreme_changes(folder, num_extreme_days, show_graphs):
    pass


if __name__ == "__main__":
    print(find_max_path(G_BOARD, STARTING_POINT))