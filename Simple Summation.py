""" Simple Summation

EN
বাং
Problem Statement
Write a program that calculates and prints the sum of two numbers entered by the user.

Input
The input consists of two integers.

Output
Output a single line containing the sum of two integers.

Constraints
-2 31 ≤ |S| ≤ 231 - 1
Example:
Enter two numbers

Input:
5 2
Output:
7 """

num1, num2 = map(int, input().split())

sum= num1 + num2

print(sum)