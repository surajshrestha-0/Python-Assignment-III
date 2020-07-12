"""
Linear search is a very simple search algorithm.
In this type of search, a sequential search is made over all items one by one.
Every item is checked and if a match is found then that particular item is returned,
otherwise the search continues till the end of the data collection.
"""


# If x is present then return its location, otherwise return -1

def linearSearch(arr, x):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


arr1 = [2, 3, 4, 10, 40]
x = 10
result = linearSearch(arr1, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)
