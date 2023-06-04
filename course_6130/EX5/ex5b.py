# 123456789, 123456789
# 15

import glob
import pandas as pd

PATH = r'C:\Users\asafk\Desktop\Hebrow Univarcity\First Year\Semester B\Python Cognitive Science\EX5\friends_datasets_ex5'

def get_file_name_list_in_folder(folder_path):
    files_names = glob.glob(folder_path + r'\friends_imdb_episode_season_*')
    return list(files_names)

# question 2
def create_season_rating(csv_folder):
    """
    Args:
        csv_folder: folder containing csv files

    Returns: DF with all the seasons rated (numVotes = num of episodes, sumvotes\avrargeVotes per episode)
    """
    list_files_names = get_file_name_list_in_folder(csv_folder)
    df_all_episodes = pd.read_csv(list_files_names[0])

    # reading all episodes data
    for index in range(1, len(list_files_names)):
        curr_season_df = pd.read_csv(list_files_names[index])
        df_all_episodes = pd.concat([df_all_episodes, curr_season_df], ignore_index=True, axis=0)

    # reading imdb data
    df_imdb = pd.read_csv(csv_folder + r'\rating_all_imdb.csv')

    # merging the data frames
    df_merged = df_all_episodes.merge(df_imdb, how="inner", on=["tconst"])

    # creating a Weighted average
    df_merged['sum_Rating'] = df_merged.apply(lambda e: e['averageRating'] * e['numVotes'], axis=1)
    seasons_sum = df_merged.groupby(by="seasonNumber", as_index=False).sum()[['seasonNumber', 'averageRating', 'numVotes','sum_Rating' ]]
    seasons_sum['Weighted_averageRating'] = df_merged.apply(lambda e: e['sum_Rating'] / e['numVotes'], axis=1)
    seasons_sum.rename(columns={'numVotes': 'sumNumVotes'},inplace = True)

    # deep coping the information
    seasons_temp = df_merged.copy(deep = True)

    # cleaning the data - deleting the pointer
    seasons_temp.drop('tconst', inplace=True, axis=1)
    seasons_rating = seasons_temp.groupby(by="seasonNumber", as_index=False).mean()[['seasonNumber' , 'numVotes']]
    seasons_rating['Weighted_averageRating'] = seasons_sum['Weighted_averageRating']   ###
    ### to change the averageRating to regular, write 'averageRating' instead of 'Weighted_averageRating' on both sides!
    seasons_rating.rename(columns={'numVotes': 'averageNumVotes'}, inplace = True)

    # seasons_rating['numVotes'] = seasons_rating.apply(lambda r: r['sumNumVotes'] / r['averageNumVotes'], axis=1) # if isinstance(r['sumNumVotes'], (int or float)) else r['sumNumVotes'] / r['averageNumVotes']
    seasons_rating['sumNumVotes'] = seasons_sum['sumNumVotes']
    seasons_rating['numVotes'] = seasons_rating.apply(lambda r: r['sumNumVotes'] / r['averageNumVotes'], axis = 1)
    seasons_rating.drop(['averageNumVotes','sumNumVotes'], inplace=True, axis=1)

    final_df = seasons_rating

    return (final_df)


# question 3
def most_lines_in_the_second_most_popular_episode(csv_folder):
    """

    Args:
        csv_folder: folder containing csv files

    Returns: DF containing the num of quotes each character has in  the second most popular ep. (based on numvotes)

    """
    # creating the base DF from the folder
    list_files_names = get_file_name_list_in_folder(csv_folder)
    df_all_episodes = pd.read_csv(list_files_names[0])

    for index in range(1, len(list_files_names)):
        curr_season_df = pd.read_csv(list_files_names[index])
        df_all_episodes = pd.concat([df_all_episodes, curr_season_df], ignore_index=True, axis=0)

    df_imdb = pd.read_csv(csv_folder + r'\rating_all_imdb.csv')
    df_merged = df_all_episodes.merge(df_imdb, how="inner", on=["tconst"])
    df_lines = pd.read_csv(csv_folder + r'\friends_quotes.csv')

    # sort the values in order to extract the relevant episode
    df_sorted_ep = df_merged.sort_values(by='numVotes', ascending=False)
    df_sort_ep_new_index = df_sorted_ep.reset_index()
    df_new = df_sort_ep_new_index.rename(columns={'episodeNumber': 'episode_number', 'seasonNumber': 'season'})
    rel_ep_num = df_new.loc[1, 'episode_number']
    rel_seson_num = df_new.loc[1, 'season']

    # unite the base DF with the quotes
    df_work1 = df_new[df_new['episode_number'] == rel_ep_num]
    df_work2 = df_work1[df_work1['season'] == rel_seson_num]
    df_relevant_ep = df_work2.merge(df_lines, how="inner", on=["season","episode_number"], )

    # group by charecters
    df_final = pd.DataFrame(df_relevant_ep.groupby(by=["author"], as_index=False))
    df_final['number_of_lines'] = pd.DataFrame(df_relevant_ep.groupby(by=["author"], as_index=False).count()['quote_order'])
    df_final = df_final.sort_values(by = 'number_of_lines',ascending=False )
    df_final = df_final.reset_index()

    # orgenazing the data
    df_final['episode_number'] = rel_ep_num
    df_final['season_number'] = rel_seson_num
    df_final = df_final.drop(columns = [1,'index'])
    df_final.rename(columns={0: 'character_name'} ,inplace = True )
    df_final = pd.DataFrame(df_final)
    return df_final

def who_said_it(csv_folder, character_name, phrase):
    """
    Args:
        csv_folder: containing csv files
        character_name:
        phrase: sentence or a word

    Returns: how many times this character uses the phrase
    """

    # creating data Frame and parameters
    rel_phrase = phrase.lower()
    rel_char = character_name.lower()
    df_lines = pd.read_csv('\\friends_quotes.csv')
    df_lines_per_char = df_lines
    df_lines_per_char['quote'] = df_lines_per_char.apply(lambda l: l['quote'].lower(), axis=1)
    df_lines_per_char['author'] = df_lines_per_char.apply(lambda l: l['author'].lower(), axis=1)

    # filtering to the relevant DF
    df_chosen_char = df_lines_per_char[df_lines_per_char['author'] == rel_char]
    df_final = df_chosen_char[df_chosen_char['quote'].str.contains(rel_phrase)]
    num_of_phrase = df_final.shape[0]

    return num_of_phrase



