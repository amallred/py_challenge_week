# Python Challenge Week
This is a part of Code:You's Data Analysis cohort.

## Challenge: Reverse That String!
### Problem
Write a function that takes a single string as input and returns that string in reverse order.
#### File: 
reverse.py

### Example

``` 
reverse_string("hello") # will output: olleh
reverse_string("Python") # will output: nohtyP 
```
 
### Your Task
- Define a function called reverse_string that accepts one argument (a string).
- Return the reversed version of the string.
- Try using string slicing as a first approach.
- Bonus: After you get it working, try writing a second version using a for loop to build the reversed string manually.
### Concepts Tested
- String manipulation
- Indexing and slicing
- Looping through strings (if attempting the bonus)
- Function definition and return values
### Stretch Ideas
- [x] Add a feature that ignores whitespace or punctuation
- [x] Make the function work for lists as well as strings
- [ ] Compare the performance of slicing vs loop methods for long strings

This one may seem simple, but thinking about different ways to solve it builds fluency — and will help with trickier string problems later.

--- 

## Is It a Palindrome?
## Problem
Write a function that checks whether a given string is a palindrome — a word or phrase that reads the same backward as forward (ignoring capitalization, spaces, and punctuation).
#### File:
palindrome.py

### Examples

```
is_palindrome("racecar") # Output: True
is_palindrome("hello") # Output: False
is_palindrome("A man a plan a canal Panama") # Output: True
``` 
### Your Task
- Define a function called is_palindrome that accepts a single string.
- Return True if the string is a palindrome, and False otherwise.
- Normalize the string by:
  - Converting it to lowercase
  - Removing spaces (and optionally punctuation)
- Reverse the normalized string and compare it to the original normalized version.
  - Converting it to lowercase
  - Removing spaces (and optionally punctuation)
### Concepts Tested
- String normalization
- Comparison logic
- Function design and return values
- Optional: working with Python's re (regular expression) module for bonus cleanup
### Stretch Ideas
- [ ] Use regular expressions to remove all non-alphanumeric characters
- [ ] Adapt the function to check if a number is a palindrome
- [x] Return a message instead of a Boolean (e.g., "Yes, it's a palindrome!")
- [ ] Make the function case-insensitive without altering the original input
- [ ] *I still want to figure out removing punctuation

This is a great real-world-style logic challenge that builds on your string handling skills — and also prepares you for upcoming projects where cleaning and normalizing data is key.

---

## Challenge: Find the Max
### Problem
Write a function that takes a list of numbers and returns the maximum value in the list — the largest number.
#### File
max.py

### Examples

```
find_max([4, 9, 1, 17, 2])   #Output : 17  
find_max([-5, -9, -2, -12]) #Output :  -2  
find_max([42])  #Output : 42
```

### Your Task
- Define a function called `find_max` that accepts a list of integers or floats.
- Return the largest number in the list.
- Do not use the built-in `max()` function — try to solve it manually using:
  - A `for` loop to check each number
  - A variable to track the current maximum
  - A `for` loop to check each number
  - A variable to track the current maximum
### Concepts Tested
- Looping through a list
- Comparison and conditional logic
- List handling
- Defensive programming (optional)
### Stretch Ideas
- [ ] Add error handling for empty lists
- [x] Allow the function to work with mixed positive and negative values
- [ ] Return both the max value and its index in the list
- [ ] Rewrite it using a while loop instead of a for loop

Hint: You’ll need a variable to hold the current highest number as you loop through the list and update it whenever you find a bigger one.

---

## Challenge: Prime Time
### Problem
Write a function that checks whether a number is prime. A prime number is a number greater than 1 that has no divisors other than 1 and itself.
#### File:
prime.py

## Examples

```
is_prime(2)     #Output: True 
is_prime(11)  #Output: True  
is_prime(15)  #Output: False  
is_prime(1)  #Output:  False  
is_prime(0) #Output:  False  
```
### Your Task
Define a function called is_prime that takes one integer as input.
Return True if the number is prime and False otherwise.
Use a loop to check divisibility — don’t use any external libraries or built-in prime checkers.

### Concepts Tested
- Conditional logic
- Loops
- Modulo operator (%)
- Efficiency and edge case handling

### Stretch Ideas
- [ ] Improve performance by only looping up to the square root of the number
- [ ] Write a second function that returns all prime numbers up to a given number
- [ ] Accept user input and check multiple numbers in one run
- [ ] Save all prime results to a file

### Hints:
- Any number less than 2 is not prime.
- Use % to check for divisibility.
- If any number between 2 and n-1 divides evenly into n, it’s not prime.

### Why It Matters
Prime checks are a classic example of how math and code intersect. They’re useful in cryptography, number theory, and performance testing. And they’re a great way to practice clean looping logic and working with conditionals.

--- 

## Challenge: Caesar Cipher Encoder
### Problem
A Caesar cipher is a simple encryption technique where each letter in a message is shifted a fixed number of places down the alphabet. For example, shifting "a" by 3 gives you "d".

Write a function that takes a string and a shift value and returns the encoded message using the Caesar cipher.
#### File:
cipher.py

### Examples
```
caesar_cipher("abc", 3) #Output:  "def"  
caesar_cipher("xyz", 2) #Output:  "zab"  
caesar_cipher("Hello, World!", 5) #Output:  "Mjqqt, Btwqi!"
```

### Your Task
- Define a function called caesar_cipher that accepts:
  - a string text
  - an integer shift
- Return a new string with each alphabetical character shifted by the shift amount.
- Keep the case (uppercase/lowercase) the same.
- Do not change non-letter characters like punctuation, spaces, or numbers.
  - a string text
  - an integer shift

### Concepts Tested
- String manipulation
- Character encoding with `ord()` and `chr()`
- Modulo math for wrapping the alphabet
- Control flow and logic

### Stretch Ideas
- [x]Add a second function to decode messages by shifting in the opposite direction
- [x]Allow the user to input text and shift value
- [x]Handle very large or negative shift values
- [ ]Save the encoded message to a file

### Hints:
- Use `ord()` to get the Unicode value of a character.
- Use `chr()` to convert back to a character.
- Wrap around the alphabet using % 26 when needed.
- Make sure to handle both uppercase and lowercase letters correctly.

### Why It Matters
Understanding the Caesar cipher helps you practice control flow, ASCII manipulation, and the modulo operator — all fundamental tools in Python. While the cipher itself is simple, the logic behind correctly shifting characters while preserving case and punctuation is a great test of your programming clarity.

---
# Bonus Challenges
## Challenge: Count Word Frequency in a Text File
### Problem
Write a function that reads a .txt file and counts how many times each word appears. Return a dictionary where the keys are words and the values are the number of times they appear.

#### Example

Given a file with:

"The cat and the hat."

Your output might be:

``` 
{'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
```
#### File:
text_count.py

### Your Task
- Open and read a .txt file (you can create a small practice file if needed)
- Normalize the text (e.g., lowercase, remove punctuation)
- Split the text into words
- Use a dictionary to count word frequencies
- Return or print the dictionary

### Concepts Tested
- File reading
- String cleanup
- Dictionaries and loops

### Stretch Ideas
- [ ] Sort the output by most frequent words
- [ ] Ignore very common stop words like “the,” “and,” etc.
- [ ] Save the results to a new file

---