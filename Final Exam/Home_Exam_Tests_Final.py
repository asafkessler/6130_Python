from exam23_partA import *
from exam23_partB import *

# Q1:
board1 = [[1, 0], [0, 2], [1, 1]]
board2 = [[0, 0], [3, 1], [3, 0], [0, 0], [1, 2], [1, 2]]
board3 = [[0, 0], [0, -1], [0, 10], [2, 1], [1, 1.1], [0, 10]]
board4 = [[1, 2]]
board5 = [[1, 1], [2, 3], [3, 2]]
board6 = [[0, 3], [2, 900]]
board7 = [[4, 1], [2, 7], [3, 1], [4, 4], [4, 5], [0, 2]]
board8 = [[4, 1], [2, 7], [3, 1], [4, 4], [4, 5], [2, 0]]
board9 = [[4, 1], [2, 7], [3, 1], [4, 4], [4, 5], [0, 2]]

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

print("Question 1 passed all tests!\n")


# Q2:
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


# Q3:
your_folder_path = "C:\\Users\97254\Documents\קוגניציה\סמסטר ב' שנה 1\פייתון הלכה למעשה 6130\Home Exam"  # תחליף/פי פה את הpath לpath של התיקייה במחשבך
extreme_changes(your_folder_path, 10, True)
extreme_changes(your_folder_path, 3, False)

assert (round(min(extreme_changes(your_folder_path, 10, False)["percent_change"]), 4)) == -1.8635
assert (round(max(extreme_changes(your_folder_path, 10, False)["percent_change"]), 4)) == 1.6112
assert (round(min(abs(extreme_changes(your_folder_path, 10, False)["percent_change"])), 4)) == 1.1912
assert (round(min(extreme_changes(your_folder_path, 10, False)["one_USD_in_ILS"]), 4)) == 3.4217
assert (list(extreme_changes(your_folder_path, 10, False).columns)) == ['Year', 'Month', 'Day', 'one_USD_in_ILS',
                                                                        'percent_change']
print("Question 3 - results of the data frame passed all tests!")
print("also, check by yourself whether the graph of 'extreme_changes' function is shown correctly, and only once"
      " (for the first call of the function). \n")


# Q4
g = GroceryStore()

assert (g.add_product("milk", 3, 10)) == True
assert (g.add_product("bread", 1, 20)) == True
assert (g.add_product("MIlK", 3, 10)) == False
assert (g.add_product("milk", 1, 10)) == False
assert (g.add_to_customer("cheese", 111)) == False
assert (g.add_to_customer("milk", 111)) == True
assert (g.add_to_customer("MILK", 111)) == True
assert (g.add_to_customer("bread", 111)) == True
assert (g.add_to_customer("milk", 112)) == True
assert (g.add_to_customer("bread", 112)) == False
assert (g.add_to_customer("milk", 111)) == False
assert (g.people_in_store()) == 2
assert (g.pay_bill(112, 10.5)) == 0.5
assert (g.people_in_store()) == 1
assert (g.pay_bill(111, 60)) == 20
assert (g.people_in_store()) == 0

assert (g.add_product("bread", 1, 20)) == True
assert (g.add_product("milk", 1, 10)) == True
assert (g.add_to_customer("bread", 111)) == True
assert (g.add_to_customer("bread", 112)) == False
assert (g.people_in_store()) == 1
assert (g.add_product("bread", 1, 20)) == True
assert (g.add_to_customer("bread", 111)) == True
assert (g.pay_bill(111, 40)) == 0

assert (g.add_product("Apple", 1, 5))  == True
assert (g.add_product("Banana", 10, 8))  == True
assert (g.add_to_customer("apple", 123456789))  == True
assert (g.add_to_customer("Cheese", 123456789))  == False
assert (g.add_to_customer("Apple", 12336))  == False
assert (g.people_in_store())  == 1
assert (g.add_product("Apple", 1, 70))  == True
assert (g.add_to_customer("Apple", 12336))  == True
assert (g.people_in_store())  == 2
assert (g.pay_bill(123456789, 20))  == 15
assert (g.pay_bill(12336, 80))  == 10
assert (g.people_in_store())  == 0

print("Question 4 passed all tests!")
