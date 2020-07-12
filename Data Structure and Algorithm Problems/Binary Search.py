"""
Binary search looks for a particular item by comparing the middle most item of the collection.
If a match occurs, then the index of item is returned.
If the middle item is greater than the item, then the item is searched
in the sub-array to the left of the middle item. Otherwise, the item is searched for
in the sub-array to the right of the middle item.
This process continues on the sub-array as well until the size of the subarray reduces to zero.
"""


# Returns index of x in arr if present, else -1
def binary_search(collection, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if collection[mid] == x:
            return mid
        # If element is smaller than mid, then it can only be present in left subarray
        elif collection[mid] > x:
            return binary_search(collection, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(collection, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


collection = [4, 22, 32, 47, 404]
x = 404

result = binary_search(collection, 0, len(collection) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
