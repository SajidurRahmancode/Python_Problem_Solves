def binary_search_recursive(arr, target):
    if len(arr) == 0:
        return -1
    mid = len(arr) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        result = binary_search_recursive(arr[:mid], target)
        return result
    else:
        result = binary_search_recursive(arr[mid+1:], target)
        return -1 if result == -1 else mid + 1 + result
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
result = binary_search_recursive(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
