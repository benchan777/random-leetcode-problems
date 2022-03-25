def sortColors(nums):
  left = 0
  pointer = 0
  right = len(nums) - 1
  
  #[2,0,2,1,1,0] if left == 2 and right == 0, swap. decrement both
  #[0,0,2,1,1,2] 0, 1. do nothing. increment left
  #[0,0,2,1,1,2] 2, 1. swap left and right. decrement both
  #[0,0,1,1,2,2] 1, 2. do nothing
  
  #[1,1,0,2,2,0]
  #[0,1,0,2,2,1]
  #
  
  while pointer <= right:
    if nums[pointer] == 0:
      nums[pointer], nums[left] = nums[left], nums[pointer]
      left += 1
      pointer += 1
    elif nums[pointer] == 2:
      nums[pointer], nums[right] = nums[right], nums[pointer]
      right -= 1
    else:
      pointer += 1

  return nums

print(sortColors([2,0,1]))