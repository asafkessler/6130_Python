import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
    df_graph_data = df_graph_data.reset_index(names='x_time_order')

    df_extreme_points_data = df_USD_in_ILS_final.merge(df_graph_data, how="inner",
                                                       on=["Year", "Month", "Day", "percent_change", "one_USD_in_ILS"])

    x_axis = df_graph_data.plot(x='x_time_order', y='one_USD_in_ILS', label='ILS for USD', linestyle='-', alpha=0.5)

    df_extreme_points_data.plot.scatter(x='x_time_order', y='one_USD_in_ILS', label='extreme_days', ax=x_axis,
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


if __name__ == "__main__":
    FOLDER_PATH = r'C:\devl\work\6130 Python\Final Exam'
    NUM_EXTREME_DAYS = 6
    SHOW_GRAPHS = True

    extreme_changes(FOLDER_PATH, 10, True)

    extreme_changes(FOLDER_PATH, 3, False)

    assert (round(min(extreme_changes(FOLDER_PATH, 10, False)["percent_change"]), 4)) == -1.8635
    assert (round(max(extreme_changes(FOLDER_PATH, 10, False)["percent_change"]), 4)) == 1.6112
    assert (round(min(abs(extreme_changes(FOLDER_PATH, 10, False)["percent_change"])), 4)) == 1.1912
    assert (round(min(extreme_changes(FOLDER_PATH, 10, False)["one_USD_in_ILS"]), 4)) == 3.4217
    assert (list(extreme_changes(FOLDER_PATH, 10, False).columns)) == ['Year', 'Month', 'Day', 'one_USD_in_ILS',
                                                                       'percent_change']
    print("Question 3 - results of the data frame passed all tests!")
    print("also, check by yourself whether the graph of 'extreme_changes' function is shown correctly, and only once"
          " (for the first call of the function). \n")
