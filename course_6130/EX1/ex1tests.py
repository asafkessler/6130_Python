import ex1
import mytoolbox

print("ex1tests.py __name__  = %s" % __name__)

if __name__ == "__main__":
    ex1_code_file_path = r"C:\devl\work\course_6130\EX1\ex1.py"  # you should change it
    mytoolbox_code_file_path = r"C:\devl\work\course_6130\EX1\mytoolbox.py"  # you should change it
    ex1_csv_example = r"C:\devl\work\course_6130\EX1\ex1_csv_example.csv"  # you should change it

    # Tests q2
    assert (ex1.max_count1([1, 2, 3, 3, 3]) == [3, 3])
    assert (ex1.max_count1([-1, 3, -1, 3]) == [3, 2])
    assert (ex1.max_count1([1, 4, 2, 10, 102]) == [102, 1])
    assert (ex1.max_count2([1, 2, 3, 3, 3]) == [3, 3])
    assert (ex1.max_count2([-1, 3, -1, 3]) == [3, 2])
    assert (ex1.max_count2([1, 4, 2, 10, 102]) == [102, 1])
    print("Passed all q2 tests")

    # Tests q3
    assert (ex1.is_numeric([1, 2, 3, 3, 3]) == False)
    assert (ex1.is_numeric(3) == True)
    assert (ex1.is_numeric(3.1) == True)
    print("Passed all q3 tests")

    # Tests q4
    assert (ex1.only_strings([1, "a", 2]) == ["a"])
    assert (ex1.only_strings([1, -1, 2]) == [])
    print("Passed all q4 tests")

    # Tests q5
    assert (mytoolbox.csv2list(ex1_csv_example, True) == [['each', 'word', 'is', 'in', 'a', 'different ', 'cell'],
                                                    ['different', 'lines', 'are', 'in', 'different ', 'sub', 'lists']])

    # Tests q6
    assert (mytoolbox.check_first_lines(ex1_code_file_path) == True)
    assert (mytoolbox.check_first_lines(mytoolbox_code_file_path) == True)
