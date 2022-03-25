def sort(lst, pointer = 0):
    if pointer == len(lst) - 1:
        return lst
    
    a = sort_helper(lst, pointer)
    if lst[pointer] > lst[a]:
        lst[pointer], lst[a] = lst[a], lst[pointer]

    return sort(lst, pointer + 1)

def sort_helper(lst, pointer = 0):
    if pointer == len(lst)-1:
        return pointer
    a = sort_helper(lst, pointer + 1)

    if lst[pointer] < lst[a]:
        return pointer
        
    return a
 
print(sort([10, 3, 5, 1, 2, 91]))