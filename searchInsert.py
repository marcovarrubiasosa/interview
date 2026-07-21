def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

assert 2 == searchInsert( nums = [1,3,5,6], target = 5)
assert 1 == searchInsert( nums = [1,3,5,6], target = 2)
assert 4 == searchInsert( nums = [1,3,5,6], target = 7)
