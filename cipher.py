'''
Create a Caesar cipher
'''

# def caesar_cipher(text, shift):
#     return ''.join(chr(ord(char) + shift) for char in text)
    # ord returns unicode int of char
    # chr returns string char of unicode int
    # This changes the letter to the unicode int, adds the shift, then converts back to a letter
    # This works, but shifts out of the alphabet and into special characters

def caesar_cipher(text,key):
    translated = ''
    for char in text:
        if char.islower():
            translated += chr((ord(char) - 97 + key) % 26 + 97)
        elif char.isupper():
            translated += chr((ord(char) - 65 + key) % 26 + 65)
        else: 
            translated += char
    return translated

''' 
I had to alter the reference code to account for if the character was upper or lower case
'''

print(caesar_cipher("abc", 3)) #Output:  "def"  
print(caesar_cipher("xyz", 2)) #Output:  "zab"  
print(caesar_cipher("Hello, World!", 5)) #Output:  "Mjqqt, Btwqi!"


'''
References: 
    - https://stackoverflow.com/questions/48514673/shift-letters-by-a-certain-value-in-python 
    - https://stackoverflow.com/questions/30825012/shifting-within-a-list-when-past-end-range 
'''