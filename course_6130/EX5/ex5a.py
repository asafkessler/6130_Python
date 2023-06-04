# 316539196, 315535518
# 10

import pandas as pd

def check_valid_input(list_df_columns, list_user_columns):
    """
    Args:
        list_df_columns (): the dataframes columns
        list_user_columns (): the user columns

    Returns:
        checks in the data is correct.
    """
    return all(elem in list_df_columns for elem in list_user_columns)


# Part A
# 1
def filter_numeric_column(df, col_name, num1, num2):
    """
    Args:
        df (): DataFrame all numeric elements?
        col_name (): The name of a Column in df.
        num1 (): numeric param
        num2 (): numeric Param

    Returns:
    A DataFrame which contains only rows in which the value in the
    given column name is between the numeric values given (including the lower value and not including the higher value).
    """
    column_data = df[col_name]

    # finding the exact min/max params
    (numeric_min, numeric_max) = (min(num1, num2), max(num1, num2))

    # getting only the indexes of the relevant values
    filtered_indexes = column_data[(column_data >= numeric_min) & (column_data < numeric_max)]
    index_list = list(filtered_indexes.index)

    # slicing the data frame by the relevant indexes chosen above
    start, end = index_list[0], index_list[0]
    if (len(index_list) > 1):
        end = index_list[len(index_list) - 1]

    new_dataframe = df[start: end + 1: ]

    return new_dataframe


# 2
def switch_col_names(df, col_name1, col_name2):
    """
    Args:
        df (): DataFrame
        col_name1 (): first name of a column
        col_name2 (): second name of a column

    Returns:
        The safe DataFrame but with switched columns.
    """

    col_new_list = list([col_name2,col_name1])
    curr_col = list(df.columns)

    if check_valid_input(curr_col, col_new_list):
        index_first = curr_col.index(col_name1)
        index_second = curr_col.index(col_name2)
        switched_df = df.rename(columns={curr_col[index_first]: col_new_list[0], curr_col[index_second]: col_new_list[1]})
    else:
        raise ValueError("The columns names are incorrect. Not Found in DataFrame")

    return switched_df


# 3
def double_special_letters(df, col_name_letter, col_name_value, col_name_results):
    """
    Args:
        df (): general dataframe
        col_name_letter (): column name of the letters data
        col_name_value (): column name of the values data
        col_name_results (): new column name of the results

    Returns:
        The function creates a new column named col_name_results
        that contains similar values to the values column
        The only difference is that in the new column the values are doubled if the letter is part of "huji".
    """

    letters_to_double = ['h', 'u', 'j', 'i']
    if check_valid_input(list(df.columns), list([col_name_letter, col_name_value])):
        df[col_name_results] = df.apply(lambda r: r[col_name_value]*2 if r[col_name_letter] in letters_to_double else r[col_name_value], axis=1)
    else:
        raise ValueError("The columns names are incorrect. Not Found in DataFrame")

    return df

# 4
def put_row_items_together(df, col_name_results):
    """
    Args:
        df (): general dataframe.
        col_name_results (): the column name to which the data will be aggregated.

    Returns:
        The function creates a new column.
         Each value in this column contains a list of all the items in the row.
    """
    df[col_name_results] = df.agg(list, axis=1)
    return df