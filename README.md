# MCTEKK-PROBLEMS

# Problem A - Password generator
Write a password generator CLI. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


# Problem B - Maximum Edge of a Triangle
Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

Examples:

next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10

Notes:
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.


# Problem C - Triangle Type
Write a SQL query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:
Equilateral: It's a triangle with sides of equal length.
Isosceles: It's a triangle with 2 sides of equal length.
Scalene: It's a triangle with sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.


Input Format
The TRIANGLES table is described as follows:

![image](https://user-images.githubusercontent.com/71860659/206881455-aae71fa1-2bf9-489e-aafe-5e64c0a79fec.png)

Each row in the table denotes the lengths of each of a triangle's three sides.

Sample Input

![image](https://user-images.githubusercontent.com/71860659/206881411-e00879ba-f73f-4d41-86ed-090199d23df1.png)


Sample Output 

Isosceles

Equilateral

Scalene

Not A Triangle

Explanation

Values in the tuple (20,20,23) form an Isosceles triangle, because A=B.

Values in the tuple (20,20,20) form an Equilateral triangle, because A=B=C

Values in the tuple (20,21,22) form a Scalene triangle because A <> B <> C

Values in the tuple (13,14,30) cannot form a triangle because the combined value of sides A and B is not larger than that of side C.
