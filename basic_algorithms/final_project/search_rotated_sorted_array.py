def rotated_array_search(input_list, target):
    input_length = len(input_list)

    # input list is empty
    if input_length == 0:
        return -1

    # find pivot point
    pivot_index = find_pivot_index(input_list, 0, input_length-1)
    if not pivot_index:
        pivot_index = 0

    if target == input_list[pivot_index]:
        return pivot_index
    if target > input_list[pivot_index]:
        return binary_search(input_list, target, 0, pivot_index)
    return binary_search(input_list, target, pivot_index + 1, len(input_list))


def find_pivot_index(input_list, left, right):
    mid = (left + right) // 2
    if left > right:
        return
    if input_list[mid - 1] > input_list[mid]:
        return mid
    if input_list[left] < input_list[mid] and input_list[right] < input_list[mid]:
        return find_pivot_index(input_list, mid + 1, right)
    return find_pivot_index(input_list, left, mid - 1)


def binary_search(input_list, target, left, right):
    mid = (left + right) // 2
    if left > right:
        return -1
    if input_list[mid] == target:
        return mid
    if input_list[mid] > target:
        return binary_search(input_list, target, left, mid - 1)
    return binary_search(input_list, target, mid + 1, right)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], 10])
test_function([[1], 10])
