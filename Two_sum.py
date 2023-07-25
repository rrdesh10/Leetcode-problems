def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, (len(nums))):
            if target == nums[i] + nums[j]:
                return [i, j]
    return "No"


s = two_sum([2, 13, 11, 7], 9)
print(s)
