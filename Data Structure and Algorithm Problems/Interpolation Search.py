"""
The Interpolation Search is an improvement over Binary Search for instances,
where the values in a sorted array are uniformly distributed.
Binary Search always goes to the middle element to check.
On the other hand, interpolation search may go to different locations
according to the value of the key being searched.
For example, if the value of the key is closer to the last element,
interpolation search is likely to start search toward the end side.
"""


# Python program to implement interpolation search

# If x is present in arr[0..n-1], then returns index of it, else returns -1
def interpolationSearch(coll, arr_len, x):
    low = 0
    high = (arr_len - 1)

    while low <= high and coll[low] <= x <= coll[high]:
        if low == high:
            if coll[low] == x:
                return low
            return -1

        # Probing the position with keeping uniform distribution in mind.
        pos = low + int(((float(high - low) / (coll[high] - coll[low])) * (x - coll[low])))

        # If x is found
        if coll[pos] == x:
            return pos

        # If x is larger, x is in upper part
        if coll[pos] < x:
            low = pos + 1

        # If x is smaller, x is in lower part
        else:
            high = pos - 1

    return -1


arr = [1, 13, 15, 20, 21, 28, 33, 38]
n = len(arr)

x = 21
index = interpolationSearch(arr, n, x)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
