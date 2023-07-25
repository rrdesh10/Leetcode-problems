def threesum(l):
    l = sorted(l)
    output = set()

    for k in range(len(l)):
        target = -l[k]
        i, j = k + 1, len(l) - 1
        while i < j:
            sum_two = l[i] + l[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                output.add((l[k], l[i], l[j]))
                i += 1
                j -= 1

    return output


print(threesum([-1, 0, 1, 2, -1, -5]))
