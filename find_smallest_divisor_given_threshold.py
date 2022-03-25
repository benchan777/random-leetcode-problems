def smallestDivisor(nums, threshold):
  # [1,11,22,33,44]
  nums.sort()
  left = 1
  right = max(nums)

  while right > left:
    midpoint = left + (right - left) // 2
    current_sum = 0

    for num in nums:
      result = -1 * (-num // midpoint)
      current_sum += result

    if current_sum > threshold:
      left = midpoint + 1
    else:
      right = midpoint
      # if midpoint < smallest_divisor:
      #   smallest_divisor = midpoint

  return left

print(smallestDivisor([1,2,5,9], 6))
# print(smallestDivisor([44,22,33,11,1], 5))
