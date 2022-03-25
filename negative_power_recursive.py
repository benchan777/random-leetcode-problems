# Write a recursive function that allows raising to a negative integer power

def negative_power(a, b):
    if b == 1:
        return 1 / a

    return (1 / a) * negative_power(a, b  - 1)

print(negative_power(8, 2))