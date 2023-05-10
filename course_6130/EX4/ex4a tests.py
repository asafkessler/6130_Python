import numpy as np

import ex4a
def count_string_with_substring(arr_str, st):
    """
    :param arr_str: one dimensional array that contains only strings
    :param st: the substring
    :return: number of strings that contains the sub string(st)
    """
    st_appearance = np.char.count(arr_str, st)
    condition = st_appearance > 0
    words_contains_st = st_appearance[condition]

    return words_contains_st.size


arr_str = np.array(['a','b','c','d','e','ac', 'csc', 'pp'])
st = 'p'
print (count_string_with_substring(arr_str, st))
print(arr_str)