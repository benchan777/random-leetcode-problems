def threeSum(nums):
  sorted_nums = sorted(nums)
  result_array = []
  print(sorted_nums)
  prev = None
  pointer1 = 1
  pointer2 = len(nums) - 1
  
  for i in range(len(nums) - 2):
    if sorted_nums[i] == prev:
      prev = sorted_nums[i]
      pointer1 += 1
      continue
      
    target = 0 - sorted_nums[i]
    
    left = pointer1
    right = pointer2
      
    while left < right:
      if sorted_nums[left] + sorted_nums[right] > target:
        right -= 1
      elif sorted_nums[left] + sorted_nums[right] < target:
        left += 1
      elif sorted_nums[left] + sorted_nums[right] == target:
        result_array.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
        prevleft = sorted_nums[left]
        prevright = sorted_nums[right]
        left += 1
        right -= 1
        while sorted_nums[left] == prevleft and sorted_nums[right] == prevright and left < right:
          left += 1
          right -= 1
      else:
        break
    pointer1 += 1
    prev = sorted_nums[i]
      
  return result_array

# threeSum([-1,0,1,2,-1,-4])
# threeSum([-2,0,0,2,2])
threeSum([0,0,0,0])