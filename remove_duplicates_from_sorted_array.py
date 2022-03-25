# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# class Solution:
def removeDuplicates(nums) -> int:
    i = 0
    j = 1

    while i < len(nums) - 1:
        if nums[i] == nums[j]:
            nums.remove(nums[i])
        else:
            i += 1
            j += 1

    return len(nums)


# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,1,2]))