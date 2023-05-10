# 315535518, 316539196
# 3

import numpy as np


def find_largest_n(arr, number):
    """
    This function finds the largest number in a given array.
    :param arr: given array.
    :param number: how many max numbers we want from the original array.
    :return: new array with the max values.
    """

    # sorts the array numbers on the same axis
    temp_arr = np.sort(arr, axis=None)
    # takes the N last numbers from the sorted array
    N_Largest_arr = temp_arr[-number:]

    return N_Largest_arr


def find_even_larger_than(arr, N):
    """
    This function finds all the even numbers in the array which are larger than N
    :param arr: one dimensional array
    :param N: the limit number to the new arr
    :return:  with even numbers that are bigger than N
    """

    condition = np.mod(arr, 2) == 0
    temp_arr = arr[condition]
    condition2 = temp_arr > N
    new_arr = temp_arr[condition2]

    return new_arr


def add_prefix_suffix(arr_str, prefix_st, suffix_st):
    """
    This function adds 2 chars a pre_fix and a suffix to a given string.
    :param arr_str: array that contains only strings
    :param prefix_st: the beginning addition to each word
    :param suffix_st: the ending addition to each word
    :return: updated arr with the whole string after additions
    """
    # adding the prefix at the beginning
    arr_str_pre = np.char.add(prefix_st, arr_str)
    # adding the suffix at the end
    updated_arr_str = np.char.add(arr_str_pre, suffix_st)

    return updated_arr_str


def count_string_with_substring(arr_str, st):
    """
    This function counts the number of appearances of a substring in a given string.
    :param arr_str: one dimensional array that contains only strings
    :param st: the substring
    :return: number of strings that contains the sub string(st)
    """
    st_appearance = np.char.count(arr_str, st)
    condition = st_appearance > 0
    words_contains_st = st_appearance[condition]

    return words_contains_st.size
