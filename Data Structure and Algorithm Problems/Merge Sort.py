"""
Merge sort is a sorting technique based on divide and conquer technique.
With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.
Merge sort first divides the array into equal halves and then combines them in a sorted manner.
"""

# Python program for implementation of MergeSort
# Merges two subarrays of arr[]. First subarray is arr[l..m], Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    left = [0] * n1
    right = [0] * n2

    # Copy data to temp arrays left[] and right[]
    for i in range(0, n1):
        left[i] = arr[l + i]

    for j in range(0, n2):
        right[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left[], if there are any
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right[], if there are any
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if left < right:
        m = (left + (right - 1)) // 2
        # Sort first and second halves
        mergeSort(arr, left, m)
        mergeSort(arr, m + 1, right)
        merge(arr, left, m, right)


disorder_list = [105, 21, 39, 404, 125, 16, 70]
n = len(disorder_list)
print('List Before Insertion Sort \n', disorder_list)
mergeSort(disorder_list, 0, n - 1)
print('\nList After Insertion Sort \n', disorder_list)
