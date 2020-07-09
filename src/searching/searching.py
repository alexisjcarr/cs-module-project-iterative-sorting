def linear_search(arr, target):
    for idx, num in enumerate(arr):
        if num == target:
            return idx
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)

    found = False
    while end >= start and not found: 
        # get the middle point
        middle_index = (start + end) // 2 
        # compare the value in the middle with target
        # if the middle value is the same as target, set found to True
        if arr[middle_index] == target:
            found = middle_index
        # move start or end index closer to one another, and shrink our search space
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return -1 if found is False else found
