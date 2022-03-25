def reverse_int_iterative(num):
    reversed_num = 0

    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num = num // 10

    return reversed_num

def reverse_int_recursive(num, rev = 0):
    if num == 0:
        return rev

    rev  = (rev * 10) + (num % 10)
    num = num // 10
    return reverse_int_recursive(num, rev)

def reverse_int_condensed(num, rev = 0):
    return rev if num == 0 else reverse_int_condensed(num // 10, (rev * 10) + (num % 10))

print(reverse_int_recursive(123456))
print(reverse_int_condensed(123456))