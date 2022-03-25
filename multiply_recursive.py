# Write a function for mutliply(a, b), where a and b are both positive
# integers, but you can only use the + or − operators.

def multiply(a, b):
    if b == 1:
        return a
    
    else:
        return a + multiply(a, b - 1)

print(multiply(4, 5))