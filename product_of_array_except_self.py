def productExceptSelf(nums):
    result = []
    acc = 1

    # left to right
    for n in nums:
        result.append(acc)
        acc *= n

    acc = 1
    # right to left
    for i in reversed(range(len(nums))):
        result[i] *= acc
        acc *= nums[i]

    return result


ans = productExceptSelf([1, 2, 3, 4])
print(ans)
