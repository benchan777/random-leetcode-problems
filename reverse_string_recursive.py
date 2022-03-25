def rev(str):
    array = str.split()
    return rev_helper(array, len(array))

def rev_helper(array, index = 0):
    if index == 0:
        return ' '.join(array)

    return rev_helper(array[::-1], index - 1)

def rev_2(str):
    return ' '.join(str.split()[::-1])

def reverse_sentence(string):
  if isinstance(string, str):
    str_array = string.split(' ')
    return str_array[-1] + " " + reverse_sentence(str_array[:-1])
  else:
    if len(string) == 1:
      return string[0]
    else:
      return string[-1] + " " + reverse_sentence(string[:-1])

print(rev_2('test words here'))