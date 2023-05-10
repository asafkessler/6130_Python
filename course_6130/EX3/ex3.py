# 316539196, 315535518
# 10

class Matrix(object):
    """
        This class is a data matrix class.
    """

    def __init__(self, n_rows, n_cols, items):
        """
            Constractor for a new Matrix.
        """

        # Check Validity of row data input
        if not isinstance(n_rows, int):
            raise TypeError("row N. must be an Integer.")
        elif n_rows <= 0:
            raise ValueError("row number has to be greater than 0.")
        else:
            self.n_rows = n_rows

        # Check Validity of row data input
        if not isinstance(n_cols, int):
            raise TypeError("col N. must be an Integer.")
        elif n_cols <= 0:
            raise ValueError("col number has to be greater than 0.")
        else:
            self.n_cols = n_cols

        # Checking meaningful size
        official_size = self.n_cols * self.n_rows
        if official_size != len(items):
            raise ValueError("The number of items should be similar to the multiplication of the row&col number.")

        # Check Validity of items data input
        flag = False
        for value in items:
            if not (isinstance(value, (int, float))):
               flag = True
        if flag:
            raise TypeError("All matrix items should be of either a float or an int type.")
        else:
            self.items = items
            self.mat = [items[i:i + n_cols] for i in range(0, len(items), n_cols)]

    """Implementing matrix row functions"""

    def switch_rows(self, row_index1, row_index2):
        """
            This function takes two indexes of rows in a matrix and switch them.
            :param row_index1: index 1
            :param row_index2: index 2
            :return: None
        """

        line1 = self.mat[row_index1]
        line2 = self.mat[row_index2]

        self.mat[row_index1] = line2
        self.mat[row_index2] = line1

    def multiple_row(self, row_index, number):
        """
        This function multiple a row by any scalar except 0.
        :param row_index: row location
        :param number: multiplier that is different from 0
        :return: updated row
        """
        if number == 0:
            raise ValueError
            print("This function must get as input nuber different than 0, choose a different number.")
        else:
            mult_line = [value*number for value in self.mat[row_index]]
            self.mat[row_index] = mult_line

    def add_row_to_row(self, row_index1, row_index2, scalar):
        """
         Add a multiplication of one row to another.
        :param row_index1: the base row.
        :param row_index2: the multiplication of the row
        :param scalar: multiplier
        :return:
        """
        mult_line = [value*scalar for value in self.mat[row_index2]]
        changed_line =  [base_value + added_value for base_value, added_value in zip(self.mat[row_index1], mult_line)]
        self.mat[row_index1] = changed_line

    def matrix_mult(self, other_mat):
        """
        This function changes the self matrix to the multiple of two of them.
        :param self: first matrix
        :param other_mat: second matrix
        :return: change the first matrix to the multiple of the two of them.
        """
        matrix_copy = [[0 for index in range(self.n_rows)] for index in range(other_mat.n_cols)]
        if self.n_rows != other_mat.n_cols:
           raise Exception("Matrix Multiplication Is Not Valid.")
        else:
            # row number
            for i in range(self.n_rows):
                # col number
                for j in range(other_mat.n_cols):
                    # row number of other
                    for n in range(other_mat.n_rows):
                       matrix_copy[i][j] += self.mat[i][n] * other_mat.mat[n][j]

        self.mat = matrix_copy


class SquaredMatrix(Matrix):
    def __init__(self, n, items):
        """ init """

        validation_vector = [False, True]

        # Check Validity of rows and cols data input
        if not isinstance(n, int) :
            raise TypeError("The size of the matrix has to be an Integer.")
        elif n <= 0:
            raise ValueError("The size of the matrix has to be bigger than 0.")
        else:
            validation_vector[0] = True

        # Check Validity of items array
        for value in items:
            if not isinstance(value, (int, float)):
                validation_vector[1] = False
                raise ValueError("Data Type of all values in the"
                                 " Items Array has to be either int or flout.")

        if validation_vector.__contains__(False):
            pass
        else:
            # The other tests are ran in the constractor of the Matrix Class.
            self.items = items
            super().__init__(n, n, self.items)

    def __pow__(self, num_multi):
        """
         Multiple a matrix by itself "n" times.
        :param n: number of multiplications >= 0
        :return: product of the multiplication process.
        """
        if num_multi <= 0:
            raise ValueError("It isn't informative to multiply a matrix 0 or less times.")
        else:
            n_power_of_M = SquaredMatrix(self.n_rows, self.items)
            for t in range(num_multi - 1):
                n_power_of_M.matrix_mult(self)

            return n_power_of_M



