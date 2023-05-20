import ex4a, ex4b
import matplotlib.image
import numpy as np

if __name__ == "__main__":
    run_part_a_tests = True
    run_part_b_tests = True

    if run_part_a_tests:
        arr = np.array([[1, 2, 3], [5, 1, 4]])
        comparing_results = (ex4a.find_largest_n(arr, 2) == np.array([4, 5]))
        assert (comparing_results.all())

        arr = np.array([[1, 2, 3], [5, 4, 4]])
        comparing_results = (ex4a.find_largest_n(arr, 3) == np.array([4, 4, 5]))
        assert (comparing_results.all())
        print("find_largest_n works Great!")

        arr = np.array([1, 2, 3, 4, 5, 6])
        comparing_results = (ex4a.find_even_larger_than(arr, 4) == np.array([6]))
        assert (comparing_results.all())
        print("find_even_larger_than works Great!")

        arr_str = np.array(['a', 'b', 'c'])
        prefix_st = 'd'
        suffix_st = "D"
        comparing_results = (ex4a.add_prefix_suffix(arr_str, prefix_st, suffix_st) == ["daD", "dbD", "dcD"])
        assert (comparing_results.all())
        print("add_prefix_suffix works Great!")

        arr_str = np.array(["Count", "me", "please"])
        st = 'e'
        assert (ex4a.count_string_with_substring(arr_str, st) == 2)
        print("count_string_with_substring works Great!")

        if run_part_b_tests:
            pass