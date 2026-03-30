import datetime

'''
Create a file for a basic log that saves the date/time and log to a txt file
'''

with open('log.txt', 'a') as file:
    entry = input("Enter log here: ")
    timestamp = datetime.datetime.now().replace(microsecond=0)
    file.write(f'[{timestamp}] {entry}\n')