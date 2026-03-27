''' 
Check if a string is a palindrome.
'''

def is_palindrome(string):
    clean = string.lower().replace(" ", "")
    reversed = clean[-1::-1]
    return clean == reversed

print(is_palindrome("RACEcar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))