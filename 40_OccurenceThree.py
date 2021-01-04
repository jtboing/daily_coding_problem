def once_from_three(lst):
    """
    Select one non-duplicated integer from any other integers that occur three times in the list
    """
    
    numbers = {}

    for number in lst:
        if number not in numbers:
            numbers[number] = 1
        elif number in numbers:
            numbers[number] += 1

    numbers_keys = list(numbers.keys())
    numbers_values = list(numbers.values())

    non_duplicated_number = numbers_keys[numbers_values.index(1)]
    print(non_duplicated_number)

lst = [6, 1, 3, 3, 3, 6, 6]
once_from_three(lst)

lst = [13, 19, 13, 13]
once_from_three(lst)