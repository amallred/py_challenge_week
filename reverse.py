''' 
Reverse a string using the slice method
'''

def reverse_string(string):
    return string[-1::-1]

print(reverse_string("hello"))
print(reverse_string("world"))
print(reverse_string("hello world"))

''' 
Reverse a string manually using `for` loop
Does this count as manually?
'''

def reverse_string_loop(string):
    new_string = ''
    for char in reversed(string):
        new_string += char
    return new_string

print(reverse_string_loop("HELLO"))