""" Even or Odd?

EN
বাং
Problem Statement
Write a program that checks if a number entered by the user is even or odd.

Input
The input consists of a integer.

Output
Output a single line explaining whether it is even or odd.

Constraints
-2 31 ≤ |S| ≤ 231 - 1
Example-1:
Enter a number

Input:
7
Output:
7 is an odd number.
Example-2:
Enter a number

Input:
8
Output:
8 is an even number. """


a=int(input())

if a%2==0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")