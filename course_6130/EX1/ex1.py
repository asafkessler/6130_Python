# 315535518, 316539196
# 5.0

# part B question 2
def max_count1(list_of_numbers):
    """
    Returns the biggest number in a list and the numbers of times it appears.
    :param list_of_numbers: list of numbers.
    :return: returns max value and amount of instances.
    """
    max1 = list_of_numbers[0]
    count_max = 0
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] > max1:
            max1 = list_of_numbers[i]
            count_max = 1
        elif list_of_numbers[i] == max1:
            count_max += 1
        else:
            continue

    L_max = list([max1, count_max])
    return L_max


def max_count2(list_of_numbers):
    """
    returns the biggest number in a list and the numbers of times it appears.
    :param list_of_numbers: list of numbers
    :return: returns max value and amount of instances
    """
    list_of_numbers.sort()
    max2 = list_of_numbers[len(list_of_numbers) - 1]
    count_max = list_of_numbers.count(max2)
    l_final = list([max2, count_max])

    return l_final


# part B question 3.b
def is_numeric(item):
    """
    checks if an object is int or float.
    :param x: parameter (general)
    :return: True for int or float type.
    """
    return isinstance(item, int) or isinstance(item, float)


# part  B question 4.b

def is_string(string_var):
    """
    checks if an object type us string.
        returns boolean expression
    :param a: parameter - type string
    :return: True for string type.
    """
    return isinstance(string_var, str)


def only_strings(list_of_items):
    """
    receives a list, return a list that contains all
    the strings from the original list by order.
    :param my_list: general lists of data
    :return: a list of only string values
    """
    string_list = list(filter(is_string, list_of_items))
    return string_list
