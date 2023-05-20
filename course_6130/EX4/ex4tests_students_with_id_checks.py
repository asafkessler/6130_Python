import ex4a, ex4b
import matplotlib.image
import numpy as np


def is_number(num_str):
    return num_str.strip().replace(".", "0").isdigit()


def check_valid_id(file_name):
    # Check file exists
    try:
        with open(file_name + ".py", "r") as ex_file:
            ids = ex_file.readline()
            time = ex_file.readline()
    except FileNotFoundError as e:
        raise Exception("File {0} is missing".format(file_name)) from e
    # Check file has 2 lines with #
    if not ids.startswith("#") or not time.startswith("#"):
        raise Exception("No # in two first lines of file {0}".format(file_name))
    # Verify ids and time validity
    ids_split = [x.strip() for x in ids[1:].split(",")]
    for one_id in ids_split:
        if not one_id.isdigit():
            raise Exception("Issue with ids in file {0}".format(file_name))
    if not is_number(time[1:]):
        raise Exception("Issue with time in file {0}".format(file_name))
    return True


if __name__ == "__main__":
    run_part_a_tests = True
    run_part_b_tests = True

    if run_part_a_tests:
        check_valid_id("ex4a")

        arr = np.array([[1, 2, 3], [5, 1, 4]])
        comparing_results = (ex4a.find_largest_n(arr, 2) == np.array([4, 5]))
        assert (comparing_results.all())

        arr = np.array([1, 2, 3, 4, 5, 6])
        comparing_results = (ex4a.find_even_larger_than(arr, 4) == np.array([6]))
        assert (comparing_results.all())

        arr_str = np.array(['a', 'b', 'c'])
        prefix_st = 'd'
        suffix_st = "D"
        comparing_results = (ex4a.add_prefix_suffix(arr_str, prefix_st, suffix_st) == ["daD", "dbD", "dcD"])
        assert (comparing_results.all())

        arr_str = np.array(["Count", "me", "please"])
        st = 'e'
        assert (ex4a.count_string_with_substring(arr_str, st) == 2)

    if run_part_b_tests:
        check_valid_id("ex4b")

    print("You passed all tests! :)\n"
          "Make sure you DON'T have any imports that you shouldn't include, \n"
          "that you DON'T print anything \n"
          "or have paths to your computer in your code!")
