'''
Find max in a list of numbers 
'''

def find_max(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
        else:
            continue
    return max

print(find_max([-1, -2, -3, -4, -5]))
print(find_max([4, 9, 1, 17, 2]))   #Output : 17  
print(find_max([-5, -9, -2, -12])) #Output :  -2  
print(find_max([42]))  #Output : 42

