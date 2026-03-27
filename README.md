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
- [ ] Return a message instead of a Boolean (e.g., "Yes, it's a palindrome!")
- [ ] Make the function case-insensitive without altering the original input
- [ ] I still want to figure out removing punctuation

This is a great real-world-style logic challenge that builds on your string handling skills — and also prepares you for upcoming projects where cleaning and normalizing data is key.