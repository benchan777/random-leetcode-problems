#TODO: complete the following functions
# To test your functions, run the tests.

def binary_to_decimal(binary_str):
    """returns the decimal number for the given binary digits"""
    position = len(binary_str) - 1
    sum = 0

    for i in range(0, len(binary_str)):
        if binary_str[i] == '1':
            sum += 2 ** position
        position -= 1
    return sum

def decimal_to_binary(decimal_num):
    """the binary representation of the given decimal number"""
    binary_str = ''

    while decimal_num / 2 >= 1:
        binary_str = binary_str + str(decimal_num % 2)
        decimal_num = decimal_num // 2

    if decimal_num / 2 == 0.5:
        binary_str = binary_str + str(1)

    if decimal_num / 2 == 1:
        binary_str = binary_str + str(0)

    return binary_str[::-1]

print(binary_to_decimal('1101101'))
print(decimal_to_binary(6387))