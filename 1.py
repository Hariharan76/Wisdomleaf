# Problem 1:
# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same
# element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,3], target = 6
# Output: [0,1]



def two_sum(nums, target):
    num_indices = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[nums[i]] = i
    
    
    return []
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))
nums = [3,3]
target = 6
print(two_sum(nums,target))
