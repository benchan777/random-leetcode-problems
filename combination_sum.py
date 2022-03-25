def combinationSum(candidates, target):
  ans = []
  dfs(candidates, target, [], ans)
  return ans

def dfs(nums, target, path, ans):
  if target < 0:
    return 
  if target == 0:
    ans.append(path)
    return 
  for i in range(len(nums)):
    dfs(nums[i:], target-nums[i], path+[nums[i]], ans)

print(combinationSum([2,3,6,7], 7))