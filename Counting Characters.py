""" Problem Statement
Write a program that counts the number of characters in a string entered by the user.

Input
The input is a string.

Output
Output the number of characters.

Constraints
Output will be an unsigned integer.
Example:
Enter a string

Input:
Alice
Output:
5 """

a=input()
count=0
for i in a:
    count+=1
print(count)