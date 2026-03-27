''' 
Check if a string is a palindrome.
'''

def is_palindrome(string):
    clean = string.lower().replace(" ", "")
    reversed = clean[-1::-1]
    if clean == reversed:
        return f"Yes, '{string}' is a palindrome."
    else:
        return f"No, '{string}' is not a palindrome."
    
print(is_palindrome("RACEcar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))