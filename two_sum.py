def twoSum(nums, target):
    numberDict = {}

    for i in range(len(nums)):
        result = target - nums[i]

        if result in numberDict:
            return numberDict.get(result), i
        else:
            numberDict[nums[i]] = i
    
# nums = [2, 7, 11, 15]
# target = 9

nums = [3,2,4]
target = 6

print(twoSum(nums, target))