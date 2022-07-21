
def binary_search(array, target):

    """
    it is good for searching in sorted array and has more efficiency than linear search
    :param array: list of numbers
    :param target: the number of you're following
    :return: index of the target in array and if there isn't, return -1
    """

    array = sorted(array)
    start = 0
    end = len(array) - 1

    while end >= start:
        middle = start + (end-start)//2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            end = middle
        elif target > array[middle]:
            start = middle + 1

    return -1


def linear_search(array, target):

    """
    it is used for searching in array which is not sorted
    :param array: list of numbers
    :param target: the number of you're following
    :return: index of the target in array and if there isn't, return -1
    """

    for i in range(len(array)):
        if target == array[i]:
            return i
    return -1

