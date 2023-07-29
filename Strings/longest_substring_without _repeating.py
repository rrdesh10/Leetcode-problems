def lenghthlongstring(st):
    n = len(st)
    maxlength = 0
    cset = set()
    left = 0

    for right in range(n):
        if st[right] not in cset:
            cset.add(st[right])
            maxlength = max(maxlength, right - left + 1)
        else:
            while st[right] in cset:
                cset.remove(st[left])
                left += 1
            cset.add(st[right])

    return maxlength


print(lenghthlongstring("abcababb"))
