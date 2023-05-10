# 315535518, 316539196
# 6.0
# part C question 5
def csv2list(csv_file_path, read_all):
    """
    This function target is to parse a csv file in to a list of lists.
    :param path: location of the relevant file
    :param read_all: boolean expression
    :return: list of lists, every list within the big list is a line from the csv file,
    and every element within the lists inside the big one is a cell from the original file.
    """
    l_final = []
    l_answer = []  # data parsed as list of lists without the ending sign
    f1 = open(csv_file_path, 'r')

    if read_all:
        # Reading all the information within the file as one bach
        s1 = f1.read()
        all_lines = s1.split("\n")
        for curr_line in all_lines:
            s2 = str(curr_line)
            second_line = s2.split(",")
            l_final.append(second_line)
    else:
        while True:
            s1 = f1.readline()
            first_line = s1.split(",")
            first_line[len(first_line) - 1] = first_line[len(first_line) - 1][
                                              0:len(first_line[len(first_line) - 1]) - 1]

            l_final.append(first_line)
            if s1 == '':
                break
    f1.close()

    # reorganizing data
    for index in range(0, len(l_final) - 1):
        l_answer.append(l_final[index])

    return l_answer


# part C question 6
def check_first_lines(code_file_path):
    """

    :param code_file_path: location of the relevant file
    :return: if the input is valid, return True
    in any other case return False
    """
    file = open(code_file_path, 'r')
    line1 = file.readline()
    line2 = file.readline()
    line1 = line1[:-1]
    line2 = line2[:-1]

    if line1[1] != " " or line2[1] != " " or line1[12] != " ":
        return False
    else:
        first_line = line1.split(' ')
        first_line[1] = first_line[1][:-1]
        second_line = line2.split(" ")

        is_numbers = second_line[1].split('.')

        if first_line[0] == second_line[0] == '#' and \
                first_line[1].isnumeric() and first_line[2].isnumeric() and \
                len(first_line[1]) == len(first_line[2]) == 9 and \
                "." in second_line[1] and is_numbers[0].isnumeric() and is_numbers[1].isnumeric() and \
                len(second_line) == 2 and \
                len(first_line) == 3:
            return True
        else:
            return False