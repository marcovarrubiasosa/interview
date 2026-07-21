def twoSum(nums, target):
    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in nums[:i]:
            return [nums[:i].index(needed), i]

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

nums = [3,2,4]
target = 6
print(twoSum(nums, target))

nums = [3,3]
target = 6
print(twoSum(nums, target))
