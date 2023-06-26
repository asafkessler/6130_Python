# id1, id2
# time
import csv

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy
import pandas as pd
import os
import random
import csv


'''
        build the classifier
        clf = RandomForestClassifier()
        self.forest_classifier = RandomForestClassifier() # parallel prediction tool
        total_number_of_row = len(self.data)
        random_features_index_array = random.sample(range(0, int(total_number_of_row)), 5)
        # test the classifier
        clf.predict(test_set[features])

        # calculate accuracy
        accuracy_score(test_set['result'], clf.predict(test_set[features]))
        accuracy_score(train_set['result'], clf.predict(train_set[features]))
'''

PATH = r"C:\devl\work\6130 Python\course_6130\EX7\data_nature_processed.csv"
FEATURES_SIZE = 10
CSV_NAME = "sample_n"
SIZE_OF_FOREST = 3

def data_set_genesis(path, number_of_sample):
    if os.path.exists(path):
        csv_file = pd.read_csv(path)
        array_random_col_index = []

        total_number_of_cols = len(csv_file.columns)
        random_features_index_array = random.sample(range(0, int(total_number_of_cols)-1), FEATURES_SIZE)

        last_col = csv_file.iloc[:, total_number_of_cols-1]
        relative_df = csv_file.iloc[:, random_features_index_array]
        relative_df.insert(FEATURES_SIZE, "result", last_col)

        name = CSV_NAME + str(number_of_sample) + ".csv"
        relative_df.to_csv(name) # Use CSV using openpyxl package
    else:
        raise ValueError("Please send a correct Path to the function.")
def data_set_separator(data, labels):
    index_num_of_row = len(data) # 75 rows

    train = data.loc[0: (index_num_of_row-5)]
    labels_train = labels.loc[0: (index_num_of_row-5)]

    test = data.loc[index_num_of_row-5: index_num_of_row]
    labels_test = labels.loc[index_num_of_row-5: index_num_of_row]
    return (train, labels_train) , (test, labels_test)

class RandomForest(object):
    def __init__(self, data, labels = None):
        self.labels = data.iloc[:, len(data.columns) - 1]
        self.data = data.iloc[:, range(0, len(data.columns) - 1)]
        self.tree_list = []
        self.tuple_train, self.tuple_test = data_set_separator(self.data, self.labels)

        for i in range(0 ,SIZE_OF_FOREST):
            tree_clf = DecisionTreeClassifier()
            curr_tree = tree_clf.fit(self.tuple_train[0], self.tuple_train[1])
            self.tree_list.append(curr_tree)

    def error_evaluation(self, other_data, other_label):
        final_prediction = []
        other_data.reset_index(inplace=True, drop=True)

        for index in range(1, len(other_data)+1):
            curr_row = other_data.loc[index]
            list_predictions = []
            print(curr_row)
            for curr_tree in self.tree_list:
                list_predictions.append(curr_tree.predict(curr_row)) # happens 5 by 101 times

            forest_prediction = True
            forest_result = sum(list_predictions)
            if forest_result <= 50:
                forest_prediction = False

            final_prediction.append(forest_prediction) # happens 5 times

        counter = 0
        for index in range(0, len(other_label)):
            if final_prediction[index] == other_label[index]:
                counter += 1

        return str(counter*20) + "%"


if __name__ == "__main__":
    # data_set_genesis(PATH, 1)
    data_set = pd.read_csv(r"C:\devl\work\6130 Python\course_6130\EX7\sample_n1.csv")
    data_set.reset_index(inplace=True, drop=True)
    data_set.drop(columns=data_set.columns[0], axis=1, inplace=True)

    test_rf = RandomForest(data_set, None)
    result = test_rf.error_evaluation(test_rf.tuple_test[0], test_rf.tuple_test[1])
    print(result)
