# 316539196
#
import matplotlib
import numpy as np

# Q1 -
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
class Shape:

    # this is based on a OOP static class variable design.
    GEOMETRIC_SHAPE_KEY = 0

    def __init__(self, shape_dots):
        if self.test_geometric_blueprint_input(shape_dots):
            self.l_dots = shape_dots
        else:
            raise ValueError("You entered the wrong number of nodes for this shape, Try again.")

    def get(self):
        return self.l_dots

    def print_shape(self):
        print("N. Of dots:", self.get_nodes_number(self) , "Dots: ", print(self.l_dots))

    def more_nodes(self, shape_obj):
        return self.get_nodes_number(self.get()) > self.get_nodes_number(shape_obj.get())

    def test_geometric_blueprint_input(self, shape_dots):
        return self.GEOMETRIC_SHAPE_KEY == len(shape_dots)

    @staticmethod
    def get_nodes_number(shape):
        """
        "Does it make sense to call this method, even if no object has been constructed yet?" -> Yes.
        Args:
            shape ():

        Returns:
        """
        return len(shape)

class Square(Shape):

    GEOMETRIC_SHAPE_KEY = 4
    def __init__(self, square_dots):
        Shape.__init__(self, square_dots) # if that checks on the key

class Triangle(Shape):

    GEOMETRIC_SHAPE_KEY = 3
    def __init__(self, triangle_dots):
        Shape.__init__(self, triangle_dots) # if that checks on the key

# Q3 -
def extreme_changes(folder, num_extreme_days, show_graphs):
    pass

if __name__ == "__main__":
    print(find_max_path(G_BOARD, STARTING_POINT))