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

    # Your code here


    return -1  # not found
