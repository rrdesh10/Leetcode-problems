def maxsum(nums):
    cmaxsubarr = 1
    cminsubarr = 1
    maxprod = nums[0]

    for n in nums:
        value = (n, n * cmaxsubarr, n * cminsubarr)
        cmaxsubarr, cminsubarr = max(value), min(value)
        maxprod = max(maxprod, cmaxsubarr)

    return maxprod


maxsum([2,3,-1,4])