
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



# Q2 -
# 1. make sure that when creating an instance only one parameter is passed by the user
# 2. make sure that the method name (not the constructor) is more_nodes
# 3. XX should be replaced.
class Square(Shape):

    GEOMETRIC_SHAPE_KEY = 4
    def __init__(self, square_dots):
        Shape.__init__(self, square_dots) # if that checks on the key

class Triangle(Shape):

    GEOMETRIC_SHAPE_KEY = 3
    def __init__(self, triangle_dots):
        Shape.__init__(self, triangle_dots) # if that checks on the key


if __name__ == "__main__":
    coordinates_square = [[1, 1], [2, 2], [0, 2], [7, 7]]
    coordinates_triangle = [[1, 1], [2, 2], [0, 2]]
    coordinates_error1 = [[1, 1], [2, 2], [0, 2]]
    coordinates_error2 = []
    coordinates_error3 = [[1, 1], [2, 2], [0, 2], [7, 7], [3, 4]]
    square_instance = Square(coordinates_square)
    triangle_instance = Triangle(coordinates_triangle)


    def square_error_check(coordinates_error):
        try:
            Square(coordinates_error)
            raise AssertionError("the Square constructor got an invalid parameter and didn't raise an error")
        except ValueError:
            pass


    assert (square_instance.more_nodes(triangle_instance)) == True
    assert (triangle_instance.more_nodes(triangle_instance)) == False
    assert (triangle_instance.more_nodes(square_instance)) == False
    square_error_check(coordinates_error1)
    square_error_check(coordinates_error2)
    square_error_check(coordinates_error3)

    print("Question 2 passes all tests!\n")