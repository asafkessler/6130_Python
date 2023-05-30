# 316539196, 315535518
# 5
import copy

import numpy as np
import pandas as pd

# Part A

# 1
def filter_numeric_column(df, col_name, num1, num2):
    col_series = df[col_name]
    filtered_indexes = col_series[(col_series >= num1) & (col_series < num2)]
    index_list = list(filtered_indexes.index)
    new_dataframe = df[index_list[0]: index_list[1] + 1:]
    return new_dataframe


# 2
def switch_col_names(df, col_name1, col_name2):
    """

    :param df:
    :type df:
    :param col_name1:
    :type col_name1:
    :param col_name2:
    :type col_name2:
    :return:
    :rtype:
    """
    new_df = df.rename(columns=({col_name2:col_name2,col_name2:col_name1}))
    return new_df

def switch_col_names(df, col_name1, col_name2):
    col_new_list = list(col_name2,col_name1)
    curr_col = df.columns
    df_new = df.rename(columns ={curr_col[0]:col_new_list[0],curr_col[1]:col_new_list[1]})
    pass


# 3
def double_special_letters(df, col_name_letter, col_name_value, col_name_results):
    """

    :param df:
    :type df:
    :param col_name_letter:
    :type col_name_letter:
    :param col_name_value:
    :type col_name_value:
    :param col_name_results:
    :type col_name_results:
    :return:
    :rtype:
    """

    """
        
        double_special_letters(df, 'letter','value','col_res')
    """
    df = pd.DataFrame(data={'letter': ['h', 'a', 'b', 'c', 'i'], 'value': [3, 4, 5, 6, 7]})

    letters_to_double = ['h','u','j','i']
    col_results_series = copy.deepcopy(df[col_name_value])

    where_to_double =  []
    for curr_letter in df['letter']:
        if curr_letter in letters_to_double:
            where_to_double.append(True)
        else:
            where_to_double.append(False)

    for index in range(len(where_to_double)):
        if where_to_double[index]:
            col_results_series[index] *= 2

    new_dataframe = df
    new_dataframe[col_name_results] = col_results_series
    return new_dataframe


# 4
def put_row_items_together(df, col_name_results):
    pass
    # # Create an empty list
    # Row_list = []
    #
    # #Iterate over each row
    # for rows in df.iterrows
    #     # Create list for the current row
    #     my_list = [rows., rows.Event, rows.Cost]
    #     # place it in the data frame
    #     new_df = df
    #     new_df[col_name_results] = my_list
    # output
    # return new_df


if __name__ == "__main__":
    '''
        x = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7]})
        col_series = x['col1']
        filtered_indexes = col_series[(col_series >= 2) & (col_series < 4)]
        new_df = x[list(filtered_indexes.index)[0]: list(filtered_indexes.index)[1] + 1:]
    '''

    final = double_special_letters({},"letter" ,"value", "result")
    print(final)
