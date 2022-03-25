def solve(s):
    return " ".join([word.capitalize() for word in s.split(" ")])

def swap_case(s):
    temp_string = ''
    for i in s:
        if i.isupper() == True:
            temp_string = temp_string + i.lower()
            
        elif i.islower() == True:
            temp_string = temp_string + i.upper()
            
        else:
            temp_string = temp_string + i
        
    return temp_string

def repeatedString(s, n):
    a_counter = s.count('a') * (n // len(s))
    new_string = ''
        
    if n % len(s) > 0:
        for i in range(0, n % len(s)):
            new_string = new_string + s[i]
            
    a_counter = a_counter + new_string.count('a')
    
    print(a_counter)

def jumpingOnClouds(c):
    jump_counter = 0
    index = 0

    while index < len(c) - 1:
        step = 2

        if step + index > len(c) - 1: # Check if attempting to jump past end of list
            step = 1

        if c[step + index] == 1:
            index += 1
            jump_counter += 1
        else:
            index += 2
            jump_counter += 1
    
    return jump_counter

def kangaroo(x1, v1, x2, v2):
    initial_jump_1 = x1 + v1
    initial_jump_2 = x2 + v2
    
    if initial_jump_1 == initial_jump_2:
        return 'YES'
    
    position_1 = initial_jump_1
    position_2 = initial_jump_2
    
    while max(position_1, position_2) < 10000:
        
        position_1 = position_1 + v1
        position_2 = position_2 + v2
        
        if position_1 == position_2:
            return 'YES'
        
    return 'NO'

def equalizeArray(arr):
    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return len(arr) - frequency[max(frequency, key = frequency.get)]

if __name__ == '__main__':
    print(equalizeArray(['1', '2', '3', '1', '2', '3', '3', '3']))