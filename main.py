
def binary_search(array, target):

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
