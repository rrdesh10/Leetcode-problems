def duplicate(nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False


containsduplicate = duplicate([1, 2, 3, 0])
print(containsduplicate)
