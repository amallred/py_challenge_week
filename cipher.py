'''
Create a Caesar cipher
'''

# def caesar_cipher(text, shift):
#     return ''.join(chr(ord(char) + shift) for char in text)
    # ord returns unicode int of char
    # chr returns string char of unicode int
    # This changes the letter to the unicode int, adds the shift, then converts back to a letter
    # This works, but shifts out of the alphabet and into special characters


# Source - https://stackoverflow.com/a/30825099
# Posted by Aditya, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-29, License - CC BY-SA 3.0

def caesar_cipher(text,key):
    return "".join([
        chr((ord(i) - 97 + key) % 26 + 97) 
        if (ord(i) <= 123 and ord(i) >= 97) 
        or (ord(i) <= 91 and ord(i) >= 65) 
        else i for i in text
        ])


print(caesar_cipher("abc", 3)) #Output:  "def"  
print(caesar_cipher("xyz", 2)) #Output:  "zab"  
print(caesar_cipher("Hello, World!", 5)) #Output:  "Mjqqt, Btwqi!"

'''
References: 
    - https://stackoverflow.com/questions/48514673/shift-letters-by-a-certain-value-in-python 
    - https://stackoverflow.com/questions/30825012/shifting-within-a-list-when-past-end-range 
'''