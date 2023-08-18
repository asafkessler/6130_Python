# 316539196
# 20
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


########################## Q1 - Question 1 ##########################
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


########################## Q2 - Question 2 ##########################
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


########################## Q3 - Question 3 ##########################

def get_file_name_list_in_folder(folder_path):
    """
    This function creates a list of all csv files names in a given folder.
    Csv File name =  full path names.

    Args:
        folder_path (): <String> a folder locate.

    Returns:
        <List> csv file names.
    """
    files_names = glob.glob(folder_path + r'\*.csv')
    return list(files_names)


def calc_rate_dollar_to_shekel(EUROinILS, USDinEURO):
    """
    e/s * d/e = d/s. dollar to shekel rate changer.
    Args:
        EUROinILS (): EURO in ILS
        USDinEURO (): USD in EURO

    Returns:
        simple multiplication.
    """
    return EUROinILS * USDinEURO


def create_n_show_graphs(df_USD_in_ILS_helper, df_USD_in_ILS_final):
    """
    This function creates the graph of the exchange rate through all the days in the original data.
       It creates a scattered graph for the extreme days found by the algorthm.
    Args:
        df_USD_in_ILS_helper (): <pandas.DataFrame> all data.
        df_USD_in_ILS_final (): <pandas.DataFrame> USD in ILS df data.

    Returns:
         None.
           presents graphs.
    """
    df_graph_data = df_USD_in_ILS_helper.iloc[::-1].reset_index(drop=True)
    df_graph_data = df_graph_data.reset_index(names='x_days_order')

    df_extreme_points_data = df_USD_in_ILS_final.merge(df_graph_data, how="inner",
                                                       on=["Year", "Month", "Day", "percent_change", "one_USD_in_ILS"])

    x_axis = df_graph_data.plot(x='x_days_order', y='one_USD_in_ILS', label='ILS for USD', linestyle='-', alpha=0.5)

    df_extreme_points_data.plot.scatter(x='x_days_order', y='one_USD_in_ILS', label='extreme_days', ax=x_axis,
                                        linestyle='', c='r', alpha=1)
    plt.show()


# Q3
def extreme_changes(folder, num_extreme_days, show_graphs):
    """
    This method calculates the days in which the change rate between USD to ILS
    is the biggest. It includes positive change, as well as negative change.
    At the end it builds those days in to a dataframe, and reruns it.
    Args:
        folder (): <String> the path to the location of the csv files, in which the rate value information is located.
        num_extreme_days (): <Int> the number of extreme days, from the total days of information, that the function need to report on.
        show_graphs (): <Boolean> true -> show graph of the exchange rate through all the days in the original data.

    Returns:
        df_USD_in_ILS by max rate days.
    """

    # 1) first stage - get the information location -> abstraction in case of more data in the future. (Not used).
    list_data_files_path = get_file_name_list_in_folder(folder)

    # 2) second stage - read the information
    df_EURO_in_ILS = pd.read_csv(folder + r'\EUR_ILS Historical Data.csv')
    df_USD_in_EURO = pd.read_csv(folder + r'\USD_EUR Historical Data.csv')

    # 3) third stage - creating the dollar to shekel rate dataframe
    df_USD_in_ILS_helper = df_EURO_in_ILS.merge(df_USD_in_EURO, how="inner", on=["Year", "Month", "Day"])

    df_USD_in_ILS_helper['one_USD_in_ILS'] = \
        df_USD_in_ILS_helper.apply(
            lambda row: calc_rate_dollar_to_shekel(row['one_EURO_in_ILS'], row['one_USD_in_EUROS']), axis=1)

    """ Logic: The previous one is actually the next one in order in the 
    dataframe. The Math Goes By: n-(n+1)(remember: next is back)/n+1. """

    df_USD_in_ILS_Reversed = df_USD_in_ILS_helper['one_USD_in_ILS'].shift(-1, fill_value=0)

    df_USD_in_ILS_helper['percent_change'] = ((df_USD_in_ILS_helper['one_USD_in_ILS'] -
                                               df_USD_in_ILS_Reversed) / df_USD_in_ILS_Reversed) * 100

    # 4) fourth stage - rearranging the data in the dataframe, relative to the rate change
    df_USD_in_ILS_helper['percent_change_abs'] = df_USD_in_ILS_helper.apply(lambda row:
                                                                            np.sqrt(row['percent_change'] ** 2), axis=1)

    sorting_dataframe = df_USD_in_ILS_helper.sort_values(by='percent_change_abs', ascending=False)
    df_USD_in_ILS_organized = sorting_dataframe.reset_index(drop=True)

    # 5) fifth stage - cutting the relevant num_extreme_days (num_extreme_days == num rows in dataframe)
    df_extreme_days = df_USD_in_ILS_organized.iloc[1: num_extreme_days + 1]
    df_USD_in_ILS_final = df_extreme_days[["Year", "Month", "Day", "one_USD_in_ILS", "percent_change"]]

    # if statement for graphs showing.
    if show_graphs:
        create_n_show_graphs(df_USD_in_ILS_helper, df_USD_in_ILS_final)

    return df_USD_in_ILS_final
