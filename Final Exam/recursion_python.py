# understanding recursion in python


def calc_list_values(l_numbers):
    if len(l_numbers) == 1:
        return l_numbers[0]
    return l_numbers.pop(0) + calc_list_values(l_numbers)


if __name__ == "__main__":
    l_numbers = [1,2,3,4,5,6,7,8,9]
    print(calc_list_values(l_numbers))