import ex5a
import pandas as pd

if __name__ == "__main__":
    run_part_a_tests = True
    run_part_b_tests = True

    if run_part_a_tests:
        # A1
        df = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7]})
        df_filtered = ex5a.filter_numeric_column(df, 'col1', 2, 4)
        df_filtered = df_filtered.reset_index(drop=True)
        df_answer_test1 = pd.DataFrame(data={'col1': [2, 3], 'col2': [4, 5]})  # the correct answer
        df_answer_test1 = df_answer_test1.reset_index(drop=True)
        assert (df_filtered.equals(df_answer_test1))

        # A2
        df = pd.DataFrame(data={'col2': [3, 4, 5, 6, 7], 'col1': [1, 2, 3, 4, 5]})
        df_switched = ex5a.switch_col_names(df, 'col2', 'col1')
        df_answer_test2 = pd.DataFrame(data={'col1': [3, 4, 5, 6, 7], 'col2': [1, 2, 3, 4, 5]})  # the correct answer
        assert (df_switched.equals(df_answer_test2))

        # A3
        df = pd.DataFrame(data={'letter': ['h', 'a', 'b', 'c', 'i'], 'value': [3, 4, 5, 6, 7]})
        df_doubled = ex5a.double_special_letters(df, 'letter', 'value', 'col_res')
        df_answer_test3 = pd.DataFrame(data={'letter': ['h', 'a', 'b', 'c', 'i'], 'value': [3, 4, 5, 6, 7],
                                             'col_res': [6, 4, 5, 6, 14]})  # the correct answer
        assert (df_doubled.equals(df_answer_test3))

        # A4
        df = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7]})
        items_together = ex5a.put_row_items_together(df, 'res1')
        df_answer_test4 = pd.DataFrame(data={'col1': [1, 2, 3, 4, 5], 'col2': [3, 4, 5, 6, 7],
                                             'res1': [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]})  # the correct answer

    if run_part_b_tests:
        pass
