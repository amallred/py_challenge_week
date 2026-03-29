'''
Write a function that reads a .txt file and counts how many times each word appears. Return a dictionary where the keys are words and the values are the number of times they appear.
'''
d = dict()
with open('text.txt', 'r') as file:
    # for line in file:
    #     print(line.strip())
    data = file.read().split(' ').translate(None, string.punctuation)
    for word in data:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])

'''
Reference: https://www.geeksforgeeks.org/python/python-count-occurrences-of-each-word-in-given-text-file/
'''