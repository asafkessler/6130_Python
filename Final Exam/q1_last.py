# import numpy as np
#
# G_BOARD1 = [[1, 1],
#            [0, 1],
#            [1, 0],
#            [2, 1],
#            [8, 3],
#            [3, 5]]
# G_BOARD2 = [[1, 1],
#            [1, 1],
#            [2, 2],
#            [2, 2],
#            [3, 3],
#            [3, 3]]
# G_BOARD3 = [[1, 1], #שמירה על מקום
#            [1, 0],
#            [1, 2],
#            [2, 2],
#            [3, 3],
#            [3, 3]]
# G_BOARD4 = [[1, 1], # מעבר פעמיים
#            [1, 0],
#            [1, 2],
#            [2, 2],
#            [3, 2],
#            [3, 3]]
# G_BOARD5 = [[0, 1], # מינוס
#            [0, -1],
#            [1, 10]]
#
# STARTING_POINT = 1
#
#
# def max_value_and_location(pair, curr_state):
#     max_val = max(pair)
#     location = pair.index(max_val)
#     return max_val, curr_state-location , location
#
# def find_max_path(board, starting_point):
#     """
#     The road not taken.
#     Args:
#         board ():
#         starting_point ():
#
#     Returns:
#     """
#     if len(board) == 0:
#         return 0
#
#     max_val, cost, new_state = max_value_and_location(board.pop(0), starting_point)
#     path_sum = max_val - np.abs(cost) + find_max_path(board, new_state)
#     return path_sum
#
#
# if __name__ == "__main__":
#     print(find_max_path(G_BOARD1, STARTING_POINT))
G_BOARD1 = [[1, 1],
            [0, 1],
            [1, 0],
            [2, 1],
            [8, 3],
            [3, 5]]

STARTING_POINT = 1

def recursive_sum_max(board, starting_point):
    if not board:
        return 0

    curr_row = board.pop(0)
    curr_max_index = curr_row.index(max(curr_row))
    max_value = curr_row[curr_max_index]

    adjustment = -1 * int(curr_max_index != starting_point)

    return max_value + adjustment + recursive_sum_max(board, curr_max_index)


# Example usage
if __name__ == "__main__":
    total_sum = recursive_sum_max(G_BOARD1.copy(), starting_max_index)
    print("Total Sum:", total_sum)
