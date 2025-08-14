def quickSort(arr):
    pivot = arr[0]
    left = []
    equal = []
    right = []
    
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)
    
    return left + equal + right

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Perform the partition
result = quickSort(arr)

# Print the result
print(' '.join(map(str, result)))


"""
solution explained with AI

To solve this problem, we need to partition an array into three parts based on a pivot element, which is always the first element of the array. The three parts are:

Left: Contains all elements less than the pivot.

Equal: Contains the pivot element itself.

Right: Contains all elements greater than the pivot.

The goal is to return a new array where the elements from the left part come first, followed by the equal part, and then the right part. The order of elements within the left and right parts does not matter.

Approach
Identify the Pivot: The pivot is the first element of the input array.

Partition the Array: Iterate through each element of the array (excluding the pivot if necessary, but in this problem, the pivot is part of the array and needs to be placed in the equal partition). For each element:

If the element is less than the pivot, add it to the left partition.

If the element is equal to the pivot, add it to the equal partition.

If the element is greater than the pivot, add it to the right partition.

Combine Partitions: Concatenate the left, equal, and right partitions into a single array and return it. 
"""