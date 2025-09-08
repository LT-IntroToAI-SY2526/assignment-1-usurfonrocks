# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience with java and html. Can you create 5-7 practice problems that cover: > - Variables and basic data types > - Conditionals (if/elif/else) > - Loops (for and while) > - Functions > - Basic list operations > > Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
Problem 1: Simple Calculator (Variables and Basic Data Types)


Description:
Write a program that asks the user to input two numbers and then prints the sum, difference, product, and quotient.

Example:

Input:
Enter first number: 8
Enter second number: 4

Output:
Sum: 12
Difference: 4
Product: 32
Quotient: 2.0


Hint: Use input() to read numbers and float() or int() to convert them.

Problem 2: Grade Checker (Conditionals)


Description:
Ask the user to enter a test score (0–100). Then print the letter grade according to this scale:

90–100: A

80–89: B

70–79: C

60–69: D

Below 60: F

Example:

Input:
Enter your score: 85

Output:
You got a B.


Hint: Use if, elif, and else.

Problem 3: Even or Odd Counter (Loops + Conditionals)


Description:
Write a program that asks the user to enter 5 numbers. After all numbers are entered, print how many were even and how many were odd.

Example:

Input:
Enter number 1: 4
Enter number 2: 7
Enter number 3: 12
Enter number 4: 3
Enter number 5: 8

Output:
Even numbers: 3
Odd numbers: 2


Hint: Use a for loop and the modulus operator %.

Problem 4: Password Checker (Loops + Conditionals)


Description:
Create a simple password checker. The correct password is "python123". Ask the user to enter a password. Keep asking until they get it right or they try 3 times.

Example:

Input:
Attempt 1: java456
Attempt 2: python
Attempt 3: python123

Output:
Access granted.


Or:

Input:
Attempt 1: test1
Attempt 2: test2
Attempt 3: test3

Output:
Access denied.


Hint: Use a while loop with a counter.

Problem 5: Function: Multiply List Elements (Functions + Lists)


Description:
Write a function multiply_list(numbers, factor) that takes a list of numbers and a factor, and returns a new list where each number is multiplied by the factor.

Example:

Input:
multiply_list([1, 2, 3], 5)

Output:
[5, 10, 15]


Hint: Use a for loop inside the function.

Problem 6: Find the Maximum (Functions + Loops + Lists)


Description:
Write a function find_max(numbers) that returns the largest number in a list without using the built-in max() function.

Example:

Input:
find_max([3, 11, 7, 2, 9])

Output:
11


Hint: Start with the first item as the "current max" and loop through the list to compare.

Problem 7: Palindrome Checker (Strings + Functions + Conditionals)

Description:
Write a function is_palindrome(word) that checks whether a word is a palindrome (it reads the same backward as forward).

Example:

Input:
is_palindrome("racecar")

Output:
True

Input:
is_palindrome("python")

Output:
False

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
num1 = 10
num2 = 20
resultAdd = num1 + num2
resultSubtract = num1 - num2
resultMultiply = num1 * num2
resultDivide = num1 / num2
print("sum: " + resultAdd)
print("quotient: " + resultDivide)
print("product: " + resultMultiply)
print("difference: " + resultSubtract)


print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


