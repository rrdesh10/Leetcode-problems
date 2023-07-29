def search(nums, target):
    pivot = nums.index(min(nums))
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[(mid + pivot) % len(nums)] > target:
            right = mid - 1
        elif nums[(mid + pivot) % len(nums)] < target:
            left = mid + 1
        else:
            return (mid + pivot) % len(nums)

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 3))
