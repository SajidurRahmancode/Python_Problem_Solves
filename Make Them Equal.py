""" Make Them Equal

EN
বাং
Problem Statement
You are given an array of integers of size 
N
N. In one operation you can either increase or decrease one element in the array by 1 unit. What is the minimum number of operations required to make all the elements of the array equal?

Input
Input consists of two lines. First one having one integer 
N
N. Next line contains 
N
N integers.

Output
Print the minimum number of operations required to make all the elements of the array equal.

Constraints
1
1 
≤
≤ 
N
N 
≤
≤ 
1
0
5
10 
5
 
Every integer of the array is between 
1
1 and 
1
0
5
10 
5
 
Example 1:
Input:
5
1 1 3 2 1
Output:
3
Example 2:
Input:
4
1 2 3 4
Output:
4 """

def min_operations_to_equal(arr):
    arr.sort()
    median = arr[len(arr) // 2]
    total_operations = 0
    for num in arr:
        total_operations += abs(num - median)
    return total_operations

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the result
print(min_operations_to_equal(arr))
  