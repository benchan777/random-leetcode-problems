def sort(lst, index = 0):
  n = len(lst)

  if index == n-1:
    return lst

  else:
    return sort(sort_helper(lst, index, index, index), index + 1)

def sort_helper(lst, pointer_1 = 0, pointer_2 = 1, low = 0):
    n = len(lst)

    if pointer_2 == n:

        if lst[pointer_1] > lst[low]:
            lst[low], lst[pointer_1] = lst[pointer_1], lst[low]
        
        return lst

    else:

        if lst[pointer_2] < lst[low]:
            low = pointer_2
          
        return sort_helper(lst, pointer_1, pointer_2 + 1, low)


print(sort([10, 3, 5, 1, 2, 91]))
print(sort([8, 6, 4, 10, 7, 1, 9]))
print(sort([10, 3, 5, 1, 2, 91, 3]))
