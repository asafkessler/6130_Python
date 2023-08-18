import numpy as np

G_BOARD1 = [[1, 1],
           [0, 1],
           [1, 0],
           [2, 1],
           [8, 3],
           [3, 5]]
G_BOARD2 = [[1, 1],
           [1, 1],
           [2, 2],
           [2, 2],
           [3, 3],
           [3, 3]]
G_BOARD3 = [[1, 1], #שמירה על מקום
           [1, 0],
           [1, 2],
           [2, 2],
           [3, 3],
           [3, 3]]
G_BOARD4 = [[1, 1], # מעבר פעמיים
           [1, 0],
           [1, 2],
           [2, 2],
           [3, 2],
           [3, 3]]
G_BOARD5 = [[0, 1], # מינוס
           [0, -1],
           [1, 10]]

STARTING_POINT = 1


def max_value_and_location(pair, curr_state):
    max_val = max(pair)
    location = pair.index(max_val)
    return max_val, curr_state-location , location

def find_max_path(board, starting_point):
    if len(board) == 0:
        return 0

    max_val, cost, new_state = max_value_and_location(board.pop(0), starting_point)
    path_sum = max_val - np.abs(cost) + find_max_path(board, new_state)
    return path_sum



# Example usage
if __name__ == "__main__":
    total_sum = find_max_path(G_BOARD1.copy(), STARTING_POINT)
    print("Total Sum:", total_sum)
