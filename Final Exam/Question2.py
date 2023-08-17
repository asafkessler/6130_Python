
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
    s = Square([[1,2],[3,4],[1,3],[2,4]])
    t = Triangle([[1,2],[3,4],[1,3]])
    print(s.more_nodes(t))
    print(s.more_nodes(s))