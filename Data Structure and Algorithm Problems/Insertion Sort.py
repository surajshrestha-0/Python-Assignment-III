"""
Insertion sort is based on the idea that one element from the input elements is consumed in
each iteration to find its correct position i.e, the position to which it belongs in a sorted array.
"""


# Python program for implementation of Insertion Sort

def insertionSort(input_list):
    # from 1 to length of given list
    for i in range(1, len(input_list)):
        element = input_list[i]
        # Move elements, to one position ahead of their current position if greater than element
        j = i - 1
        while j >= 0 and element < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = element


disorder_list = [105, 21, 39, 404, 125, 16, 70]
print('List Before Insertion Sort \n', disorder_list)
insertionSort(disorder_list)
print('\nList After Insertion Sort \n', disorder_list)
