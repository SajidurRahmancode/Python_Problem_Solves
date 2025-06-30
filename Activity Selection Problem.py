""" Problem Statement
You are given 
N
N activities with their start and finish times. Find the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

Input
Input consists of 
N
+
1
N+1 lines. First one having one integer 
N
N. Next 
N
N lines contain two integers 
S
,
E
S,E each, the start and end time.

Output
Print the maximum number of activities that can be performed by a single person.

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
 
1
≤
S
≤
E
≤
1
0
9
1≤S≤E≤10 
9
 
Example 1:
Input:
5
1 5
3 4
2 6
5 7
9 12
Output:
3
Example 2:
Input:
3
1 3
3 6
6 8
Output:
3
"""

def max_activities(activities):
    # Sort activities based on their finish times
    activities.sort(key=lambda x: x[1])
    
    count = 1
    last_end = activities[0][1]
    
    for i in range(1, len(activities)):
        current_start, current_end = activities[i]
        if current_start >= last_end:
            count += 1
            last_end = current_end
    
    return count

# Read input
n = int(input())
activities = []
for _ in range(n):
    s, e = map(int, input().split())
    activities.append((s, e))

# Calculate and print the result
print(max_activities(activities))

