""" Problem Statement:

Whenever George asks Lily to hang out, she's busy doing homework. George wants to help her finish it faster, but he's in over his head! Can you help George understand Lily's homework so she can hang out with him?

Consider an array of 
n
n distinct integers, 
a
r
r
=
[
a
[
0
]
,
a
[
1
]
,
…
,
a
[
n
−
1
]
]
arr=[a[0],a[1],…,a[n−1]]. George can swap any two elements of the array any number of times. An array is beautiful if the sum of 
∣
a
r
r
[
i
]
−
a
r
r
[
i
−
1
]
∣
∣arr[i]−arr[i−1]∣ among 
0
<
i
<
n
0<i<n is minimal.

Given the array 
a
r
r
arr, determine and return the minimum number of swaps that should be performed in order to make the array beautiful.

Example:

For 
a
r
r
=
[
7
,
15
,
12
,
3
]
arr=[7,15,12,3], one minimal array is 
[
3
,
7
,
12
,
15
]
[3,7,12,15]. To achieve this, George performed the following swaps:

Swap 3 and 7:
[
7
,
15
,
12
,
3
]
→
[
3
,
15
,
12
,
7
]
[7,15,12,3]→[3,15,12,7]

Swap 7 and 15:
[
3
,
15
,
12
,
7
]
→
[
3
,
7
,
12
,
15
]
[3,15,12,7]→[3,7,12,15]

It took 2 swaps to make the array beautiful. This is minimal among the choices of beautiful arrays possible.

Function Description:

Complete the lilysHomework function in the editor below.

Parameters:

int arr[n]: an integer array.

Returns:

int: the minimum number of swaps required.

Input Format:

The first line contains a single integer, 
n
n, the number of elements in 
a
r
r
arr.

The second line contains 
n
n space-separated integers, 
a
r
r
[
i
]
arr[i].

Constraints:

1
≤
n
≤
10
5
1≤n≤10 
5
 

1
≤
a
r
r
[
i
]
≤
2
×
10
9
1≤arr[i]≤2×10 
9
 

Sample Input:

text
4
2 5 3 1
Sample Output:

text
2
Explanation:

Define 
a
r
r
′
=
[
1
,2,3,5]
arr ′=[1,2,3,5] to be the beautiful reordering of arr. The sum of the absolute values of differences between its adjacent elements is minimal among all permutations, and only two swaps (1 with 2 and then 2 with 5) were performed.

This problem requires finding the minimum number of swaps needed to transform the given array into a beautiful array, where the sum of absolute differences between adjacent elements is minimized. The solution involves sorting the array in both ascending and descending order and determining the minimal swaps required for either case.

 """





def lilysHomework(arr):
    def calculate_swaps(original, target):
        pos = {val: idx for idx, val in enumerate(original)}
        swaps = 0
        temp = original.copy()
        for i in range(len(temp)):
            if temp[i] != target[i]:
                swaps += 1
                correct_val = target[i]
                current_val = temp[i]
                # Swap in temp
                temp[i], temp[pos[correct_val]] = temp[pos[correct_val]], temp[i]
                # Update the positions in the pos dictionary
                pos[current_val] = pos[correct_val]
                pos[correct_val] = i
        return swaps
    
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)
    
    swaps_asc = calculate_swaps(arr.copy(), sorted_asc)
    swaps_desc = calculate_swaps(arr.copy(), sorted_desc)
    
    return min(swaps_asc, swaps_desc)

# Read input
n = int(input())
arr = list(map(int, input().split()))
print(lilysHomework(arr))

