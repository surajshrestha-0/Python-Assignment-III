""""
Bubble Sort is the simplest sorting algorithm that works
by repeatedly swapping the adjacent elements if they are in wrong order.
"""


# Python program for implementation of Bubble Sort

def bubbleSort(input_list):
    list_length = len(input_list)
    # initial index of all elements in the given list
    for i in range(list_length):
        for j in range(0, list_length - i - 1):
            # swapping index if previous element is greater than next element
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]


disorder_list = [105, 21, 39, 404, 125, 16, 70]
print('List Before Bubble Sort \n', disorder_list)
bubbleSort(disorder_list)
print('\nList After Bubble Sort \n', disorder_list)
