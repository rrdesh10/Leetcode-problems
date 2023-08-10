def findmin(nums:list[int]) -> int:
    l = 0
    r = len(nums)-1

    while l < r:
        m = l + (r-1)

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    
    return nums[l]

findmin([3,4,5,1,2])
