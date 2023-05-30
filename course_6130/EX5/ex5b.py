# 123456789, 123456789
# time
import glob

import numpy as np
import pandas as pd
import os

PATH = r'C:\Users\asafk\Desktop\Hebrow Univarcity\First Year\Semester B\Python Cognitive Science\EX5\friends_datasets_ex5'

def get_file_name_list_in_folder(folder_path):
    files_names = glob.glob(folder_path + r'\friends_imdb_episode_season_*')
    return list(files_names)


# question 2
def create_season_rating(csv_folder):

    list_files_names = get_file_name_list_in_folder(csv_folder)
    df_all_episodes = pd.read_csv(list_files_names[0])

    for index in range(1, len(list_files_names)):
        curr_season_df = pd.read_csv(list_files_names[index])
        df_all_episodes = pd.concat([df_all_episodes, curr_season_df], ignore_index=True, axis=0)

    df_imdb = pd.read_csv(csv_folder + r'\rating_all_imdb.csv')
    df_merged = df_all_episodes.merge(df_imdb, how="inner", on=["tconst"])
    print(list(df_merged.shape))
    print(list(df_merged.columns))

    seasons_sum = df_merged.groupby(by="seasonNumber", as_index=False).sum()[['seasonNumber', 'averageRating', 'numVotes']]
    seasons_rating = df_merged.groupby(by="seasonNumber", as_index=False).mean()[['seasonNumber', 'averageRating']]

    final_df = seasons_rating
    final_df["numVotes"] = seasons_sum["numVotes"]

    return (final_df)

def most_lines_in_the_second_most_popular_episode(csv_folder):
    df_line = pd.read_csv(csv_folder + r'friends_quotes.csv')

def who_said_it(csv_folder, character_name, phrase):
    pass


if __name__ == "__main__":
    create_season_rating(PATH)