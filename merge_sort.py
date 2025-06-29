def merge_sort(array):
    # Base case: if array has 0 or 1 element, it's already sorted
    if len(array) <= 1:
        return array
    
    # Split the array into two halves
    middle_index = len(array) // 2
    left_half = array[:middle_index]
    right_half = array[middle_index:]
    
    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    merged_result = []
    left_index, right_index = 0, 0
    
    # Compare elements from both halves and add the smaller one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_result.append(left[left_index])
            left_index += 1
        else:
            merged_result.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from either half
    merged_result.extend(left[left_index:])
    merged_result.extend(right[right_index:])
    
    return merged_result

# Test cases
test1 = merge_sort([9, 8])
print(test1)  # Output: [8, 9]

test2 = merge_sort([38, 27, 43, 3, 9, 82, 10])
print(test2)  # Output: [3, 9, 10, 27, 38, 43, 82]