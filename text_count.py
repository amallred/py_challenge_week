'''
Write a function that reads a .txt file and counts how many times each word appears. Return a dictionary where the keys are words and the values are the number of times they appear.
'''
import re
import string

d = dict()

with open('text.txt', 'r') as file:
    data = file.read().replace('\n', ' ') # new line removed
    split_data = re.split(('[^\\w\\n]'), data) # removes everything except (^): letters/numbers (\w), new lines (\n) 

    for word in split_data:
        if word == '':
            continue
        for char in word:
            if char in string.punctuation:
                print(char)

        
        if word.lower() in d:
            d[word.lower()] = d[word.lower()] + 1
        else:
            d[word.lower()] = 1

for key in list(d.keys()):
    print(key, ":", d[key])

'''
Reference: https://www.geeksforgeeks.org/python/python-count-occurrences-of-each-word-in-given-text-file/
(also, LOTS AND LOTS of Googling to figure out the regex)
'''