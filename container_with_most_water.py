def maxArea(height):
  left = 0
  right = len(height) - 1
  max_area = (right - left) * min(height[left], height[right])
  
  while right - left > 0:
    print('-----')
    print(f"left index: {left} -> {height[left]}")
    print(f"right index: {right} -> {height[right]}")
    if height[left] < height[right]:
      left += 1
      max_area = max(((right - left) * min(height[left], height[right])) ,max_area)
    else:
      right -= 1
      max_area = max(((right - left) * min(height[left], height[right])) ,max_area)
  return max_area

  #   min_height = min(height[left], height[right])
    
  #   if height[left] == min_height and height[left + 1] > min_height:
  #     left += 1
  #     max_area = max(((right - left) * min(height[left], height[right])) ,max_area)
  #   elif height[right] == min_height and height[right - 1] > min_height:
  #     right -= 1
  #     max_area = max(((right - left) * min(height[left], height[right])) ,max_area)
  #   else:
  #     # return max_area
  #     left += 1
  #     right -= 1
  #     max_area = max(((right - left) * min(height[left], height[right])) ,max_area)
  # return max_area

print(maxArea([1,3,2,5,25,24,5]))