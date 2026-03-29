"""
Write a function that reads a .txt file and counts how many times each word appears. Return a dictionary where the keys are words and the values are the number of times they appear.
"""
import re
import string

d = dict()
stop_words = ["","a", "an", "and", "the", "of"]

with open('text.txt', 'r') as file:
    data = file.read().replace('\n', ' ') # new line removed
    split_data = re.split(('[^\\w\\n]'), data) # removes everything except (^): letters/numbers (\w), new lines (\n) 

    for word in split_data:
        if word in stop_words:
            continue
        for char in word:
            if char in string.punctuation:
                print(char)

        
        if word.lower() in d:
            d[word.lower()] = d[word.lower()] + 1
        else:
            d[word.lower()] = 1

organized_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
for key in list(organized_dict.keys()):
    print(key, ":", organized_dict[key])

"""
Reference: https://www.geeksforgeeks.org/python/python-count-occurrences-of-each-word-in-given-text-file/
(also, LOTS AND LOTS of Googling to figure out the regex)
"""