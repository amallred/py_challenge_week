''' 
Reverse a string using the slice method
'''

def reverse_string(string):
    return string[-1::-1]

print(reverse_string("hello world slice"))

''' 
Reverse a string manually using `for` loop
Does this count as manually?
'''

def reverse_string_loop(string):
    new_string = ''
    for char in reversed(string):
        new_string += char
    return new_string

print(reverse_string_loop("HELLO FOR LOOP"))

''' 
Ignore whitespace or punctuation
'''

def reverse_string_loop_alpha(string):
    new_string = ''
    for char in reversed(string):
        if char.isalpha():
            new_string += char
        else:
            continue
    return new_string

print(reverse_string_loop_alpha("Hello NO spaces"))

''' 
Make it work for a list
'''

def reverse_list(input_list):
    return list(reversed(input_list))

print(reverse_list(['apples', 'bananas', 'potatoes']))

