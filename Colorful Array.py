""" Colorful Array

EN
বাং
Problem Statement
You are given an array of integers of size 
N
N. You have to color the elements of the array in a such way that no adjacent elements have the same color and value.

If two adjacent elements have different values then you can use the same color.
What is the minimum number of colors required.

Input
Input consists of two lines. First one having one integer 
N
N. Next line contains 
N
N integers.

Output
Print the minimum number of colors required to color the array.

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
2
Example 2:
Input:
4
1 2 3 4
Output:
1 """

n, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

# Initialize dp array where dp[w] is the maximum value for weight w
dp = [0] * (W + 1)

for wi, vi in items:
    # Iterate from W down to wi to avoid reusing the same item multiple times
    for w in range(W, wi - 1, -1):
        if dp[w - wi] + vi > dp[w]:
            dp[w] = dp[w - wi] + vi

print(max(dp))