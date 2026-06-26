
def removeElement(nums: List[int], val: int) -> int:
    k = 0
    for x in nums:
        if x != val: nums[k], k = x, k+1
    return k

assert removeElement([3,2,2,3], 3) == 2
assert removeElement([0,1,2,2,3,0,4,2], 2) == 5
