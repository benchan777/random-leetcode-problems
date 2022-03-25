def linear_search_iterative(lst, target):
    for i in lst:
        if i == target:
            return i
    return "Item not found"

def linear_search_recursive(lst, target):
    if not lst:
        return "Item not found"
    if lst[0] == target:
        return target
    return linear_search_recursive(lst[1:], target)

print(linear_search_iterative([1, 10, 100], 10))
print(linear_search_iterative([1, 10, 100], 99))

print(linear_search_recursive([1, 10, 100], 10))
print(linear_search_recursive([1, 10, 100], 99))