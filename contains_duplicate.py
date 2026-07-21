def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if j - i > k:
                break
            if nums[i] == nums[j]:
                return True
    return False

assert True == containsNearbyDuplicate([1, 2, 3, 1], 3)  # True
assert True == containsNearbyDuplicate([1, 0, 1, 1], 1)  # True
assert False == containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)  # False
