"""
Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element
and partitioning the array around it such that: Left side of pivot contains all the elements that are less than
the pivot element Right side contains all elements greater than the pivot
"""


# Python program for implementation of Quick Sort
def partition(input_list, low, high):
    i = (low - 1)  # index of smaller element
    pivot = input_list[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if input_list[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]

    input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(input_list, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(input_list, low, high)

        # Separately sort elements before partition and after partition
        quickSort(input_list, low, pi - 1)
        quickSort(input_list, pi + 1, high)


disorder_list = [105, 21, 39, 404, 125, 16, 70]
n = len(disorder_list)
print('List Before Quick Sort \n', disorder_list)
quickSort(disorder_list, 0, n - 1)
print('\nList After Quick Sort \n', disorder_list)
