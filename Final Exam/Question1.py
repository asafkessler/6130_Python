G_BOARD = [[1, 1],
           [0, 1],
           [1, 0],
           [2, 1],
           [8, 3],
           [3, 5]]

STARTING_POINT = 0


# Question 1
def find_max_path(board, starting_point):
    """
    This function finds the maximum path sum in a given board, under the following principles:
    1) it starts from a given starting_point
    2) it walks to the max value in a local pair of numbers in the board. we can think of a local pair as a row.
    3) if the pointer to the max value changes from row(pair) n = 1, to row n + 1, it subtracts 1 from the total sum.
    4) the function needs to see in to the future, which means it need to deside if to keep the pointer in its position,
    or move it, in terms of a general max path role.

    A Note from the programmer (@asafk):
    This Q was interesting! In one of my versions I looked on the board as a DAG, and ran a max path algorithm on
    it. It worked, but I wasn't able to bring it to the required design.

    Another note:
    only if life could be more like parallel recursive algorithms with a max function at the end.
    I wouldn't need to choose, I could study psychology and cognitive science, while running another "self"
    (process) that will study physics and cognitive science. And at the end, when all the different self's, all
    the different parallel processes, will reach the end - pair/row, or Time for that matter, a manager self, will run
    a max function that will determine which life was a "better" life to live.

    Args:
        board (): a given board, structured as a <List<List<[number, number]>>.
        starting_point (): the starting point for the pointer in the first row/pair.

    Returns:
        The value of the max path.
    """

    # recursive breaking point
    if len(board) == 1:
        return board[0][starting_point]

    cost_option1 = find_max_path(board[1:], starting_point) + board[0][starting_point]
    cost_option2 = find_max_path(board[1:], 1 - starting_point) + board[0][starting_point] - 1
    return max(cost_option1, cost_option2)


if __name__ == "__main__":
    board1 = [[1, 0], [0, 2], [1, 1]]
    board2 = [[0, 0], [3, 1], [3, 0], [0, 0], [1, 2], [1, 2]]
    board3 = [[0, 0], [0, -1], [0, 10], [2, 1], [1, 1.1], [0, 10]]
    board4 = [[1, 2]]
    board5 = [[1, 1], [2, 3], [3, 2]]
    board6 = [[0, 3], [2, 900]]
    board7 = [[4, 1], [2, 7], [3, 1], [4, 4], [4, 5], [0, 2]]
    board8 = [[4, 1], [2, 7], [3, 1], [4, 4], [4, 5], [2, 0]]
    board9 = [[4, 1], [2, 7], [3, 1], [4, 4], [4, 5], [0, 2]]
    board10 = [[0, 1], [0, -1], [1, 10]]

    assert (find_max_path(board1, 0)) == 3
    assert (find_max_path(board1, 1)) == 3
    assert (find_max_path(board2, 1)) == 8
    assert (find_max_path(board3, 1)) == 21.1
    assert (find_max_path(board4, 0)) == 1
    assert (find_max_path(board5, 0)) == 6
    assert (find_max_path(board6, 0)) == 899
    assert (find_max_path(board7, 1)) == 20
    assert (find_max_path(board8, 1)) == 20
    assert (find_max_path(board9, 0)) == 22
    assert (find_max_path(board10, 0)) == 9
    assert (find_max_path(board10, 1)) == 10
    assert (find_max_path(G_BOARD, 0)) == 16
    assert (find_max_path(G_BOARD, 1)) == 16
    print("Question 1 passed all tests!\n")
