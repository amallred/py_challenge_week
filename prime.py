'''
Determine if a number is prime
'''

def is_prime(n):
    number = n -1
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        while number > 1:
            if n % number == 0:
                # print(n % number)
                return False
            elif n % number > 0:
                number -= 1
        return True

print(is_prime(2))     #Output: True 
print(is_prime(11))  #Output: True  
print(is_prime(15))  #Output: False  
print(is_prime(1))  #Output:  False 
print(is_prime(0)) #Output:  False  