# 316539196, 315535518
# 10

import copy

from ex3 import Matrix, SquaredMatrix

def test_matrix_function():
    matrix_A = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
    # assert (matrix_A.mat == [[1, 2], [3, 4], [5, 6]])
    #
    # # (indices start from 0)
    # matrix_A.switch_rows(1, 2)
    # assert (matrix_A.mat == [[1, 2], [5, 6], [3, 4]])
    #
    # matrix_A.multiple_row(1, 2)
    # assert (matrix_A.mat == [[1, 2], [10, 12], [3, 4]])
    #
    # matrix_A.add_row_to_row(0, 2, -2)
    # assert (matrix_A.mat == [[-5, -6], [10, 12], [3, 4]])

def test_matrix_mult():
    matrix_A = Matrix(4, 2, [-1, 2, 3, 4, 5, 6 ,7 ,8])
    matrix_B = Matrix(2, 3, [-1, 2, 3, 4, 5, 6])
    matrix_A.matrix_mult(matrix_B)
    # assert (matrix_B.mat == [[-1, 2, 3], [4, 5, 6]])
    assert(matrix_A.mat == [[9, 8, 9], [13, 26, 33], [19, 40, 51], [25, 54 ,69]])

def test_square_matrix():
    matrix_A = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
    matrix_C = SquaredMatrix(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert (matrix_C.mat == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert (matrix_C.__pow__(1).mat == [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert (matrix_C.__pow__(2).mat == [[30, 36, 42], [66, 81, 96], [102, 126, 150]])

def test_deepcopy():
    arr = [1,2,3,4,5,6]
    arr_test = copy.deepcopy(arr)
    arr[4] = "asaf"
    print(arr, arr_test)

if __name__ == "__main__":
    """
        Testing the Matrix and SquaredMatrix Classes.
    """
    # feel free to change the testing status to explore our code :)
    bool_able_matrix_text = False
    bool_test_matrix_mult = True
    bool_test_square_matrix = False
    bool_test_deep_copy = False

    # Matrix Class Tests
    if bool_able_matrix_text:
        test_matrix_function()

    # Testing matrix multiplication
    if bool_test_matrix_mult:
        test_matrix_mult()

    # Testing of the SquaredMatrix
    if bool_test_square_matrix:
        test_square_matrix()

    # Test Of Deep Copy
    if bool_test_deep_copy:
        test_deepcopy()