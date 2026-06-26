def majorityElement(nums: List[int]) -> int:
    count = 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate

assert majorityElement([3,2,3]) == 3
assert majorityElement([2,2,1,1,1,2,2]) == 2
assert majorityElement([1,1,1,2,3,4]) == 1
