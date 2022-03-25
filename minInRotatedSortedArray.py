def findMin(nums):
  startIndex = 0
  endIndex = len(nums) - 1
  
  while endIndex - startIndex != 1:
    midpoint = (endIndex + startIndex) // 2
    if nums[startIndex] > nums[midpoint]:
      endIndex = midpoint
    else:
      startIndex = midpoint
  return min(nums[startIndex], nums[endIndex])

findMin([11,13,15,17])