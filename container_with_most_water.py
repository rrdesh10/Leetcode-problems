def maxcontainer(arr):
    maxarea = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            maxarea = max(maxarea, min(arr[j], arr[i]) * (j-i))
    return maxarea


print(maxcontainer([1, 8, 6, 2, 5, 4, 8, 3, 7]))
