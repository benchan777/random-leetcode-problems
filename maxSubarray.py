# def maxSubarray(m, array):
#   local_max = 0
#   global_max = 0

#   for i in range(len(array)):
#     local_max = max(array[i], array[i] + local_max)

#     if local_max > global_max:
#       global_max = local_max

def maxSubarray(m, array):
  global_max = 0

  local_max = 0
  left = 0
  right = 0

  total_sum_so_far = 0

  while right < len(array):
    local_max += array[right]
    total_sum_so_far += array[right]
    
    if (right - left) + 1 >= m:
      global_max = max(global_max, local_max)
      local_max -= array[left]

      left += 1
      right += 1
    else:
      right += 1

  return(total_sum_so_far - global_max)

maxSubarray(2, [10,4,8,13,20])