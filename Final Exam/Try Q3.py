import matplotlib.pyplot
import numpy as np
import pandas as pd
import matplotlib as plt
import math

folder = r'C:\devl\work\6130 Python\Final Exam'
PATH = folder
num_extreme_days = 9
show_graphs = True

#### reducing number of DF!!!!!!! #####
df_EURO_in_ILS = pd.read_csv(folder + r'\EUR_ILS Historical Data.csv')
df_USD_in_EUROS = pd.read_csv(folder + r'\USD_EUR Historical Data.csv')
df_USD_in_EUROS = df_USD_in_EUROS.iloc[:,0:4]

# merging the DF and creating new columns based on the data
df_merged = df_EURO_in_ILS.merge(df_USD_in_EUROS, how="inner", on=["Year", "Month", "Day"])
df_merged['one_USD_in_ILS'] = df_merged.apply(lambda r: r['one_EURO_in_ILS'] * r['one_USD_in_EUROS'], axis = 1)
shifted = df_merged['one_USD_in_ILS'].shift(-1, fill_value=0)
df_merged['percent change'] = ((df_merged['one_USD_in_ILS'] - shifted)/shifted)*100

# sorting the data according to the max change ! HEREEEE !
df_merged['percent change absolute val'] = df_merged.apply(lambda r: math.sqrt(r['percent change']**2), axis = 1)
df_sorted = df_merged.sort_values(by='percent change absolute val', ascending=False)
df_sort_update_index = df_sorted.reset_index(drop=True)

# taking the relevent number of days and only the relevent columns
df_critical_days = df_sort_update_index.iloc[1:num_extreme_days+1]   ### ignoring the inf value of the last line
final_df = df_critical_days[["Year", "Month", "Day","one_USD_in_ILS","percent change"]]

# implimanting a graph
#### improving and making it shorter - graph by indexes as X axis #####
if show_graphs == True:
    df_for_graph = df_merged.iloc[::-1].reset_index(drop=True)
    df_for_graph = df_for_graph.reset_index()
    df_extreme_points = final_df.merge(df_for_graph, how="inner",
                                       on=["Year", "Month", "Day", "percent change", "one_USD_in_ILS"])

    ax = df_for_graph.plot(x='chronological order', y='one_USD_in_ILS', label= 'ILS for USD', linestyle='-', alpha = 0.5 )

    df_extreme_points.plot.scatter(x='chronological order', y='one_USD_in_ILS',label='extreme days', ax=ax,linestyle='', c = 'r', alpha=1)
    plt.pyplot.show()

# data.reindex(index=data.index[::-1], inplace=True)
# df = df[::-1]
