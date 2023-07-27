def maxSubarraySum(nums):
    # float(-inf) is float neg infinite used for comparison as lowermost value
    maxSum = float('-inf')
    currentSum = 0

    for num in nums:
        currentSum += num

        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0

    return maxSum


arraysum = maxSubarraySum([1 - 2, 1, -3, 4, -1, 2, 1, -5, 4])
print(arraysum)
