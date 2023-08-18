class Shape(object):
    """
        Shape: This is an abstract class for a geometrical object.
                (for this specific exersice all the objects are 2D).

        Data members: <List> shape_dots.

        Methods: comparison.
    """

    # A key to define geometric shape. (design based on a OOP static class variable)
    GEOMETRIC_SHAPE_KEY = 0

    def __init__(self, shape_dots):
        """
            Constractor.
        Args:
            shape_dots (): List<nodes>
        """
        # Checking if the users shape_dots list is in the right size for the relevant shape to create.
        if self.test_geometric_blueprint_input(shape_dots):
            self.l_dots = shape_dots
        else:
            raise ValueError("You entered the wrong number of nodes for this shape, Try again.")

    def get(self):
        return self.l_dots

    def print_shape(self):
        print("N. Of dots:", len(self), "Dots: ", print(self.l_dots))

    def more_nodes(self, shape_obj):
        """
            This method checks if a given shape has more nodes than another shape.
        Args:
            shape_obj (): Shape.

        Returns:
            Boolean. True if self shape has more dots, False if not.
        """
        return len(self.get()) > len(shape_obj.get())

    def test_geometric_blueprint_input(self, shape_dots):
        return self.GEOMETRIC_SHAPE_KEY == len(shape_dots)


class Square(Shape):
    GEOMETRIC_SHAPE_KEY = 4

    def __init__(self, square_dots):
        # Creates a square using the parent constractor.
        Shape.__init__(self, square_dots)


class Triangle(Shape):
    GEOMETRIC_SHAPE_KEY = 3

    def __init__(self, triangle_dots):
        # Creates a triangle using the parent constractor.
        Shape.__init__(self, triangle_dots)


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
