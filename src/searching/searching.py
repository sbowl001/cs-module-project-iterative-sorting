def linear_search(arr, target):
    # Your code here

    n = len(arr)
    for i in range(0, n):
        if (arr[i] == target):
            return i
    return -1   # not found

arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]
print(linear_search(arr1, 7))
# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    index = 0
    length = len(arr) - 1 

    while index <= length:
        midpoint = index + (length - 1) // 2

        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            index = midpoint + 1 

        else: 
            length = midpoint - 1 


    return -1  # not found


arr2 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr2, -8))